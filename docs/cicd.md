# CI/CD Pipeline

## Overview

The project uses a CI/CD pipeline to automate the deployment and execution of the data pipeline.

CI/CD is implemented using:

- GitHub Actions
- Databricks Asset Bundles
- Databricks CLI

This ensures consistent and automated deployment of the pipeline.

---

## CI/CD Workflow

The CI/CD pipeline follows this process:

Developer Push  
↓  
GitHub Repository  
↓  
GitHub Actions Workflow  
↓  
Databricks Bundle Validation  
↓  
Databricks Deployment  
↓  
Pipeline Execution

---

## Development Workflow

1. Developers create feature branches.
2. Changes are pushed to GitHub.
3. A Pull Request is created.
4. After review, code is merged into the `dev` branch.

The `dev` environment is used for testing pipeline changes.

---

## Production Deployment

When code is pushed to the `main` branch:

1. GitHub Actions is triggered
2. Databricks bundle configuration is validated
3. The pipeline is deployed to Databricks
4. The Medallion pipeline job is executed

This process ensures that the production environment always runs the latest validated pipeline.

---

## CI/CD Components

### GitHub

Used for:

- Source control
- Collaboration
- Branching workflow
- Pull requests

---

### GitHub Actions

Automates:

- Bundle validation
- Deployment to Databricks
- Pipeline execution

Two workflows exist:

- databricks-dev.yml
- databricks-prod.yml

---

### Databricks Asset Bundles

Used to define and deploy pipeline resources including:

- Workflows
- Jobs
- Task dependencies

Bundles ensure infrastructure is version-controlled and reproducible.

---

## Benefits of CI/CD

The CI/CD pipeline provides:

- Automated deployment
- Consistent pipeline execution
- Version-controlled infrastructure
- Reduced manual errors
- Faster development cycles