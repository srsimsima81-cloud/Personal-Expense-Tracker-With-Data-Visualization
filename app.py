import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from src.data_loader import load_data
from src.cleaner import clean_data
from src.analysis import category_analysis, monthly_analysis, payment_analysis

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Expense Dashboard", layout="wide")

# -----------------------------
# UI STYLING
# -----------------------------
st.markdown("""
<style>

/* Background */
.stApp {
    background: radial-gradient(circle at top, #02040a, #000000);
    color: #ffffff;
}

/* Global text */
html, body, [class*="css"] {
    color: #ffffff !important;
    font-family: Arial;
}

/* Headings */
h1, h2, h3, h4 {
    color: #ffffff !important;
    text-shadow: 0 0 8px #00ff99, 0 0 15px #00ff99;
}

/* Metrics */
div[data-testid="metric-container"] {
    background: rgba(0, 255, 120, 0.05);
    border: 1px solid rgba(0, 255, 120, 0.25);
    border-radius: 12px;
    padding: 15px;
    box-shadow: 0 0 12px rgba(0,255,120,0.25);
}

/* Buttons */
.stButton>button {
    background: #00ff99;
    color: black;
    font-weight: bold;
    border-radius: 10px;
    border: none;
}

.stButton>button:hover {
    box-shadow: 0 0 15px #00ff99;
    transform: scale(1.05);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #05070f;
}

/* Dataframe text */
.dataframe {
    color: white !important;
}

/* Chart text */
text {
    fill: white !important;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD DATA
# -----------------------------
df = load_data("data/expenses.csv")
df = clean_data(df)

# -----------------------------
# TITLE
# -----------------------------
st.title("💲 Personal Expense Dashboard")
st.write("Track your spending, analyze patterns, and improve financial control.")

# -----------------------------
# METRICS
# -----------------------------
col1, col2, col3 = st.columns(3)

total_spent = df["Amount"].sum()
highest_cat = category_analysis(df).idxmax()
avg_daily = df.groupby("Date")["Amount"].sum().mean()

col1.metric("Total Spending", f"₹ {total_spent:,.0f}")
col2.metric("Top Category", highest_cat)
col3.metric("Avg Daily Spend", f"₹ {avg_daily:,.0f}")

# -----------------------------
# CATEGORY BAR CHART (GREEN)
# -----------------------------
st.subheader("Category Insights")

fig1, ax1 = plt.subplots(figsize=(4, 2.2), dpi=120)

category_analysis(df).plot(
    kind="bar",
    ax=ax1,
    color="#00ff99",
    edgecolor="white"
)

ax1.set_facecolor("#000000")
fig1.patch.set_facecolor("#000000")

ax1.tick_params(axis='x', colors='white', rotation=35)  # 🔥 FIX
ax1.tick_params(axis='y', colors='white')

ax1.set_title("Spending by Category", color="white")

plt.tight_layout()

st.pyplot(fig1, use_container_width=False)
# -----------------------------
# MONTHLY LINE CHART (GREEN)
# -----------------------------
st.subheader("Monthly Trend")

fig2, ax2 = plt.subplots(figsize=(6, 3))

monthly_analysis(df).plot(
    kind="line",
    marker="o",
    ax=ax2,
    color="#00ff99",
    linewidth=2
)

ax2.set_facecolor("#000000")
fig2.patch.set_facecolor("#000000")

ax2.tick_params(colors="white")
ax2.set_title("Monthly Spending Trend", color="white")

plt.tight_layout()

st.pyplot(fig2)

# -----------------------------
# PAYMENT PIE CHART (FIXED SMALL)
# -----------------------------
st.subheader("Payment Distribution")

fig3, ax3 = plt.subplots(figsize=(3, 3), dpi=120)  # 🔥 FIXED SIZE

payment_analysis(df).plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax3,
    textprops={'color': 'white'}
)

ax3.set_ylabel("")
fig3.patch.set_facecolor("#000000")

plt.tight_layout()

st.pyplot(fig3, use_container_width=False)  # 🔥 IMPORTANT FIX

# -----------------------------
# DATA TABLE
# -----------------------------
st.subheader("Transaction Data")
st.dataframe(df, use_container_width=True)