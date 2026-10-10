import streamlit as st
from ai_functions import main_ai_function

# Настройка страницы[span_13](start_span)[span_13](end_span)
st.set_page_config(page_title="PC-Doctor AI", page_icon="🛠️")

st.title("🛠️ PC-Doctor AI")
st.caption("Умная проверка совместимости комплектующих вашего ПК.")


user_input = st.text_input(
    "Введите комплектующие ПК (например: OptiPlex 3020 и Quadro K620):",
    placeholder="Например: i5-4590, 8GB RAM, GTX 1050 Ti",
)


if st.button("✨ Проверить совместимость"):
    if not user_input.strip():
        st.warning("Пожалуйста, введите название комплектующих!") # (end_span)
    else:
        try:
            with st.spinner("Анализируем комплектующие..."):  #[span_18](start_span)[span_18](end_span)[span_19](start_span)[span_19](end_span)
                result = main_ai_function(user_input)

            # Крок 3: Вывод результата[span_20](start_span)[span_20](end_span)[span_21](start_span)[span_21](end_span)
            st.subheader("Результат проверки:")  #[span_22](start_span)[span_22](end_span)
            st.success(result)  #[span_23](start_span)[span_23](end_span)

        except Exception as e:
            st.error(f"Произошла ошибка при обработке: {e}")  #[span_24](start_span)[span_24](end_span)[span_25](start_span)[span_25](end_span)

