# ========================================
# Configuration
# ========================================

bronze_db = "bronze"
silver_db = "silver"
gold_db = "gold"
volume_path = "/FileStore/raw_sources" 

# ========================================
# Create Databases (Schemas)
# ========================================

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {bronze_db}")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {silver_db}")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {gold_db}")

# ========================================
# Create a folder to store source files in DBFS
# ========================================

dbutils.fs.mkdirs(volume_path)

