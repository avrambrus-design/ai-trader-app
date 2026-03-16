import streamlit as st
from openai import OpenAI
import base64
from PIL import Image
import io

st.set_page_config(page_title="AI Trader", layout="wide")
st.title("📈 AI Trader Millionaire")

# Поле для ключа в левой колонке
key = st.sidebar.text_input("OpenAI API Key", type="password")
file = st.file_uploader("Загрузите скриншот графика", type=["jpg", "jpeg", "png"])

if file:
    img = Image.open(file)
    st.image(img, use_container_width=True)
    
    if st.button("🚀 Проанализировать сделку"):
        if not key:
            st.error("Ошибка: Сначала вставьте API Key в поле слева!")
        else:
            try:
                client = OpenAI(api_key=key)
                
                # Кодируем картинку
                buf = io.BytesIO()
                img.save(buf, format="JPEG")
                img_b64 = base64.b64encode(buf.getvalue()).decode()
                
                with st.spinner('Трейдер-миллионер изучает график...'):
                    # Запрос к нейросети (ВСЁ В ОДНОМ)
                    res = client.chat.completions.create(
                        model="gpt-4o",
                        messages=
                        }]
                    )
                    st.subheader("📊 Вердикт:")
                    st.write(res.choices.message.content)
            except Exception as e:
                st.error(f"Произошла ошибка: {e}")
