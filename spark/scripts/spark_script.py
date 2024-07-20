from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
	.appName("Local Spark Testing") \
	.getOrCreate()

# Load Dataset
df = spark.read.csv("file:///home/sowrabh/Desktop/Project_works/Data_Processing/spark/data/taxi_tripdata.csv", header=True,  inferSchema=True)

# Data Cleaning and Transformation
df_cleaned = df.dropna().filter(col("payment_type") != "unwanted_value")

# Data aggregation
df_aggregated = df_cleaned.groupBy("payment_type").agg({"fare_amount" : "sum"})

# Show results
df_aggregated.show()

spark.stop()
