import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
transaction_df = pd.read_csv(r"R:\New folder\transaction_data.csv")
purchase_df = pd.read_csv(r"R:\New folder\purchase_behaviour.csv")

# Convert DATE column to datetime format
transaction_df["DATE"] = pd.to_datetime(transaction_df["DATE"], origin="1899-12-30", unit="D")

# Merge datasets on LYLTY_CARD_NBR
merged_df = transaction_df.merge(purchase_df, on="LYLTY_CARD_NBR", how="left")

# Identify top 3 most profitable products
top_products = merged_df.groupby("PROD_NAME")["TOT_SALES"].sum().nlargest(3).reset_index()
print("Top 3 Most Profitable Products:")
print(top_products)

# Identify most profitable customer segments
customer_segments = merged_df.groupby(["LIFESTAGE", "PREMIUM_CUSTOMER"])["TOT_SALES"].sum().reset_index()
customer_segments = customer_segments.sort_values(by="TOT_SALES", ascending=False)
print("\nMost Profitable Customer Segments:")
print(customer_segments)

# Visualize top products
plt.figure(figsize=(10, 5))
sns.barplot(x="TOT_SALES", y="PROD_NAME", data=top_products, palette="viridis")
plt.title("Top 3 Most Profitable Products")
plt.xlabel("Total Sales")
plt.ylabel("Product Name")
plt.show()

# Visualize customer segmentation
plt.figure(figsize=(12, 6))
sns.barplot(x="TOT_SALES", y="LIFESTAGE", hue="PREMIUM_CUSTOMER", data=customer_segments, palette="coolwarm")
plt.title("Customer Segments by Total Sales")
plt.xlabel("Total Sales")
plt.ylabel("Lifestage")
plt.legend(title="Premium Customer")
plt.show()

# Summary of insights
summary = """
Insights:
1. The top 3 most profitable products are Dorito Corn Chp Supreme 380g, Smiths Crnkle Chip Orgnl Big Bag 380g, and Smiths Crinkle Chips Salt & Vinegar 330g.
2. The most profitable customer segments are older families and mid-age couples who are premium customers.
3. These customers likely have higher spending capacity and prefer premium or bulk-size products.
4. Marketing should focus on targeting these high-value customer segments with loyalty programs and exclusive deals.
"""
print(summary)
