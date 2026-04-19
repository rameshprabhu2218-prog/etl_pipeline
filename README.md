# 🚀 ETL Pipeline with Python & SQLite

A beginner-friendly ETL (Extract, Transform, Load) pipeline that processes CSV sales data, cleans it, and loads it into a SQLite database.

## 📌 What This Project Does
- **Extracts** raw sales data from a CSV file
- **Transforms** it (removes duplicates, handles nulls, formats dates, calculates revenue)
- **Loads** clean data into a SQLite database
- Generates a simple summary report

## 🛠️ Tech Stack
- Python 3.x
- Pandas
- SQLite3
- Logging

## 📁 Project Structure
```
project1_etl_pipeline/
│
├── data/
│   └── raw_sales.csv        # Sample raw input data
├── etl_pipeline.py          # Main ETL script
├── generate_data.py         # Script to generate sample data
├── requirements.txt
└── README.md
```

## ▶️ How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Generate sample data
python generate_data.py

# Run the ETL pipeline
python etl_pipeline.py
```

## 📊 Output
- `sales.db` — SQLite database with clean data
- Console logs showing each ETL step
- Summary report printed to terminal

## 💡 Key Concepts Demonstrated
- ETL pipeline design
- Data cleaning with Pandas
- SQL database operations
- Python logging best practices
- Error handling
