import shutil
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window


def _build_spark() -> SparkSession:
    return (
        SparkSession.builder.master("local[*]")
        .appName("CryptoETL")
        .config("spark.sql.session.timeZone", "UTC")
        .getOrCreate()
    )


def run_etl(
    history_input_path: str = "data/crypto_prices_history.csv",
    latest_input_path: str = "data/crypto_prices.csv",
    trends_output_path: str = "output/trends_report.csv",
    latest_output_path: str = "output/latest_trends.csv",
) -> None:
    spark = _build_spark()
    try:
        source_path = Path(history_input_path)
        if not source_path.exists():
            fallback_path = Path(latest_input_path)
            if not fallback_path.exists():
                raise FileNotFoundError(f"Expected input file not found: {source_path}")
            source_path = fallback_path

        raw_df = spark.read.csv(str(source_path), header=True, inferSchema=True)
        if "snapshot_date" in raw_df.columns:
            dated_df = raw_df.withColumn("snapshot_date", F.to_date("snapshot_date"))
        elif "fetched_at" in raw_df.columns:
            dated_df = raw_df.withColumn("snapshot_date", F.to_date("fetched_at"))
        else:
            raise ValueError("Input data must include either snapshot_date or fetched_at")

        df = (
            dated_df.withColumn("current_price", F.col("current_price").cast("double"))
            .withColumn("market_cap", F.col("market_cap").cast("double"))
            .withColumn("market_cap_rank", F.col("market_cap_rank").cast("int"))
            .withColumn("total_volume", F.col("total_volume").cast("double"))
        )

        coin_window = Window.partitionBy("id").orderBy("snapshot_date")
        trend_df = (
            df.withColumn("previous_price", F.lag("current_price").over(coin_window))
            .withColumn("previous_market_cap", F.lag("market_cap").over(coin_window))
            .withColumn(
                "daily_price_change_pct",
                F.round(
                    ((F.col("current_price") - F.col("previous_price")) / F.col("previous_price")) * 100,
                    2,
                ),
            )
            .withColumn(
                "daily_market_cap_change_pct",
                F.round(
                    ((F.col("market_cap") - F.col("previous_market_cap")) / F.col("previous_market_cap")) * 100,
                    2,
                ),
            )
            .withColumn(
                "trend_label",
                F.when(F.col("daily_price_change_pct") > 1, F.lit("Bullish"))
                .when(F.col("daily_price_change_pct") < -1, F.lit("Bearish"))
                .otherwise(F.lit("Sideways")),
            )
            .drop("previous_price", "previous_market_cap")
        )

        ordered_df = trend_df.orderBy("snapshot_date", "market_cap_rank")
        latest_date = ordered_df.select(F.max("snapshot_date").alias("max_date")).collect()[0]["max_date"]
        latest_df = ordered_df.filter(F.col("snapshot_date") == F.lit(latest_date))

        trends_path = Path(trends_output_path)
        latest_path = Path(latest_output_path)

        if trends_path.exists() and trends_path.is_dir():
            shutil.rmtree(trends_path)
        if latest_path.exists() and latest_path.is_dir():
            shutil.rmtree(latest_path)

        output_dir = trends_path.parent
        output_dir.mkdir(parents=True, exist_ok=True)

        ordered_df.toPandas().to_csv(trends_path, index=False)
        latest_df.orderBy("market_cap_rank").toPandas().to_csv(latest_path, index=False)
    finally:
        spark.stop()


if __name__ == "__main__":
    run_etl()


