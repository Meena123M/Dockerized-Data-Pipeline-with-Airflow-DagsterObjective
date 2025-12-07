# 🚀 Dockerized Data Pipeline with Airflow/Dagster  
### 📊 Automated Stock Market Data Ingestion (End-to-End Project)

This project is a fully **Dockerized, end-to-end data pipeline** built entirely from scratch. It automates the process of fetching stock market data from the **Alpha Vantage API**, processing the JSON response, and storing it into a **PostgreSQL** database—scheduled and orchestrated using **Apache Airflow** (or Dagster).

---

## 📌 **Project Highlights**

### 🛠️ 1. Complete Environment Setup  
- Installed and configured **Ubuntu**, **WSL**, and **Python virtual environments**  
- Set up project structure and all development dependencies

---

### 🌐 2. Data Ingestion from Alpha Vantage  
- Fetched real-time stock market data using the Alpha Vantage API  
- Parsed and validated **JSON** responses  
- Implemented clean Python scripts for fetching and transforming stock data

---

### 🗄️ 3. Database Integration (PostgreSQL)  
- Designed database schema for storing OHLCV stock data  
- Inserted data using **psycopg2**  
- Ensured reliable connection handling, commits, and error management

---

### 🐳 4. Containerization with Docker  
Created a full **Docker Compose** setup containing:  
- 🟦 **PostgreSQL** (Database)  
- 🟧 **Apache Airflow** (Webserver, Scheduler, Worker)  
- 🧰 Supporting services and initialization scripts  

This makes the pipeline **reproducible, portable, and production-ready**.

---

### 📅 5. Workflow Orchestration with Airflow  
- Built custom **Airflow DAGs** to automate data ingestion every few minutes  
- Implemented tasks for API call → processing → DB insertion  
- Verified DAG runs through the **Airflow UI**  
- Added logging, retries, and modular task design

---

### 🧪 6. End-to-End Testing  
- Successfully connected Airflow with PostgreSQL inside Docker  
- Triggered DAGs manually and via schedule  
- Validated end-to-end data flow from API → DAG → Database

---

## 🧱 **Tech Stack**

| Component | Technology |
|----------|------------|
| Language | Python |
| Orchestration | Apache Airflow / Dagster |
| Database | PostgreSQL |
| API | Alpha Vantage |
| Libraries | `requests`, `json`, `psycopg2`, `pandas` |
| Deployment | Docker & Docker Compose |
| OS | Ubuntu / WSL |

---



