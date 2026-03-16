import streamlit as st
from openai import OpenAI
import base64
from PIL import Image
import io

st.set_page_config(page_title="AI Trader", layout="wide")
st.title("📈 AI Trader Millionaire")

# 1. Настройки в боковой панели
key = st.sidebar.text_input("OpenAI API Key", type="password")
file = st.file_uploader("Загрузите график", type=["jpg", "jpeg", "png"])

if file:
    img = Image.open(file)
    st.image(img, use_container_width=True)
    
    if st.button("🚀 Анализ"):
        if not key:
            st.error("Введите ключ!")
        else:
            try:
                client = OpenAI(api_key=key)
                
                # Кодируем картинку
                buf = io.BytesIO()
                img.save(buf, format="JPEG")
                raw_img = base64.b64encode(buf.getvalue()).decode('utf-8')
                
                # Готовим данные для запроса (разбиваем по частям, чтобы не запутаться)
                instruction = "Ты трейдер на $1,000,000. Дай точку входа, стоп и тейк по графику."
                img_data = {"url": f"data:image/jpeg;base64,{raw_img}"}
                
                content =
                
                with st.spinner('Анализирую...'):
                    # Сам запрос
                    res = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[{"role": "user", "content": content}]
                    )
                    st.subheader("Вердикт:")
                    st.write(res.choices.message.content)
            except Exception as e:
                st.error(f"Ошибка: {e}")
