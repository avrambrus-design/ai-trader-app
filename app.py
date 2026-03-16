import streamlit as st
import openai
import base64
from PIL import Image
import io

# 1. Настройка внешнего вида страницы
st.set_page_config(page_title="AI Trader Millionaire", layout="wide")
st.title("📈 Анализ графика от Трейдера-Миллионера")
st.markdown("Загрузите скриншот графика, и ИИ проанализирует его как профессионал с доходом $1M/мес.")

# 2. Боковая панель для настроек
st.sidebar.header("Настройки")
api_key = st.sidebar.text_input("Введите OpenAI API Key", type="password", help="Ваш ключ sk-...")

# Функция для превращения картинки в понятный для ИИ формат
def encode_image(image):
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')

# 3. Загрузка файла
uploaded_file = st.file_uploader("Выберите скриншот графика (PNG, JPG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Ваш график для анализа', use_container_width=True)
    
    if st.button("🚀 Проанализировать сделку"):
        if not api_key:
            st.error("Ошибка: Сначала введите API Key в поле слева!")
        else:
            try:
                client = openai.OpenAI(api_key=api_key)
                base64_image = encode_image(image)
                
                with st.spinner('Анализирую рынок, ищу ликвидность...'):
                    # Тот самый запрос к GPT-4o
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=,
                            }
                        ],
                        max_tokens=800,
                    )
                    
                    # Вывод результата на экран
                    st.success("Анализ завершен!")
                    st.subheader("📊 Вердикт Трейдера-Миллионера:")
                    st.write(response.choices[0].message.content)
                    
            except Exception as e:
                st.error(f"Произошла ошибка: {str(e)}")
                st.info("Проверьте, пополнен ли баланс вашего OpenAI API и правильно ли введен ключ.")
else:
    st.info("Ожидаю загрузку скриншота графика...")

# Футер
st.sidebar.markdown("---")
st.sidebar.write("⚠️ Не является финансовой рекомендацией.")
