from pathlib import Path
import json

Path("notebooks").mkdir(exist_ok=True)

notebook = {
    "cells": [

        # ---------------- Setup ----------------
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["# 💲 Personal Expense Tracker - EDA Notebook"]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "import sys\n",
                "sys.path.append('..')\n",
                "\n",
                "import pandas as pd\n",
                "import matplotlib.pyplot as plt\n",
                "\n",
                "from src.data_loader import load_data\n",
                "from src.cleaner import clean_data\n",
                "from src.analysis import category_analysis, monthly_analysis, payment_analysis\n",
                "\n",
                "print('Setup Complete')"
            ]
        },

        # ---------------- Load Data ----------------
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 📥 Load Dataset"]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "df = load_data('../data/expenses.csv')\n",
                "df = clean_data(df)\n",
                "df.head()"
            ]
        },

        # ---------------- Data Info ----------------
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 📊 Dataset Info"]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "df.info()\n",
                "df.describe()"
            ]
        },

        # ---------------- Category Analysis ----------------
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 💰 Category-wise Spending"]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "cat = category_analysis(df)\n",
                "cat"
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "cat.plot(kind='bar', color='green')\n",
                "plt.title('Category Spending')\n",
                "plt.show()"
            ]
        },

        # ---------------- Monthly Analysis ----------------
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 📅 Monthly Spending Trend"]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "month = monthly_analysis(df)\n",
                "month"
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "month.plot(marker='o', color='green')\n",
                "plt.title('Monthly Trend')\n",
                "plt.show()"
            ]
        },

        # ---------------- Payment Analysis ----------------
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 💳 Payment Method Distribution"]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "pay = payment_analysis(df)\n",
                "pay"
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "pay.plot(kind='pie', autopct='%1.1f%%')\n",
                "plt.title('Payment Methods')\n",
                "plt.show()"
            ]
        },

        # ---------------- Insights ----------------
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["## 📌 Key Insights"]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "source": [
                "print('Highest spending category:', cat.idxmax())\n",
                "print('Total spending:', df['Amount'].sum())\n",
                "print('Average daily spending:', df.groupby('Date')['Amount'].sum().mean())"
            ]
        }

    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python (Expense Tracker)",
            "language": "python",
            "name": "expense_tracker"
        },
        "language_info": {
            "name": "python"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}

with open("notebooks/expense_analysis.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print("Full multi-cell notebook created successfully.")