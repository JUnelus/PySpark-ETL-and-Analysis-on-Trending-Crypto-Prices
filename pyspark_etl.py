import os

os.environ["HADOOP_HOME"] = "C:/hadoop"
os.environ["JAVA_HOME"] = "C:/Program Files/Java/jdk-21"  # or wherever your JDK is

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lag, round as pyspark_round
from pyspark.sql.window import Window

spark = SparkSession.builder.appName("CryptoETL").getOrCreate()

# Load
df = spark.read.csv('data/crypto_prices.csv', header=True, inferSchema=True)

# Transform: calculate % price change
window = Window.orderBy("market_cap_rank")
df = df.withColumn("price_change_pct",
                   pyspark_round(((col("current_price") - lag("current_price", 1).over(window)) / lag("current_price", 1).over(window)) * 100, 2))

df = df.dropna() # Remove rows with NA from lag

# Save cleaned/trended data
df.write.csv('output/trends_report.csv', header=True, mode='overwrite')
spark.stop()
