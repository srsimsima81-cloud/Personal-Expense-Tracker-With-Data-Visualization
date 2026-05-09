def generate_summary(total, highest, avg_daily, category, monthly, payment):

    summary = f"""
EXPENSE SUMMARY REPORT
======================

TOTAL SPENDING: ₹{total}

HIGHEST CATEGORY: {highest}

AVERAGE DAILY SPENDING: ₹{avg_daily}

CATEGORY DATA:
{category}

MONTHLY DATA:
{monthly}

PAYMENT DATA:
{payment}
"""

    with open("outputs/summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)