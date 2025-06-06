import argparse
from src.etl import run_etl
from src.utils import configure_logger

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start-date', required=True)
    parser.add_argument('--end-date', required=True)
    args = parser.parse_args()

    logger = configure_logger()
    run_etl(args.start_date, args.end_date, logger)

if __name__ == '__main__':
    main()