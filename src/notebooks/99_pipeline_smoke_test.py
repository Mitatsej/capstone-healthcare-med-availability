# Databricks notebook source
# Simple pipeline smoke test for Medallion pipeline.
# This is intended to be run as a Databricks Job task after the main pipeline.

from pyspark.sql import functions as F

# Fill in the key Bronze and Silver tables your pipeline creates.
# Use fully-qualified names where possible (catalog.schema.table).

bronze_tables = [
    # TODO: add key Bronze tables, e.g. "main.bronze.raw_inventory"
]

silver_tables = [
    # TODO: add key Silver tables, e.g. "main.silver.geography_base"
]


def table_exists(table_name: str) -> bool:
    try:
        spark.table(table_name)
        return True
    except Exception:
        return False


def basic_smoke_check(table_name: str):
    if not table_exists(table_name):
        raise AssertionError(f"Expected table '{table_name}' does not exist.")

    df = spark.table(table_name)
    row_count = df.limit(1).count()
    if row_count == 0:
        raise AssertionError(f"Table '{table_name}' exists but appears to be empty.")


failed = []
categories = [("bronze", bronze_tables), ("silver", silver_tables)]

for layer_name, tables in categories:
    for tbl in tables:
        print(f"[SMOKE] Checking {layer_name} table: {tbl}")
        try:
            basic_smoke_check(tbl)
            print(f"[OK] {layer_name} table passed smoke test: {tbl}")
        except AssertionError as e:
            print(f"[FAIL] {e}")
            failed.append(str(e))

if failed:
    raise AssertionError(
        "Pipeline smoke test failed for one or more tables:\n" + "\n".join(failed)
    )

print("[RESULT] Pipeline smoke test completed successfully.")

