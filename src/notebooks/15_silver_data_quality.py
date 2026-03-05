# Databricks notebook source
# This notebook runs basic data-quality checks on key Silver tables.
# Fill in the actual table names for your environment before using it in CI.

from pyspark.sql import functions as F

# List your important Silver tables here once they exist.
# Example (replace with your real catalog/schema/table names):
#   "main.silver.geography_base",
#   "main.silver.location_county",
#   "main.silver.pharmacies",
#   "main.silver.medication",
#   "main.silver.population",
silver_tables = [
    # TODO: add fully-qualified Silver table names here
]


def table_exists(table_name: str) -> bool:
    try:
        spark.table(table_name)
        return True
    except Exception:
        return False


def check_non_empty(df, table_name: str):
    row_count = df.count()
    if row_count == 0:
        raise AssertionError(f"Silver table '{table_name}' is empty.")


def check_no_all_null_columns(df, table_name: str):
    null_only_cols = []
    for col in df.columns:
        non_null_count = df.filter(F.col(col).isNotNull()).limit(1).count()
        if non_null_count == 0:
            null_only_cols.append(col)
    if null_only_cols:
        raise AssertionError(
            f"Silver table '{table_name}' has columns that are entirely NULL: {null_only_cols}"
        )


failed_tables = []
skipped_tables = []

for tbl in silver_tables:
    if not table_exists(tbl):
        skipped_tables.append(tbl)
        print(f"[SKIP] Silver table does not exist (yet): {tbl}")
        continue

    print(f"[CHECK] Silver table: {tbl}")
    df = spark.table(tbl)

    try:
        check_non_empty(df, tbl)
        check_no_all_null_columns(df, tbl)
        print(f"[OK] Silver table passed checks: {tbl}")
    except AssertionError as e:
        failed_tables.append((tbl, str(e)))
        print(f"[FAIL] {e}")

if failed_tables:
    messages = [f"{tbl}: {msg}" for tbl, msg in failed_tables]
    raise AssertionError(
        "One or more Silver tables failed data-quality checks:\n" + "\n".join(messages)
    )

print("[RESULT] Silver data-quality checks completed.")
if skipped_tables:
    print(f"[INFO] Skipped tables (not found): {skipped_tables}")

