from pyspark.sql.functions import col

# Read sample dataset
df = spark.read.csv("datasets/sample_customer_data.csv", header=True)

# Null value check
null_email_df = df.filter(col("email").isNull())

# Duplicate record check
duplicate_df = df.groupBy("customer_id").count().filter(col("count") > 1)

print("Null email records count:", null_email_df.count())
print("Duplicate customer records count:", duplicate_df.count())
