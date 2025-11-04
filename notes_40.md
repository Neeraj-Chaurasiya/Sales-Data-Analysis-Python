
# 📅 Day 40 – End-to-End Sales Data Analysis Project (Pandas + Visualization)

---

## 🎯 Objective

E-commerce sales dataset ka use karke **data cleaning, feature engineering, visualization, aur reporting** karna.  
Ye project tumhara **first complete data analysis pipeline** hoga jisme Python ke Pandas aur Seaborn ka full use hai.

---

## ✅ Topics Covered

- Data loading & cleaning  
- Feature engineering (final amount, profit)  
- Exploratory data analysis (EDA)  
- Region & category-wise insights  
- Visualizations (bar, scatter, pie, heatmap)  
- Export final Excel report  

---

## 🧩 Step 1 – Import & Clean Data

```python
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

df = pd.read_csv(r"c:/Freelanceing (500 days)/Month_02/day_40/ecommerce_sales_34500.csv")
print(df.info())
print(df.isnull().sum())
df.dropna(inplace=True)
```

**Explanation:**  
- Loads sales dataset into a Pandas DataFrame.  
- `df.info()` → Check columns, data types, and missing values.  
- `dropna()` → Removes missing/null records to ensure clean data.  

💡 **Tip:** Always clean data before visualization to avoid inaccurate charts.

---

## 🧮 Step 2 – Feature Engineering

```python
df["final Amount"] = df["price"] * df["quantity"] * (1 - df["discount"])
df["Profit"] = df["final Amount"] * 0.15
print(df.head(3))
```

**Explanation:**  
- Calculates **final Amount** after discount.  
- Adds a **Profit** column (15% profit margin assumed).  
- Adds meaningful business metrics to the dataset.

💡 **Feature Engineering** converts raw data into insights-ready columns.

---

## 📊 Step 3 – Exploratory Analysis (EDA)

```python
region_summary = df.groupby("region")["final Amount"].sum().reset_index()
category_summary = df.groupby("category")["final Amount"].sum().reset_index()
print(category_summary)
```

**Explanation:**  
- Groups sales data by **region** and **category**.  
- Aggregates total revenue for each group.  
- Helps identify top-performing business areas.

---

## 🎨 Step 4 – Visualization 1: Region-wise Total Sales

```python
plt.figure(figsize=(10,6))
sns.barplot(x="region", y="final Amount", data=df, estimator=sum, ci=None, palette="crest")
plt.title("Region-wise Total Sales")
plt.ylabel("Total Sales (₹)")
plt.xlabel("Region")
plt.savefig("c:/Freelanceing (500 days)/Month_02/day_40/Output/region_sales.png", dpi=300)
plt.show()
```

**Explanation:**  
- Bar chart compares total sales across regions.  
- `estimator=sum` → Aggregates values.  
- `palette="crest"` → Adds a modern blue-green gradient.

💡 **Insight:** Quickly shows which region contributes most to revenue.

---

## 📊 Step 5 – Visualization 2: Category-wise Total Sales

```python
plt.figure(figsize=(10,6))
sns.barplot(x="category", y="final Amount", data=df, estimator=sum, ci=None, palette="crest")
plt.title("Category-wise Total Sales")
plt.ylabel("Total Sales (₹)")
plt.xlabel("Category")
plt.savefig("c:/Freelanceing (500 days)/Month_02/day_40/Output/category_sales.png", dpi=300)
plt.show()
```

**Explanation:**  
- Displays which product categories perform best.  
- Helps focus marketing or supply chain on top categories.

💡 **Insight:** Identify best-performing categories.

---

## 💰 Step 6 – Visualization 3: Profit vs Discount (Scatter Plot)

```python
plt.figure(figsize=(10,6))
sns.scatterplot(x="Profit", y="discount", data=df, alpha=0.6)
plt.title("Profit vs Discount")
plt.xlabel("Profit")
plt.ylabel("Discount")
plt.savefig("c:/Freelanceing (500 days)/Month_02/day_40/Output/profit_vs_discount.png", dpi=300)
plt.show()
```

**Explanation:**  
- Each dot = one sale record.  
- Reveals relationship between **profit** and **discount**.  
- `alpha=0.6` adds slight transparency for overlapping points.

💡 **Insight:** Higher discounts may reduce profit — this chart verifies it.

---

## 🔥 Step 7 – Visualization 4: Correlation Heatmap

```python
plt.figure(figsize=(8,6))
corr = df[["price","quantity","discount","final Amount","Profit"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap (Sales Metrics)", fontsize=15, fontweight="bold")
plt.tight_layout()
plt.savefig("c:/Freelanceing (500 days)/Month_02/day_40/Output/correlation_heatmap.png", dpi=300)
plt.show()
```

**Explanation:**  
- Shows correlation strength between key numeric columns.  
- `annot=True` → Displays numeric correlation values.  
- `coolwarm` → Red-blue gradient for better visual contrast.

💡 **Insight:** Reveals how sales, discounts, and profit interact.

---

## 🧾 Step 8 – Visualization 5: Payment Method Distribution (Pie Chart)

```python
plt.figure(figsize=(7,7))
payment_counts = df["payment_method"].value_counts()
plt.pie(payment_counts, labels=payment_counts.index, autopct="%1.1f%%", startangle=120)
plt.title("Payment Method Distribution", fontsize=15, fontweight="bold")
plt.tight_layout()
plt.savefig("c:/Freelanceing (500 days)/Month_02/day_40/Output/payment_method_share.png", dpi=300)
plt.show()
```

**Explanation:**  
- Displays share of different payment methods (like Cash, UPI, Card).  
- `autopct` shows percentage distribution.  
- Circular chart for quick summary view.

💡 **Insight:** Helps businesses understand payment preferences.

---

## 📦 Step 9 – Export & Report Generation

```python
total_revenue = df["final Amount"].sum()
avg_profit = df["Profit"].mean()
Top_customers = df.groupby("customer_id")["final Amount"].sum().sort_values(ascending=False).head().reset_index()
Top_category = df.groupby("category")["quantity"].sum().sort_values(ascending=False).head(2).reset_index()

summary_data = {
  "Metric": ["total_revenue","avg_profit","Top_category"],
  "Value": [total_revenue,avg_profit,Top_category["category"][0]]
}

summary_df = pd.DataFrame(summary_data)

with pd.ExcelWriter("c:/Freelanceing (500 days)/Month_02/day_40/sales_report.xlsx") as writer:
  summary_df.to_excel(writer, sheet_name="Summary", index=False)
  Top_customers.to_excel(writer, sheet_name="Top_Customer", index=False)
  df.head(100).to_excel(writer, sheet_name="Sample_Data", index=False)
```

**Explanation:**  
- Summarizes total revenue, average profit, and top category.  
- Writes all results into a single Excel workbook with 3 sheets.  
- Output file → `sales_report.xlsx`

💡 **Insight:** Automates entire reporting process — client-ready format.

---

## 🧠 Summary

| Step | Action | Output |
|------|---------|---------|
| 1 | Load and clean data | Missing values handled |
| 2 | Feature engineering | Added “Final Amount” & “Profit” |
| 3 | EDA | Region & Category summaries |
| 4 | Visualization | 5 Charts generated |
| 5 | Export | Excel report with summary sheets |

---

## 🌟 Outcome

By end of Day 40:  
You’ve built a **real-world end-to-end data analysis project** using Pandas + Seaborn.  
You now know how to clean data, create features, visualize insights, and export reports.  

💼 **Resume Tip:**  
> “Developed an end-to-end e-commerce data analysis pipeline using Pandas, Seaborn, and Excel reporting. Generated business insights through data visualization and KPI summary automation.”

---
