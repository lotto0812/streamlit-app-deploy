
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
from openai import OpenAI
import openai
# secrets.tomlファイルからAPIキーを取得
api_key = st.secrets["OPENAI"]["OPENAI_API_KEY"]

# OpenAI APIに接続
openai.api_key = api_key
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