This document explains how team members should contribute to the project.
 
## 1. Source of Truth
 
GitHub is the official source of the project.  
Code is not considered part of the project until it is pushed to the repository.
 
---
 
## 2. Workflow
 
1. Clone the repository
2. Create a feature branch
3. Implement your changes
4. Push to GitHub
5. Open a Pull Request to the `dev` branch
 
---
 
## 3. Branch Naming Convention
 
Use descriptive branch names:
 
feature/<task-name>
fix/<issue-name>
docs/<documentation-name>
 
Examples:
feature/bronze-ingestion
feature/dashboard-analysis
docs/update-readme
 
---
 
## 4. Do NOT work directly on main
 
- main = final stable version (demo ready)
- dev = integration branch
- feature branches = individual work
 
---
 
## 5. Pull Requests
 
Every change must go through a Pull Request.
 
Requirements:
- Code compiles / runs
- Clear description of changes
- Linked issue (if applicable)
 
---
 
## 6. Working with Databricks
 
- Each member may use their own Databricks Community account for testing
- No shared workspace is required
- Final deployment will be handled by Platform Engineering
 
---
 
## 7. Folder Structure
 
Place files in the appropriate folders:
 
src/notebooks/bronze/     → raw ingestion
src/notebooks/silver/     → cleaned data
src/notebooks/gold/       → curated data
src/notebooks/analytics/  → analysis & insights
 
---
 
## 8. Communication
 
If unsure where something belongs, ask in the team channel before pushing.