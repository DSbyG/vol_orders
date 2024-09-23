import streamlit as st
from decimal import Decimal
from helpers import calculate_order_volumes, calculate_avg_entry


# Добавим стили CSS для космической панели
def add_custom_css():
    st.markdown(
        """
        <style>
        body {
            background-color: #121212;
            color: #FFFFFF;
            font-family: 'Roboto Mono', monospace;
        }
        .stButton button {
            background-color: #03DAC6;
            color: #000000;
            border-radius: 12px;
            padding: 10px;
            font-size: 18px;
            font-weight: bold;
        }
        .stSlider .st-eg {
            background-color: #03DAC6;
            color: #FFFFFF;
        }
        .stNumberInput > div > input {
            background-color: #1E1E1E;
            color: #03DAC6;
        }
        .block-container {
            padding: 2rem;
            border: 2px solid #03DAC6;
            border-radius: 15px;
            background-color: #1E1E1E;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

# Основная функция расчета объемов ордеров
def calculate_order_volumes(vol1, mar, num_orders):
    volumes = [vol1]
    for i in range(1, num_orders):
        new_volume = volumes[-1] + (volumes[-1] * mar)
        volumes.append(new_volume)
    return volumes

# Функция для расчета средней цены входа
def calculate_avg_entry(prices, volumes):
    total_volume = sum(volumes)
    weighted_sum = sum([p * v for p, v in zip(prices, volumes)])
    avg_entry_price = weighted_sum / total_volume
    return avg_entry_price

# Streamlit интерфейс
# Основное приложение с интерфейсом космического корабля
def main():
    st.title("Калькулятор ордеров с увеличением объема")
    st.markdown("Приборная панель для управления ордерами")

    # Ввод данных
    deposit = float(st.number_input("Введите ваш депозит в $", min_value=100.00, max_value=100000.00, value=10000.00, format="%.2f"))
    num_orders = st.slider("Количество ордеров", min_value=1, max_value=8, value=3)
    vol1 = float(st.number_input("Объем первого ордера ($)", min_value=10.00, max_value=2000.00, value=100.00, format="%.2f"))
    mar = st.slider("Процент мартингейла (%)", min_value=10, max_value=40, value=30) / 100

    prices = []
    for i in range(num_orders):
        price = st.number_input(f"Цена входа для ордера {i+1}", value=0.0008555, format="%.10f")
        prices.append(price)

    # Расчет
    volumes = calculate_order_volumes(vol1, mar, num_orders)
    total_investment = sum(volumes)
    avg_entry_price = calculate_avg_entry(prices, volumes)

    # Вывод результатов
    st.write(f"Объемы ордеров: {volumes}")
    st.write(f"Всего в сделке: {total_investment}$")
    st.write(f"Средняя точка входа: {avg_entry_price}$")

if __name__ == "__main__":
    main()
