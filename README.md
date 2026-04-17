# Crypto Data Pipeline

A production-style ETL pipeline designed to collect real-time Bitcoin market data, enrich it with live currency exchange rates, apply incremental loading logic for new records only, transform it into analytics-ready format, and store it in SQL Server for reporting and dashboarding.

---

## 🚀 Project Highlights

* Collects live Bitcoin price data using the CoinGecko API
* Integrates real-time USD → INR conversion rates
* Calculates Bitcoin price in INR dynamically
* Tracks market movement with price change metrics
* Uses CSV as a staging layer for raw data storage
* Cleans, standardizes, and transforms data with Pandas
* Loads final structured data into SQL Server
* Supports incremental loading using timestamp-based logic
* Ready for Power BI dashboards

---

## 🏗️ Architecture

CoinGecko API + FX API → CSV Staging Layer → Python (Pandas Processing) → SQL Server

---

## 📂 Repository Structure

```bash
Crypto_Pipeline/
│── Data/
│   ├── Setup.py
│   └── Staging_File.csv
│
│── src/
│   ├── Extract.py
│   ├── Transform.py
│   └── Load.py
│
│── Main_Pipeline.py
│── config.py
│── .env
│── .gitignore
│── README.md
```

---

## 🔄 ETL Workflow

### 1️⃣ Extract Layer

* Pulls real-time Bitcoin market data
* Fetches latest USD/INR exchange rate
* Saves raw records into staging CSV

### 2️⃣ Transform Layer

* Converts timestamps and numeric datatypes
* Removes duplicates
* Creates derived metrics:

  * Price Change (USD)
  * Price in INR
  * Price Change in INR
* Applies incremental logic using latest database timestamp

### 3️⃣ Load Layer

* Pushes transformed records into SQL Server final table
* Appends only new records

---

## 📊 Final Dataset Columns

* id
* symbol
* default_currency
* current_price_usd
* current_price_inr
* market_cap
* high_24h
* low_24h
* price_change_usd
* price_change_inr
* last_updated

---

## ▶️ Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run pipeline
python Main_Pipeline.py

#Server details
Update Your Server Details in config.py file
```

---

## 🛠️ Tech Stack

* Python
* Pandas
* SQLAlchemy
* SQL Server
* REST APIs
* CSV
* Git & GitHub

---

## 📌 Future Enhancements

* Airflow scheduling
* Azure Blob Storage staging layer
* Docker deployment
* Real-time dashboard automation
