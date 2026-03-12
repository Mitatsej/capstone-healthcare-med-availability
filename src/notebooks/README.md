# Data Pipeline Notebooks

This directory contains the notebooks that implement the **Medallion data pipeline logic**.

Each folder represents a stage of the data processing lifecycle.

## Notebook Structure

00_bronze  
Data ingestion from raw datasets into Delta tables.

01_silver  
Data cleaning, transformation, and standardization.

02_gold  
Creation of analytics-ready tables used for insights and reporting.

15_silver_data_quality  
Data validation checks to ensure the reliability of Silver datasets.

99_pipeline_smoke_test  
Final validation step that confirms the pipeline executed successfully.

## Purpose

These notebooks transform raw healthcare datasets into structured and reliable data that supports analytics on **medication availability across regions**.
