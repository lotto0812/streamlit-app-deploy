
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

st.title("サンプルアプリ①: 簡単なWebアプリ")

input_message = st.text_input(label="文字数のカウント対象となるテキストを入力してください。")

text_count = len(input_message)

if st.button("実行"):

    st.write(f"文字数: **{text_count}**")
    print("a")

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