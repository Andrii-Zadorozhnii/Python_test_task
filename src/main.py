import argparse
from .etl import run_etl
from .utils import setup_logger


def main():
    parser = argparse.ArgumentParser(description="CPA Calculation ETL")
    parser.add_argument("--start-date", required=True, help="Start date in ISO format")
    parser.add_argument("--end-date", required=True, help="End date in ISO format")
    parser.add_argument("--data-dir", default="data", help="Data directory")
    args = parser.parse_args()

    logger = setup_logger()
    logger.info(f"Starting CPA calculation from {args.start_date} to {args.end_date}")

    try:
        run_etl(args.start_date, args.end_date, args.data_dir)
    except Exception as e:
        logger.exception("ETL process failed")
        raise


if __name__ == "__main__":
    main()
