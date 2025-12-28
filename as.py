import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Restaurant data
data = {
    "Order_ID": [1, 2, 3, 4, 5],
    "Customer": ["Rahul", "Anjali", "Karan", "Neha", "Rahul"],
    "Item": ["Burger", "Pizza", "Pasta", "Burger", "Pizza"],
    "Quantity": [2, 1, 1, 1, 2],
    "Price": [120, 250, 200, 120, 250]
}

df = pd.DataFrame(data)

# Calculate total bill per order
df["Total_Bill"] = df["Quantity"] * df["Price"]

# Total restaurant sales
total_sales = np.sum(df["Total_Bill"])

# Most popular items
popular_items = df["Item"].value_counts()

# Display results
print("Restaurant Orders:\n", df)
print("\nTotal Sales:", total_sales)
print("\nMost Popular Items:\n", popular_items)

# Visualize most popular items
popular_items.plot(kind="bar", color="skyblue")
plt.title("Most Popular Food Items")
plt.xlabel("Item")
plt.ylabel("Number of Orders")
plt.show()

# Visualize total sales per customer
sales_per_customer = df.groupby("Customer")["Total_Bill"].sum()
sales_per_customer.plot(kind="pie", autopct='%1.1f%%', startangle=90, colors=["lightgreen", "lightblue", "orange", "pink"])
plt.title("Total Sales per Customer")
plt.ylabel("")
plt.show()

