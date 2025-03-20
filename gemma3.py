import streamlit as st
import requests
import json

def query(user_prompt):
    url = 'http://localhost:11434/api/generate'
    sys_prompt = '''
    You are a chatbot designed solely to provide detailed explanations for the questions posed by the user.
    Your role is not to offer direct solutions, but to clarify concepts, elaborate on ideas, and guide the user to a better understanding of their query.
    '''
    payload = {'model' : 'gemma3:1b', 'prompt' : user_prompt, 'system' : sys_prompt}
    try:
        response = requests.post(url = url, json = payload, headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            result = response.text
            lines = result.strip().split("\n")
            full_response = "".join(json.loads(line)["response"] for line in lines)
            return full_response
        else:
            return "Error: Unable to reach the AI model service."
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    st.title("Gemma3")
    st.write("Ask me anything!")

    user_input = st.text_input("Ask any question:")

    if user_input:
        with st.spinner('Getting response...'):
            response = query(user_input)
            st.write("Answer:")
            st.write(response)

if __name__ == "__main__":
    main()