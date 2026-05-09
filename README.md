# 💲 Personal Expense Tracker with Data Visualization

## 📌 Project Overview
The Personal Expense Tracker is a Python-based data analytics project that helps users record, analyze, and visualize their daily expenses. It provides insights into spending patterns using charts and summary reports generated from structured data.

This project demonstrates skills in **Python programming, data analysis, data visualization, and dashboard development**.

---

## 🎯 Problem Statement
People often lose track of their daily expenses, leading to poor budgeting and financial imbalance. This project solves that problem by providing a structured system to:

- Track expenses
- Categorize spending
- Analyze financial behavior
- Visualize spending patterns
- Generate summary reports

---

## ⚙️ Features

- Add and manage expense data (CSV-based)
- Automatic data cleaning and formatting
- Category-wise expense analysis
- Monthly spending trends
- Payment method breakdown
- Interactive visual dashboards
- Summary report generation
- Clean and modern UI dashboard

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit
- CSV (Data Storage)

---

## 📁 Project Structure

```
Personal-Expense-Tracker-With-Data-Visualization/
│
├── data/
│   └── expenses.csv                  # Raw / synthetic expense dataset
│
├── notebooks/
│   ├── expense_analysis.ipynb       # Main EDA notebook
│   └── setup_notebook.py            # Auto notebook generator script
│
├── src/
│   ├── data_loader.py               # Load CSV data
│   ├── cleaner.py                   # Data cleaning logic
│   ├── analysis.py                  # Category, monthly, payment analysis
│   └── report_generator.py         # Summary report creation
│
├── images/
│   ├── category_chart.png           # Bar chart output
│   ├── monthly_trend.png           # Line chart output
│   └── payment_chart.png           # Pie chart output
│
├── outputs/
│   └── expense_summary.txt          # Final text summary report
│
├── reports/
│   └── final_report.csv            # Structured analysis output
│
├── app.py                          # Streamlit dashboard UI
├── main.py                         # Backend execution script
│
├── requirements.txt                # Project dependencies
├── .gitignore                      # Ignore venv/cache files
└── README.md                       # Project documentation
```

---

## 🚀 How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run backend script
```bash
python main.py
```

### 3️⃣ Run dashboard UI
```bash
streamlit run app.py
```

---

## 📊 Visualizations Included

- 📊 Category-wise Spending (Bar Chart)
- 📈 Monthly Spending Trend (Line Chart)
- 🥧 Payment Method Distribution (Pie Chart)
- 📋 Transaction Data Table

---

## 📌 Sample Insights Generated

- Highest spending category
- Monthly spending pattern
- Average daily expense
- Payment method usage distribution

---

## 🧠 Learning Outcomes

- Data preprocessing using Pandas
- Data visualization using Matplotlib
- Dashboard creation using Streamlit
- Modular Python project structure
- Real-world financial data analysis

---



## 📈 Future Improvements

- Budget limit alerts
- Login system for users
- Database integration (SQLite/MySQL)
- AI-based expense categorization
- Export reports as PDF
- Mobile-friendly dashboard

---

## 👨‍💻 Author

**Personal Project (Student Level)**  
Built for learning Data Analysis + Python Development + Dashboard Design

---

## ⭐ Outcome

This project demonstrates real-world skills in:
- Data Analytics
- Financial Tracking Systems
- Python Automation
- Interactive Dashboard Development
```