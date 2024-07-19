from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

spark = SparkSession.builder.appName("ProductsCategories").getOrCreate()

products_data = [
    ("Product1", 1),
    ("Product2", 2),
    ("Product3", None),
    ("Product4", 1),
    ("Product5", None)
]

categories_data = [
    (1, "Category1"),
    (2, "Category2"),
    (3, "Category3")
]

products_df = spark.createDataFrame(products_data, ["ProductName", "CategoryId"])
categories_df = spark.createDataFrame(categories_data, ["CategoryId", "CategoryName"])

product_category_df = products_df.join(categories_df, products_df.CategoryId == categories_df.CategoryId, "left_outer")\
    .select("ProductName", "CategoryName")

products_without_categories_df = products_df.filter(col("CategoryId").isNull()).select("ProductName")

product_category_df.show()
products_without_categories_df.show()

spark.stop()