# 🦊 HuntX – Wildlife Safety Data Engineering Project  
### Status: 🚧 75% Complete | 📊 Dashboard Ready | 🤖 AI Module In Progress

HuntX is an **end-to-end Data Engineering & Analytics project** built to analyze wildlife attack data, generate risk insights, and prepare a foundation for an AI-powered voice/semantic search agent.

This project demonstrates:
- Data engineering pipeline (Raw → Processed → Transformed)
- Automated data cleaning & validation
- Feature engineering (risk scoring, attack categories, severity levels)
- BI dashboard for insights
- Future integration of multimodal AI interaction


## 📌 Project Overview

HuntX solves a real-world use case:

> “How can wildlife attack data be analyzed, cleaned, transformed, and visualized to help track, predict, and reduce risk?”

## 🛠️ Tech Stack

### **Data Engineering**
- Python (Pandas, NumPy)
- ETL workflows (cleaning → transformation → loading)
- Feature engineering
- Data quality validation

### **Storage / Warehouse**
- SQLite (current)
- Snowflake-ready structure (planned)

### **Analytics & Visualization**
- Power BI Dashboard  
- KPI cards, risk charts, location heatmaps



---

## ✔️ Completed (75%)

### **1. ETL Pipeline (Raw → Processed → Transformed)**
- Removed duplicates across 1,000+ rows  
- Fixed nulls, irregular values, inconsistent casing  
- Standardized species name formats  
- Created structured schema

### **2. Feature Engineering**
Added derived columns:
- `risk_score`
- `is_dangerous`
- `region_category`
- `attack_severity`

### **3. Power BI Dashboard**
Dashboard includes:
- Total attacks by region
- Severity-level heatmap
- Species-wise risk score
- Yearly trends
- Insights for policymakers / wildlife departments

## 📊 HuntX Dashboard
<img width="1366" height="571" alt="HuntX dashboard" src="https://github.com/user-attachments/assets/ac24c9ef-18bf-4ee7-a092-d44db3a787b8" />



## 🚧 In Progress (25%)

### **4. AI Voice Search Engine (Planned)**
To be implemented:
- Whisper voice input  
- Llama-based natural language query  
- Querying transformed dataset  
- Responding with voice/text insights  
- Running offline (inspired by MyDataWhisperer)

## 🔜 Upcoming Enhancements
- Add Snowflake warehouse version  
- Add pipeline orchestration (Prefect / Airflow)  
- Add interactive Streamlit app  
- Expand dashboard with predictive analytics 
