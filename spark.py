from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Test").getOrCreate()

df = spark.read.csv("results.csv", header=True, inferSchema=True)

print(df.show())
