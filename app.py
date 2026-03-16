import streamlit as st
import openai
import base64
from PIL import Image
import io

st.set_page_config(page_title="AI Trader", layout="wide")
st.title("📈 AI Trader Millionaire")

# Поле для ключа
api_key = st.sidebar.text_input("OpenAI API Key", type="password")

# Загрузка фото
uploaded_file = st.file_uploader("Загрузите скриншот графика", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Ваш график', use_container_width=True)
    
    if st.button("🚀 Анализ"):
        if not api_key:
            st.error("Введите API Key в поле слева!")
        else:
            try:
                client = openai.OpenAI(api_key=api_key)
                
                # Кодируем картинку
                buffered = io.BytesIO()
                image.save(buffered, format="JPEG")
                img_str = base64.b64encode(buffered.getvalue()).decode()
                
                with st.spinner('Анализирую...'):
                    # Правильный и полный запрос к ИИ
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=
                            }
                        ]
                    )
                    st.subheader("Вердикт:")
                    st.write(response.choices.message.content)
            except Exception as e:
                st.error(f"Ошибка: {e}")
else:
    st.info("Загрузите скриншот графика для начала.")
