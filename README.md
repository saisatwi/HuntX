# 🛡️ HuntX – Safety Data Engineering & Incident Analytics Platform
### Status: 🚧 75% Complete | 📊 Dashboard Live | 🤖 AI Safety Agent In-Progress

**HuntX** is a high-performance Data Engineering and Analytics platform designed to process, classify, and visualize large-scale safety incident data. While the current dataset focuses on wildlife safety, the architecture is built to mirror **Global Trust & Safety Operations** used by major platforms (like YouTube/Google) to manage risk, enforce policy, and automate incident escalation.

---

## 🎯 Project Impact (Trust & Safety Focus)
This project solves the "Scale" problem in safety operations:
> "How can we transform thousands of raw, messy incident reports into actionable risk scores that help human moderators prioritize high-harm cases?"

## 🛠️ Technical Ecosystem

### **Data Operations & Engineering**
- **Python (Pandas, NumPy):** Automated ETL pipeline for cleaning 1,000+ raw incident records.
- **Data Integrity:** Implemented schema normalization, null-handling, and de-duplication to ensure "Single Source of Truth."
- **Feature Engineering:** Developed custom logic for `risk_score` and `attack_severity` to automate incident prioritization.

### **Analytics & Intelligence**
- **Power BI:** Interactive Command Center for safety leads to track regional risk heatmaps and severity trends.
- **SQL:** Complex aggregations for trend analysis and warehouse-ready (Snowflake-style) data modeling.

---

## ✔️ Core Deliverables (75% Complete)

### 1. The Safety Data Pipeline (Raw → Transformed)
* **High-Volume Processing:** Standardized inconsistent inputs from multiple sources into a unified safety schema.
* **Quality Enforcement:** Reduced data noise by fixing irregular values and inconsistent casing—mirroring the precision required in YouTube auditing.

### 2. Algorithmic Risk Scoring (Policy Logic)
I engineered specific indicators to simulate **Trust & Safety workflows**:
* `risk_score`: A weighted calculation based on incident impact.
* `is_dangerous`: A boolean flag for immediate escalation (SLA-driven).
* `attack_severity`: Categorical classification to guide policy enforcement.

### 3. Safety Operations Dashboard
* **Regional Heatmaps:** Identifying "High-Harm" geographic zones.
* **KPI Tracking:** Monitoring total incidents, severity distribution, and yearly trends.
* **Stakeholder Insights:** Visuals designed for "Executive Review" to guide safety policy changes.

## 📊 Operational Dashboard Preview
<img width="1366" height="571" alt="HuntX dashboard" src="https://github.com/user-attachments/assets/ac24c9ef-18bf-4ee7-a092-d44db3a787b8" />

---

## 🚧 Roadmap (25% In-Progress)

### 🤖 AI-Assisted Safety Investigator (Upcoming)
Building a multimodal module to allow safety investigators to query the database using natural language:
- **Speech-to-Query:** Using Whisper for voice-activated incident retrieval.
- **LLM Integration:** Llama-based agent to explain "Why" a specific incident was flagged as high-risk.
- **Scalability:** Transitioning the local SQLite database to a **Snowflake Data Warehouse** for enterprise-level performance.

---

## 👨‍💻 Candidate Alignment
This project demonstrates my ability to handle the **technical and operational** demands of a Google Content Specialist:
- **Operations:** Managing high-volume workflows (Ref: Amazon Robotics experience).
- **Data:** Using SQL/Python to find the "needle in the haystack."
- **Policy:** Applying human-in-the-loop logic to train better AI safety models.
