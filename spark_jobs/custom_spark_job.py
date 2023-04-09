import os
from pyspark.sql import SparkSession

# read the environment variable for the header parameter
header = os.environ.get("HEADER")

# create a SparkSession
spark = SparkSession.builder \
    .appName("CSV to Delta Lake") \
    .getOrCreate()

# read a CSV file into a DataFrame
df = spark.read \
    .option("header", header) \
    .option("inferSchema", "true") \
    .csv("file:///path/to/csv/file.csv")

# write the DataFrame to a Delta Lake table
df.write \
    .format("delta") \
    .mode("overwrite") \
    .save("/path/to/delta/lake/table")

# stop the SparkSession
spark.stop()