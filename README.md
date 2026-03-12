# Healthcare Medication Availability Data Pipeline

## Project Overview

This project builds an end-to-end **Healthcare Data Pipeline** using the **Medallion Architecture (Bronze, Silver, Gold)** on Databricks.

The objective of the project is to integrate multiple healthcare datasets and transform them into analytics-ready data that can support insights about **medication availability across regions**.

Healthcare data often comes from multiple sources and formats. This pipeline standardizes and processes the data in order to support analytics and reporting.

---

# Problem Statement

Healthcare organizations often face challenges understanding **medication availability across regions and pharmacies**.

Data related to diseases, medications, pharmacies, insurance, and geography is typically fragmented and difficult to analyze.

This project addresses this challenge by building a structured data pipeline that:

- integrates multiple healthcare datasets
- cleans and standardizes raw data
- produces analytics-ready tables
- enables insights about medication availability

---

# Architecture

The pipeline follows the **Medallion Architecture**.

Bronze → Raw ingestion layer  
Silver → Cleaned and standardized datasets  
Gold → Business-ready analytics tables
Raw Data
↓
Bronze Layer(Data Ingestion)
↓
Silver Layer(Data Cleaning & Transformation)
↓
Data Quality Checks
↓
Gold Layer(Analytics Tables)

---

# Data Pipeline Layers

## Bronze Layer

The Bronze layer ingests raw datasets into Databricks Delta tables.  
This layer preserves the original data structure and tracks ingestion metadata.

Datasets include:

- diseases
- medications
- pharmacies
- inventory
- insurance
- geography

---

## Silver Layer

The Silver layer performs data transformation and standardization.

Key operations include:

- cleaning raw data
- column standardization
- removing invalid records
- joining datasets for consistency

This layer produces structured and reliable datasets for analytics.

---

## Gold Layer

The Gold layer produces business-level tables used for analytics.

These tables combine multiple Silver datasets to generate insights related to:

- medication availability
- regional distribution of pharmacies
- relationships between diseases and medications

Gold tables are optimized for reporting and analytical use.

---

# Platform Engineering

The platform layer ensures the pipeline can be **automatically deployed and executed**.

Key components include:

- Databricks Workflows for pipeline orchestration
- Databricks Asset Bundles for deployment
- GitHub for source control
- GitHub Actions for CI/CD automation

The CI/CD pipeline validates the bundle configuration, deploys the workflow, and triggers pipeline execution.

---

# Technology Stack

- Databricks
- PySpark
- Delta Lake
- Databricks Workflows
- Databricks Asset Bundles
- GitHub
- GitHub Actions

---

# CI/CD Pipeline

The project includes automated deployment using GitHub Actions.

Pipeline workflow:
Developer Push
↓
GitHub Repository
↓
GitHub Actions
↓
Databricks Bundle Validation
↓
Databricks Deployment
↓
Pipeline Execution

---
# How to Run the Pipeline

The pipeline can be executed using Databricks Asset Bundles.

Example command:

databricks bundle run medallion_pipeline --target dev

# Data Quality

Data quality checks are implemented to ensure reliability of the Silver datasets.

Checks include:

- table existence validation
- empty table detection
- null column validation

If a quality check fails, the pipeline stops before executing the Gold layer.

---

# Contributors

This project was developed as part of a **Data Engineering Capstone Project**.

Team responsibilities included:

- Platform Engineering (CI/CD, workflow orchestration)
- Data pipeline development
- Analytics development
# Data Sources

The pipeline processes several healthcare-related datasets including:

- Diseases dataset
- Medications dataset
- Pharmacies dataset
- Inventory dataset
- Insurance dataset
- Geographic information dataset

These datasets are ingested in the Bronze layer and transformed through the Medallion pipeline.
