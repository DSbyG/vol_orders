from decimal import Decimal

def calculate_order_volumes(vol1, mar, num_orders):
    # Используем Decimal для vol1 и мар, чтобы гарантировать точность
    volumes = [Decimal(vol1)]
    for i in range(1, num_orders):
        new_volume = volumes[-1] + (volumes[-1] * Decimal(mar))
        volumes.append(new_volume)
    return volumes

def calculate_avg_entry(prices, volumes):
    # Переводим цены и объемы в Decimal для точных расчетов
    total_volume = sum(Decimal(v) for v in volumes)
    weighted_sum = sum(Decimal(p) * Decimal(v) for p, v in zip(prices, volumes))
    avg_entry_price = weighted_sum / total_volume
    return round(avg_entry_price, 10)  # Округляем до 10 знаков для точности
