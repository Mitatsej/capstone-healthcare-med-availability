# Databricks notebook source
print("Starting Bronze ingestion workflow")

# COMMAND ----------
dbutils.notebook.run("./00_bronze_ingest", 0)

# COMMAND ----------
print("Bronze ingestion workflow finished")