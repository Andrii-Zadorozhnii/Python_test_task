import logger


def run_etl(start_date, end_date, logger):
    try:
        spend_data = load_json("data/fb_spend.json")
        conv_data = load_json("data/network_conv.json")

        filtered_spend = filter_by_date(spend_data, start_date, end_date)
        filtered_conv = filter_by_date(conv_data, start_date, end_date)

        merged_data = merge_datasets(filtered_spend, filtered_conv)

        calculated_data = calculate_cpa(merged_data)

        with Database() as db:
            db.upsert_data(calculated_data)

        logger.error(f"Processed {len(calculated_data)} records")

    except Exception as e:
        logger.exception(f"ETL process failed: {e}")
        raise
