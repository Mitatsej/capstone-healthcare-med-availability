# Databricks Jobs Configuration

This directory contains the configuration for the **Medallion pipeline workflow** executed in Databricks.

The pipeline is orchestrated using **Databricks Workflows** and deployed using **Databricks Asset Bundles**.

## Workflow Overview

The Medallion pipeline follows this execution order:

Bronze Ingestion  
↓  
Silver Transformations  
↓  
Data Quality Validation  
↓  
Gold Publishing  
↓  
Pipeline Smoke Test

## Key Responsibilities

- Define the workflow orchestration for the pipeline
- Configure task dependencies between pipeline layers
- Ensure reliable execution using retries and timeouts
- Enable automated deployment via CI/CD

The workflow configuration is deployed automatically through **GitHub Actions** and executed in the Databricks workspace.
