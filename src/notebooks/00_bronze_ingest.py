# ========================================
# Configuration
# ========================================

bronze_db = "bronze"
silver_db = "silver"
gold_db = "gold"

# ========================================
# Create Databases (Schemas)
# ========================================

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {bronze_db}")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {silver_db}")
spark.sql(f"CREATE SCHEMA IF NOT EXISTS {gold_db}")

disease1 = "src/diseases/ICD10codes.csv"
disease2 = "src/diseases/U.S._Chronic_Disease_Indicators_20260223.csv"
disease3 = "src/diseases/drug-label-0013-of-0013.json"
disease4 = "src/diseases/icd9to10dictionary.txt"
geography1 = "src/geography/ACSDT5Y2023.B01003-Column-Metadata.csv"
geography2 = "src/geography/ACSDT5Y2023.B01003-Data.csv"
insurance1 = "src/Insurance/benefits-and-cost-sharing-puf.csv"
insurance2 = "src/Insurance/plan-attributes-puf.csv"
inventory = "src/inventory/1-inventory-data.js"
medication1 = "src/medications/DrugReviews.csv"
medication2 = "src/medications/package.txt"
medication3 = "src/medications/exclusivity.txt"
medication4 = "src/medications/patent.txt"
medication5 = "src/medications/product.txt"
medication6 = "src/medications/products.txt"
pharmacies = "src/pharmacies/Pharmacies.csv"


# ==========================================
# Helper Function
# ==========================================

def load_csv_to_bronze(path, table_name):
    df = (
        spark.read
            .option("header", True)
            .option("inferSchema", False)  # keep raw in Bronze
            .csv(path)
    )
    
    df.write.mode("overwrite").saveAsTable(f"bronze.{table_name}")
    print(f"Loaded {path} → bronze.{table_name}")


def load_json_to_bronze(path, table_name):
    df = spark.read.json(path)
    
    df.write.mode("overwrite").saveAsTable(f"bronze.{table_name}")
    print(f"Loaded {path} → bronze.{table_name}")

# ==========================================
# Load CSV Files
# ==========================================

load_csv_to_bronze(disease1, "diseases_icd10_raw")
load_csv_to_bronze(disease2, "diseases_chronic_indicators_raw")
load_csv_to_bronze(disease4, "icd9to10dictionary_raw")

load_csv_to_bronze(geography1, "geography_metadata_raw")
load_csv_to_bronze(geography2, "geography_population_raw")

load_csv_to_bronze(insurance1, "insurance_benefits_raw")
load_csv_to_bronze(insurance2, "insurance_plan_attributes_raw")

load_csv_to_bronze(medication1, "medication_reviews_raw")

load_csv_to_bronze(pharmacies, "pharmacies_raw")

# ==========================================
# Load JSON Files
# ==========================================

load_json_to_bronze(disease3, "diseases_drug_label_raw")

# ==========================================
# Load JS Files
# ==========================================

# Read raw file as text
raw_text_df = spark.read.text(inventory)

# Collect file into a single string
file_content = "\n".join(row.value for row in raw_text_df.collect())

# Extract JSON array between [ and ]
json_array = re.search(r'\[.*\]', file_content, re.DOTALL).group()

# Convert JSON string into Spark DataFrame
rdd = spark.sparkContext.parallelize([json_array])
df = spark.read.json(rdd)

# Write to Bronze (clean table name)
df.write.mode("overwrite").saveAsTable("bronze.inventory-data")

# ==========================================
# Load txt files
# ==========================================

df = (
    spark.read
        .option("header", True)        # first row contains column names
        .option("delimiter", "~")      # tilde separator
        .option("inferSchema", False)  # keep raw in Bronze
        .csv(medication3)
)

# Write to Bronze (keeping original filename as table name)
df.write.mode("overwrite").saveAsTable("bronze.exclusivity")

