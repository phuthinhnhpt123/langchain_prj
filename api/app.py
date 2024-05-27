from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn

import os
# from dotenv import load_dotenv

# load_dotenv()

app = FastAPI(
    title='Langchain Server',
    version="1.0",
    description="A simple API Server"
)

# Ollama LLM
llm = Ollama(model='llama2')

prompt = ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 50 words")

add_routes(
    app,
    prompt|llm,
    path='/poem'

)

if __name__=='__main__':
    uvicorn.run(app,host='localhost',port=8000)
