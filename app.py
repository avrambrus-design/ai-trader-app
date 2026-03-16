import streamlit as st
import openai
import base64
from PIL import Image
import io

# 1. Настройка страницы
st.set_page_config(page_title="AI Trader Millionaire", layout="wide")
st.title("📈 AI Trader Millionaire")
st.write("Загрузи график — получи вердикт профессионала.")

# 2. Боковая панель для ввода API-ключа
st.sidebar.header("Настройки")
api_key = st.sidebar.text_input("Введите OpenAI API Key", type="password")

# 3. Функция для подготовки картинки
def encode_image(image):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

# 4. Загрузка файла
uploaded_file = st.file_uploader("Загрузите скриншот графика", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Показываем загруженное фото
    image = Image.open(uploaded_file)
    st.image(image, caption='Твой график', use_container_width=True)
    
    # Кнопка запуска анализа
    if st.button("🚀 Проанализировать как Профи"):
        if not api_key:
            st.error("Ошибка: Сначала вставь API Key в поле слева!")
        else:
            try:
                # Инициализация клиента OpenAI
                from openai import OpenAI
                client = OpenAI(api_key=api_key)
                
                # Кодируем фото в текст для нейросети
                base64_image = encode_image(image)
                
                with st.spinner('Трейдер-миллионер изучает график...'):
                    # Запрос к нейросети GPT-4o
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=
                        ],
                        max_tokens=1000
                    )
                    
                    # Вывод результата на сайт
                    st.success("Анализ готов!")
                    st.subheader("📊 Вердикт Трейдера:")
                    st.write(response.choices.message.content)
                    
            except Exception as e:
                st.error(f"Произошла ошибка: {str(e)}")
else:
    st.info("Жду скриншот твоего графика.")
