from .utils import load_json, filter_by_date, merge_data, calculate_cpa
from .database import init_db, upsert_data
import logging

logger = logging.getLogger(__name__)


def run_etl(start_date, end_date, data_dir="data"):
    logger.info(f"Starting ETL for {start_date} to {end_date}")

    # Load data
    spend_data = load_json(f"{data_dir}/fb_spend.json")
    conv_data = load_json(f"{data_dir}/network_conv.json")

    # Filter data
    filtered_spend = filter_by_date(spend_data, start_date, end_date)
    filtered_conv = filter_by_date(conv_data, start_date, end_date)

    # Merge data
    merged_data = merge_data(filtered_spend, filtered_conv)

    # Calculate CPA
    result_data = calculate_cpa(merged_data)

    # Initialize DB
    init_db()

    # Upsert data
    upsert_data(result_data)

    # Print summary
    logger.info(f"Processed {len(result_data)} records")
    print(f"ETL Summary ({start_date} to {end_date}):")
    print(f"- {len(result_data)} records processed")
    print(f"- {len(filtered_spend)} spend records")
    print(f"- {len(filtered_conv)} conversion records")

    return result_data
