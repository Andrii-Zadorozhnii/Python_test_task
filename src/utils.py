import json
import logging
import os
from datetime import datetime


def setup_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    return logging.getLogger(__name__)


def load_json(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logger = logging.getLogger(__name__)
        logger.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in file: {file_path}")
        raise


def filter_by_date(data, start_date, end_date):
    return [d for d in data if start_date <= d["date"] <= end_date]


def merge_data(spend_data, conv_data):
    merged = {}
    for item in spend_data:
        key = (item["date"], item["campaign_id"])
        merged.setdefault(
            key,
            {
                "date": item["date"],
                "campaign_id": item["campaign_id"],
                "spend": 0.0,
                "conversions": 0,
            },
        )["spend"] = item["spend"]

    for item in conv_data:
        key = (item["date"], item["campaign_id"])
        merged.setdefault(
            key,
            {
                "date": item["date"],
                "campaign_id": item["campaign_id"],
                "spend": 0.0,
                "conversions": 0,
            },
        )["conversions"] = item["conversions"]

    return list(merged.values())


def calculate_cpa(data):
    for record in data:
        if record["conversions"] == 0:
            record["cpa"] = None
        else:
            record["cpa"] = record["spend"] / record["conversions"]
    return data
