from pyspark.conf import SparkConf
from pyspark.sql import SparkSession


# create a SparkSession
spark = SparkSession.builder \
    .appName("CSV to Delta Lake") \
    .getOrCreate()

print(spark.range(1000 * 1000 * 1000).count())

spark.stop()