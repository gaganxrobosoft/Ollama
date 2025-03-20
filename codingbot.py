import streamlit as st
import ollama

def query_ollama(user_prompt):
    messages = [
        {"role": "system", "content": "You are a coding expert. Answer only questions related to programming and coding."},
        {"role": "user", "content": user_prompt}
    ]
    
    try:
        response = ollama.chat(
            model="gemma3:1b", 
            messages=messages, 
            options={"temperature": 0, "top_k": 40, "max_tokens": 150}
        )
        return response["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"
    
def main():
    st.title("Gemma3 Coding Assistant")
    st.write("Ask me anything about coding!")

    user_input = st.text_input("Ask your coding question:")

    if user_input:
        with st.spinner('Getting response...'):
            response = query_ollama(user_input)  
            st.write("Answer:")
            st.write(response)

if __name__ == "__main__":
    main()
