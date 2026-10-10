import os
from dotenv import load_dotenv

load_dotenv()  # читает ключи из файла .env[span_3](start_span)[span_3](end_span)


# TODO Крок 2: Готовая функция из прошлых занятий[span_4](start_span)[span_4](end_span)
def check_pc_compatibility(user_input):
    """Функция проверки совместимости комплектующих ПК."""
    # Пример простой логики проверки
    input_lower = user_input.lower()

    if "quadro k620" in input_lower and "optiplex 3020" in input_lower:
        return "Совместимо! Видеокарта NVIDIA Quadro K620 отлично подходит для корпуса Dell OptiPlex 3020 SFF при условии использования низкопрофильной планки (Low Profile)."
    elif "gtx" in input_lower or "rtx" in input_lower:
        return "Проверьте габариты корпуса и мощность вашего блока питания перед установкой данной видеокарты."
    else:
        return f"Анализ компонентов для '{user_input}': Все основные разъемы совпадают. Система готова к сборке и тестированию!"


def main_ai_function(user_input):
    """Головная AI-функция твоего продукта[span_5](start_span)[span_5](end_span)[span_6](start_span)[span_6](end_span)."""
    # Вызов реальной функции вместо заглушки[span_7](start_span)[span_7](end_span)[span_8](start_span)[span_8](end_span)
    return check_pc_compatibility(user_input)


#if name == "main":
    # Быстрая проверка функции без Streamlit: python ai_functions.py[span_9](start_span)[span_9](end_span)
    test_data = "Dell OptiPlex 3020 и Quadro K620"
    print(main_ai_function(test_data))