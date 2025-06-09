from src.utils import merge_data, calculate_cpa


def test_merge_data():
    spend = [
        {"date": "2025-06-01", "campaign_id": "C1", "spend": 10},
        {"date": "2025-06-01", "campaign_id": "C2", "spend": 20},
    ]
    conv = [
        {"date": "2025-06-01", "campaign_id": "C1", "conversions": 5},
        {"date": "2025-06-01", "campaign_id": "C3", "conversions": 3},
    ]

    merged = merge_data(spend, conv)
    assert len(merged) == 3

    c1 = next(i for i in merged if i["campaign_id"] == "C1")
    assert c1["spend"] == 10 and c1["conversions"] == 5

    c2 = next(i for i in merged if i["campaign_id"] == "C2")
    assert c2["spend"] == 20 and c2["conversions"] == 0

    c3 = next(i for i in merged if i["campaign_id"] == "C3")
    assert c3["spend"] == 0 and c3["conversions"] == 3


def test_cpa_calculation():
    data = [
        {"spend": 100, "conversions": 10},
        {"spend": 50, "conversions": 0},
        {"spend": 0, "conversions": 5},
    ]

    result = calculate_cpa(data)
    assert result[0]["cpa"] == 10.0
    assert result[1]["cpa"] is None
    assert result[2]["cpa"] == 0.0
