import pytest # type: ignore
from app.helpers import calculate_order_volumes, calculate_avg_entry

def test_calculate_order_volumes():
    vol1 = 100
    mar = 0.3
    num_orders = 3
    volumes = calculate_order_volumes(vol1, mar, num_orders)
    assert volumes == [100, 130, 169]

def test_calculate_avg_entry():
    prices = [50, 49, 48]
    volumes = [100, 130, 169]
    avg_entry = calculate_avg_entry(prices, volumes)
    assert round(avg_entry, 2) == 48.42
