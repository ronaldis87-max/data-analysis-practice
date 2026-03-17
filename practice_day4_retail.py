import pandas as pd
# ============================================
# CHALLENGE 1A: Product Performance Analysis
# ============================================
print("\n📦 CHALLENGE 1A: Product Performance\n")
#Load data
df = pd.read_csv('retail_sales.csv')
df['date'] = pd.to_datetime(df['date'])
df['revenue'] = df['price'] * df['quantity']
#Calculate total revenue by product
rev_product = df.groupby('product')['revenue'].sum()
best_product = rev_product.idxmax()
best_product_rev = rev_product.max()
print(f"{best_product} generate highest revenue with ${best_product_rev}")
print("Top five products by Revenue:")
Sorted_rev_product = rev_product.sort_values(ascending=False)
print(Sorted_rev_product.head(5)) # wanted to print it nicely using loop and enumerate but i don't have my note i remember i can do something like this and where i have done it before but can't from memory
print()
#Calculate total quantity sold by product
qtt_product = df.groupby('product')['quantity'].sum()
most_sold = qtt_product.idxmax()
most_sold_qtt = qtt_product.max()
print(f"{most_sold} is most sold product with {most_sold_qtt} items sold")
print("Top five products by Quantity:")
sorted_qtt_product = qtt_product.sort_values(ascending=False)
print(sorted_qtt_product.head(5))
print()
avg_product = rev_product / qtt_product
most_exp = avg_product.idxmax()
print("Average price by product:")
print(avg_product)
print(f" The most expensive product on average is {most_exp} ")
if best_product == most_sold:
    print("✅ Yes, same product!")
else:
    print(f"❌ No, revenue leader is {best_product} and quantity leader is {most_sold}")