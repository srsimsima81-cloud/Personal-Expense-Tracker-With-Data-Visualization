def category_analysis(df):
    return df.groupby("Category")["Amount"].sum()

def monthly_analysis(df):
    return df.groupby("Month")["Amount"].sum()

def payment_analysis(df):
    return df.groupby("Payment_Method")["Amount"].sum()

def daily_analysis(df):
    return df.groupby("Date")["Amount"].sum()