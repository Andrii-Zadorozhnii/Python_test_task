import pytest
from src.utils import calculate_cpa


def test_cpa_calculation():
    test_data = [
        {"spend": 100, "conversions": 10, "expected": 10.0},
        {"spend": 50, "conversions": 0, "expected": None},
        {"spend": 0, "conversions": 5, "expected": 0.0},
    ]

    for item in test_data:
        data = [{"spend": item["spend"], "conversions": item["conversions"]}]
        result = calculate_cpa(data)[0]
        assert result["cpa"] == item["expected"]
