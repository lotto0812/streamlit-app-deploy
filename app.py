
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
from openai import OpenAI
import openai
api_key = os.getenv('OPENAI_API_KEY')
#client = OpenAI(api_key=api_key)
openai.api_key = os.getenv('OPENAI_API_KEY')
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="こんにちは！私の名前は山田です。"),
    AIMessage(content="こんにちは、山田さん！お名前を教えていただきありがとうございます。何かお手伝いできることはありますか？"),
    HumanMessage(content="私の名前が分かりますか？"),
]

result = llm(messages)
print(result)