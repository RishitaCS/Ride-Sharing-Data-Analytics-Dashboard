# 🚖 Ride-Sharing Data Analytics Dashboard

An end-to-end data analytics project that analyzes ride-sharing trip data to uncover trends in demand, pricing, wait times, and customer experience.  
The project integrates **SQL, Python, and Streamlit** to provide interactive dashboards and automated reporting.

---

## 📊 Features

- **Data Cleaning & Preparation**  
  - Raw CSV ➝ SQLite database & Parquet format  
  - Time parsing, null handling, and data validation  

- **SQL Analytics**  
  - KPIs: total rides, cancellations, peak hours, average fare  
  - Query execution with SQLite  

- **Exploratory Data Analysis (EDA)**  
  - Distribution of distance, fare, and wait time 
  - Peak hours analysis
  - Trip distance vs. price correlations  
  - City analysis 

- **Automated Reports**  
  - Weekly Excel reports generated with `openpyxl`  

- **Interactive Dashboard**  
  - Built with **Streamlit**  
  - Filter by city, date range  
  - Visualizations: Rides by Hour  

---

## 🛠️ Tech Stack

- **Python**: Pandas, Matplotlib, Seaborn, SQLite3, OpenPyXL  
- **SQL**: SQLite database for querying KPIs  
- **Visualization**: Streamlit, Seaborn, Matplotlib  
- **Automation**: Weekly report generator  

---

## 📂 Project Structure

```
Ride-Sharing-Data-Analytics-Dashboard/
│
├── data/
│   ├── raw/                 # Raw dataset (CSV)
│   ├── cleaned_trips.parquet # Cleaned dataset (generated)
│   └── rides.db             # SQLite database (generated)
│
├── notebooks/
│   └── eda.ipynb            # Exploratory Data Analysis
│
├── reports/
│   └── weekly_report_*.xlsx # Auto-generated weekly reports
│
├── app.py                   # Streamlit dashboard
├── prepare_data.py           # Cleans raw CSV → DB + Parquet
├── run_sql.py                # Run sample SQL queries
├── generate_weekly_report.py # Automated report generator
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## ⚡ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/Ride-Sharing-Data-Analytics-Dashboard.git
cd Ride-Sharing-Data-Analytics-Dashboard
```

### 2️⃣ Setup Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Prepare the Data

Place your **raw dataset** inside `data/raw/` and run:

```bash
python prepare_data.py
```

This will generate:
- `data/cleaned_trips.parquet`  
- `data/rides.db`  

### 5️⃣ Run Exploratory Analysis

Open Jupyter or VS Code Notebook:

```bash
jupyter notebook notebooks/eda.ipynb
```

### 6️⃣ Launch Streamlit Dashboard

```bash
streamlit run app.py
```

---

## 📈 Sample SQL Queries

```sql
-- Total rides
SELECT COUNT(*) FROM trips;

-- Peak ride hours
SELECT strftime('%H', trip_start_time) AS hour, COUNT(*) 
FROM trips 
GROUP BY hour ORDER BY rides DESC;
```

Run with:

```bash
python run_sql.py
```

---

## 📑 Automated Weekly Reports

```bash
python generate_weekly_report.py
```

This generates Excel reports under `/reports/`.

---

## 🌍 Live App

🚀 Deployed on Streamlit Cloud:  
👉 [Ride-Sharing Analytics Dashboard](https://ride-sharing-data-analytics-dashboard-kiehol4ppl43dwimgay5kb.streamlit.app/)

---
