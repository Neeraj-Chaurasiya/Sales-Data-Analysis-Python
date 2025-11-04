# Import & Clean Data

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv(r"c:/Freelanceing (500 days)/Month_02/day_40/ecommerce_sales_34500.csv")
print(df.info())
print(df.isnull().sum())
df.dropna(inplace=True)

# Feature Engineering

df["final Amount"] = df["price"] * df["quantity"] * (1 - df["discount"])
df["Profit"] = df["final Amount"]*0.15
print(df.head(3))

# Exploratory Analysis

region_summary = df.groupby("region")["final Amount"].sum().reset_index()
category_summary = df.groupby("category")["final Amount"].sum().reset_index()
print(category_summary)

# Visualization :


plt.figure(figsize=(10,6))
sns.barplot(x="region",y="final Amount", data=df, estimator=sum, ci=None, palette="crest")
plt.title("Region-wise Total Sales ")
plt.ylabel("Total Sales (₹)")
plt.xlabel("Region")
plt.savefig("c:/Freelanceing (500 days)/Month_02/day_40/Output/region_sales.png", dpi=300)
plt.show()

plt.figure(figsize=(10,6))
sns.barplot(x="category", y="final Amount", data=df, estimator=sum, ci=None, palette="crest")
plt.title("Category-wise Total sales ")
plt.ylabel("Total Sales (₹)")
plt.xlabel("Category")
plt.savefig("c:/Freelanceing (500 days)/Month_02/day_40/Output/category_sales.png", dpi=300)
plt.show()

plt.figure(figsize=(10,6))
sns.scatterplot(x="Profit", y="discount", data=df,  alpha=0.6)
plt.title("Profit vs discount")
plt.xlabel("Profit")
plt.ylabel("Discount")
plt.savefig("c:/Freelanceing (500 days)/Month_02/day_40/Output/profit_vs_discount.png", dpi=300)
plt.show()

plt.figure(figsize=(8,6))
corr = df[["price","quantity","discount","final Amount","Profit"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap (Sales Metrics)", fontsize=15, fontweight="bold")
plt.tight_layout()
plt.savefig("c:/Freelanceing (500 days)/Month_02/day_40/Output/correlation_heatmap.png", dpi=300)
plt.show()

plt.figure(figsize=(7,7))
payment_counts = df["payment_method"].value_counts()
plt.pie(payment_counts, labels=payment_counts.index, autopct="%1.1f%%", startangle=120)
plt.title("Payment method distribution ", fontsize = 15, fontweight = "bold")
plt.tight_layout()
plt.savefig("c:/Freelanceing (500 days)/Month_02/day_40/Output/payment_method_share.png", dpi=300)
plt.show()

# Export & Report

total_revenue = df["final Amount"].sum()
avg_profit = df["Profit"].mean()
Top_customers = df.groupby("customer_id")["final Amount"].sum().sort_values(ascending=False).head().reset_index()
Top_category = df.groupby("category")["quantity"].sum().sort_values(ascending=False).head(2).reset_index()

print("Total Revenue :",total_revenue)
print("Average Profit per Sale: :",avg_profit)
print("\nTop 5 Customers:\n",Top_customers)
print("\nMost Popular Category:\n",Top_category)

summary_data = {
  "Metric": ["total_revenue","avg_profit","Top_category"],
  "Value": [total_revenue,avg_profit,Top_category["category"][0]]
}

summary_df = pd.DataFrame(summary_data)

with pd.ExcelWriter("c:/Freelanceing (500 days)/Month_02/day_40/sales_report.xlsx") as writer:
  summary_df.to_excel(writer, sheet_name="Summary", index=False)
  Top_customers.to_excel(writer, sheet_name="Top_Custormer", index=False)
  df.head(100).to_excel(writer, sheet_name="Sample_Data", index=False)

