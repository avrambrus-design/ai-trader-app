import streamlit as st
import openai
import base64
from PIL import Image
import io

# Настройка страницы
st.set_page_config(page_title="AI Trader Millionaire", layout="wide")
st.title("📈 Анализ графика от Трейдера-Миллионера")

# Поле для API ключа (потом спрячем его в настройки)
api_key = st.sidebar.text_input("Введите OpenAI API Key", type="password")

def encode_image(image):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

uploaded_file = st.file_uploader("Загрузите скриншот графика", type=["jpg", "jpeg", "png"])

if uploaded_file and api_key:
    image = Image.open(uploaded_file)
    st.image(image, caption='Ваш график', use_column_width=True)
    
    if st.button("Проанализировать сделку"):
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
            
            st.subheader("Вердикт системы:")
            st.write(response.choices[0].message.content)
else:
    st.info("Пожалуйста, введите API ключ в боковой панели и загрузите фото.")
