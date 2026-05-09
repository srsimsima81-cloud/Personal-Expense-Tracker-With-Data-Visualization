import matplotlib.pyplot as plt

def plot_category(data):
    data.plot(kind="bar")
    plt.title("Category-wise Spending")
    plt.tight_layout()
    plt.savefig("images/category.png")
    plt.close()

def plot_monthly(data):
    data.plot(kind="line", marker="o")
    plt.title("Monthly Spending")
    plt.tight_layout()
    plt.savefig("images/monthly.png")
    plt.close()

def plot_payment(data):
    data.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Payment Method")
    plt.tight_layout()
    plt.savefig("images/payment.png")
    plt.close()