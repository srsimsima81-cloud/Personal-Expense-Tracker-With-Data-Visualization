from src.data_loader import load_data
from src.cleaner import clean_data
from src.analysis import category_analysis, monthly_analysis, payment_analysis, daily_analysis
from src.visualization import plot_category, plot_monthly, plot_payment
from src.report_generator import generate_summary

# Load
df = load_data("data/expenses.csv")

# Clean
df = clean_data(df)

# Analysis
cat = category_analysis(df)
month = monthly_analysis(df)
pay = payment_analysis(df)
daily = daily_analysis(df)

# Metrics
total = df["Amount"].sum()
highest = cat.idxmax()
avg_daily = daily.mean()

# Visuals
plot_category(cat)
plot_monthly(month)
plot_payment(pay)

# Report
generate_summary(total, highest, avg_daily, cat, month, pay)

print("Project executed successfully.")