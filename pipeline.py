from __future__ import annotations

import argparse

from analysis.exploratory_analysis import generate_daily_analysis
from fetch_crypto_data import fetch_top_crypto
from pyspark_etl import run_etl
from update_readme import update_readme


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the crypto ETL + analysis pipeline")
    parser.add_argument(
        "--skip-fetch",
        action="store_true",
        help="Skip the API call and use existing files in data/",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if not args.skip_fetch:
        print("[1/4] Fetching latest crypto data...")
        fetch_top_crypto()
    else:
        print("[1/4] Skipping fetch step (--skip-fetch)")

    print("[2/4] Running PySpark ETL...")
    run_etl()

    print("[3/4] Generating charts and daily trend analysis...")
    generate_daily_analysis()

    print("[4/4] Updating README with latest results...")
    update_readme()

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()

