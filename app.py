import streamlit as st
import openai
import base64
from PIL import Image
import io

st.set_page_config(page_title="AI Trader", layout="wide")
st.title("📈 AI Trader Millionaire")

api_key = st.sidebar.text_input("OpenAI API Key", type="password")
uploaded_file = st.file_uploader("Загрузите график", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Ваш график', use_container_width=True)
    
    if st.button("🚀 Анализ"):
        if not api_key:
            st.error("Введите API Key!")
        else:
            try:
                client = openai.OpenAI(api_key=api_key)
                buffered = io.BytesIO()
                image.save(buffered, format="JPEG")
                img_str = base64.b64encode(buffered.getvalue()).decode()
                
                with st.spinner('Анализирую...'):
                    response = client.chat.completions.create
                        model="gpt-4o",
                        messages=
                    st.write(response.choices.message.content)
            except Exception as e:
                st.error(f"Ошибка: {e}")
