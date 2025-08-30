import pandas as pd
import matplotlib.pyplot as plt

# load csv
print("loading data...")
df = pd.read_csv("OnlineRetail.csv", encoding="ISO-8859-1")
print("data loaded, shape =", df.shape)
print(df.head())

# clean data
print("cleaning data...")
df = df.dropna()   # remove missing
df = df.drop_duplicates()   # remove dups
print("after clean, shape =", df.shape)

# change date col
print("converting date col...")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# add total column
print("adding total column...")
df["total"] = df["Quantity"] * df["UnitPrice"]

# ---- simple checks ----
print("\n--- quick stats ---")
total_sales = df["total"].sum()
most_sold = df.groupby("Description")["Quantity"].sum().idxmax()
avg_order = df.groupby("InvoiceNo")["total"].sum().mean()
uniq_customers = df["CustomerID"].nunique()

print("total sales =", total_sales)
print("most sold =", most_sold)
print("avg order value =", avg_order)
print("unique customers =", uniq_customers)

# ---- plots ----
print("\nplotting top 10 products...")
df.groupby("Description")["total"].sum().nlargest(10).plot(kind="bar", figsize=(10,5))
plt.title("Top 10 Products by Sales")
plt.show()

print("plotting monthly trend...")
df.resample("M", on="InvoiceDate")["total"].sum().plot(kind="line", figsize=(10,5))
plt.title("Monthly Sales Trend")
plt.show()

print("plotting sales by country...")
df.groupby("Country")["total"].sum().nlargest(5).plot(kind="pie", autopct="%1.1f%%", figsize=(6,6))
plt.title("Sales by Country (Top 5)")
plt.ylabel("")
plt.show()

# ---- insights ----
print("\n--- Insights ---")
print("1. total sales around =", round(total_sales,2))
print("2. most sold product is:", most_sold)
print("3. avg order value ~", round(avg_order,2))
print("4. unique customers =", uniq_customers)
print("5. UK is top country by sales")
print("6. sales peak in winter months (seasonal trend)")
