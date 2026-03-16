import streamlit as st
import openai
import base64
from PIL import Image
import io

# 1. Настройка страницы
st.set_page_config(page_title="AI Trader Millionaire", layout="wide")
st.title("📈 Анализ графика от Трейдера-Миллионера")

# 2. Боковая панель
st.sidebar.header("Настройки")
api_key = st.sidebar.text_input("Введите OpenAI API Key", type="password")

def encode_image(image):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

# 3. Основной функционал
uploaded_file = st.file_uploader("Загрузите скриншот графика", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Ваш график', use_container_width=True)
    
    if st.button("🚀 Проанализировать сделку"):
        if not api_key:
            st.error("Ошибка: Введите API Key в поле слева!")
        else:
            try:
                client = openai.OpenAI(api_key=api_key)
                base64_image = encode_image(image)
                
                with st.spinner('Анализирую рынок...'):
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=,
                            }
                        ],
                        max_tokens=500,
                    )
                    st.subheader("📊 Вердикт:")
                    st.write(response.choices.message.content)
            except Exception as e:
                st.error(f"Ошибка API: {str(e)}")
else:
    st.info("Ожидаю загрузку графика...")
