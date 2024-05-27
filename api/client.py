import requests
import streamlit as st

def get_ollama_response(input_text):
    response=requests.post(
        "http://127.0.0.1:8000/poem/invoke",
        json={'input':{'topic':input_text}}
    )

    return response.json()['output']

st.title('Langchain Demo with Llama API')
input_text = st.text_input("Write a poem on")

if input_text:
    st.write(get_ollama_response(input_text))