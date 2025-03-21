import ollama
import mysql.connector
import pandas as pd
import streamlit as st

def connect_to_mysql():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="KMgagan271#",
        database="genai",
    )

def get_schema():
    conn = connect_to_mysql()
    cursor = conn.cursor()

    cursor.execute("SHOW TABLES;")
    tables = [table[0] for table in cursor.fetchall()]

    schema_info = ""
    for table in tables:
        cursor.execute(f"DESCRIBE {table};")
        columns = cursor.fetchall()
        schema_info += f"Table: {table}\n"
        schema_info += "Columns: " + ", ".join([f"{col[0]} ({col[1]})" for col in columns]) + "\n\n"

    conn.close()
    return schema_info.strip()

def generate_sql(user_input, schema_info):
    messages = [
        {"role": "system", "content": "You are a SQL assistant. Help generate SQL queries based on database schema."},
        {"role": "user", "content": f"Database Schema:\n{schema_info}"},
        {"role": "user", "content": f"Generate an SQL Query based on the following instructions:\n{user_input}"},
        {"role": "system", "content": "Provide the SQL query that fulfills the user's request. Make sure to respect the database schema provided."}
    ]
    
    response = ollama.chat(
        model="gemma3:1b",
        messages=messages,
        options={
            "temperature": 0,
            "top_k": 40,
            "max_tokens": 50
        }
    )

    return response["message"]["content"].strip("```sql").strip("```").strip()

def execute_sql(sql_query):
    conn = connect_to_mysql()
    try:
        df = pd.read_sql(sql_query, conn)  
        conn.close()
        return df
    except Exception as e:
        conn.close()
        return f"SQL Execution Error: {e}"

def main():
    st.title("Gemma3 SQL Assistant")
    st.write("Ask me to generate and execute SQL queries based on your instructions!")

    user_input = st.text_input("Enter your SQL query instruction:")

    if user_input:
        schema_info = get_schema()
        with st.spinner('Generating SQL query...'):
            sql_query = generate_sql(user_input, schema_info)
            st.write("Generated SQL Query:")
            st.code(sql_query, language='sql')

        with st.spinner('Executing SQL query...'):
            result = execute_sql(sql_query)
            if isinstance(result, pd.DataFrame):
                st.write("Query Results:")
                st.dataframe(result)
            else:
                st.error(result) 

if __name__ == "__main__":
    main()
