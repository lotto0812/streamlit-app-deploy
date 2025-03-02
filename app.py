from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import openai

# secrets.tomlファイルからAPIキーを取得
openai.api_key = st.secrets["OPENAI"]["OPENAI_API_KEY"]

from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage , SystemMessage

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0, api_key=openai.api_key)

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0, api_key=openai.api_key)

st.title("あなたはどんな人ですか")

st.write("##### 動作モード1: 名前おやじ")
st.write("##### 動作モード1: 誕生日魔神")
st.write("##### 動作モード2: BMIくん") 

selected_item = st.radio(
    "動作モードを選択してください。",
    ["名前", "誕生日", "BMI"]
)

if selected_item == "名前":
    name = st.text_input("名前を入力してください。") 
    if st.button("名前を覚える"):
        messages = [
            HumanMessage(content=f"私の名前は{name}です。")
        ]
        result = llm(messages)
        st.write(result.content)
elif selected_item == "誕生日":
    name = st.text_input("名前を入力してください。")
    birthday = st.text_input("誕生日を入力してください。")
    if st.button("名前と誕生日を覚える"):
        messages = [
            HumanMessage(content=f"私の名前は{name}です。誕生日は{birthday}です。")
        ]
        result = llm(messages)
        st.write(result.content)
elif selected_item == "BMI":
    name = st.text_input("名前を入力してください。")
    height = st.number_input("身長を入力してください。", min_value=0, max_value=300)
    weight = st.number_input("体重を入力してください。", min_value=0, max_value=300)
    if st.button("名前と身長と体重を覚える"):
        messages = [
            HumanMessage(content=f"私の名前は{name}です。身長は{height}cmです。体重は{weight}kgです。")
        ]
        result = llm(messages)
        st.write(result.content)

# 名前を覚え、名前を聞かれたら答える専門家
def remember_names():
    messages = [
        HumanMessage(content="私の名前は佐藤勇介です。Aさんの名前は加藤太郎です"),
        AIMessage(content="Aさんの名前は加藤太郎です。"),
        HumanMessage(content="私の名前が分かりますか？"),
        AIMessage(content="Aさんの名前は加藤太郎です。"),
        HumanMessage(content="私の名前が分かりますか？"),
        AIMessage(content="佐藤勇介さんです。"),
    ]
    result = llm(messages)
    print(result.content)

# 名前と誕生日を覚え、名前を入力したら誕生日を答える専門家
def remember_birthdays():
    messages = [
        HumanMessage(content="私の名前は佐藤勇介です。誕生日は1990年1月1日です。Aさんの名前は加藤太郎です。誕生日は1995年2月2日です。"),
        AIMessage(content="Aさんの名前は加藤太郎です。誕生日は1995年2月2日です。"),
        HumanMessage(content="私の名前が分かりますか？"),
        AIMessage(content="佐藤勇介さんです。誕生日は1990年1月1日です。"),
        HumanMessage(content="佐藤勇介さんの誕生日はいつですか？"),
        AIMessage(content="1990年1月1日です。"),
        HumanMessage(content="加藤太郎さんの誕生日はいつですか？"),
        AIMessage(content="1995年2月2日です。"),
    ]
    result = llm(messages)
    print(result.content)

# 名前と身長と体重を覚え、名前を入力したらBMIを答える専門家
def remember_bmi():
    messages = [
        HumanMessage(content="私の名前は佐藤勇介です。身長は170cmです。体重は60kgです。Aさんの名前は加藤太郎です。身長は160cmです。体重は50kgです。"),
        AIMessage(content="Aさんの名前は加藤太郎です。身長は160cmです。体重は50kgです。"),
        HumanMessage(content="私の名前が分かりますか？"),
        AIMessage(content="佐藤勇介さんです。身長は170cmです。体重は60kgです。"),
        HumanMessage(content="佐藤勇介さんのBMIはいくつですか？"),
        AIMessage(content="20.8です。"),
        HumanMessage(content="加藤太郎さんのBMIはいくつですか？"),
        AIMessage(content="19.5です。"),
    ]
    result = llm(messages)
    print(result.content)

# 必要に応じて関数を呼び出します
remember_names()
remember_birthdays()
remember_bmi()