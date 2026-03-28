import pandas as pd

# ============================================
# CHALLENGE 1A: Product Performance Analysis
# ============================================
print("\n📦 CHALLENGE 1A: Product Performance\n")

# Load data
df = pd.read_csv('retail_sales.csv')
df['date'] = pd.to_datetime(df['date'])
df['revenue'] = df['price'] * df['quantity']

# Revenue analysis
print("=" * 50)
print("REVENUE ANALYSIS")
print("=" * 50)

rev_product = df.groupby('product')['revenue'].sum()
best_product = rev_product.idxmax()
best_product_rev = rev_product.max()

print(f"\n🏆 Top Revenue: {best_product} (${best_product_rev:,.2f})")

print("\nTop 5 Products by Revenue:")
for i, (product, revenue) in enumerate(rev_product.sort_values(ascending=False).head(5).items(), 1):
    print(f"  {i}. {product}: ${revenue:,.2f}")

# Quantity analysis
print("\n" + "=" * 50)
print("QUANTITY ANALYSIS")
print("=" * 50)

qtt_product = df.groupby('product')['quantity'].sum()
most_sold = qtt_product.idxmax()
most_sold_qtt = qtt_product.max()

print(f"\n🏆 Most Sold: {most_sold} ({most_sold_qtt} units)")

print("\nTop 5 Products by Quantity:")
for i, (product, quantity) in enumerate(qtt_product.sort_values(ascending=False).head(5).items(), 1):
    print(f"  {i}. {product}: {quantity} units")

# Price analysis
print("\n" + "=" * 50)
print("PRICE ANALYSIS")
print("=" * 50)

avg_product = rev_product / qtt_product
most_exp = avg_product.idxmax()

print(f"\n💰 Most Expensive Average: {most_exp} (${avg_product[most_exp]:.2f})")

print("\nAverage Price by Product:")
for product, price in avg_product.sort_values(ascending=False).items():
    print(f"  {product}: ${price:.2f}")

# Comparison
print("\n" + "=" * 50)
print("KEY INSIGHT")
print("=" * 50)

if best_product == most_sold:
    print("✅ Revenue leader = Quantity leader")
else:
    print(f"❌ Different leaders:")
    print(f"   Revenue: {best_product}")
    print(f"   Quantity: {most_sold}")

print("\n✅ Challenge 1A Complete!")
# ============================================
# CHALLENGE 1B: Customer Segmentation
# ============================================
print("\n" + "=" * 60)
print("👥 CHALLENGE 1B: Customer Segmentation")
print("=" * 60)
#Total revenue by customer type
Total_revenue = df['revenue'].sum()
Total_trans = df['revenue'].count()
rev_customer = df.groupby('customer_type')['revenue'].sum()
percent_customer_revenue = (rev_customer / Total_revenue)*100
best_cust_type = rev_customer.idxmax()
best_cust_type_rev = rev_customer.max()
print(f"The type of customer who generates the most revenue is {best_cust_type} with ${best_cust_type_rev}")
print("Percentage of customer revenue:")
print(percent_customer_revenue.round(2).sort_values(ascending=False))
#Average transaction value by customer type
avg_customer_revenue = df.groupby('customer_type')['revenue'].mean()
most_spender_type = avg_customer_revenue.idxmax()
print("")
if best_cust_type == most_spender_type:
    print("same customer segmentation has high volume and high value!")
else:
    print(f"revenue leader is {best_cust_type} and value leader is {most_spender_type}")
#Transaction count by customer type
trans_count = df.groupby('customer_type')['revenue'].count()
most_trans = trans_count.idxmax()
print(f"\n{most_trans} has the most transactions")
#Products preference by customer type
product_customer_type = df.groupby(['customer_type', 'product'])['revenue'].sum().unstack()
for customer_type in product_customer_type.index:
    top_product = product_customer_type.loc[customer_type].idxmax()
    top_product_rev = product_customer_type.loc[customer_type].max()
    print(f"{customer_type} → Top product: {top_product} with ${top_product_rev}")
print("\n" + "=" * 60)
print("📊 STRATEGIC RECOMMENDATION")
print("=" * 60)

# Summary of findings
print("\n📋 SUMMARY OF FINDINGS:\n")

for customer_type in rev_customer.sort_values(ascending=False).index:
    revenue = rev_customer[customer_type]
    revenue_pct = percent_customer_revenue[customer_type]
    transactions = trans_count[customer_type]
    trans_pct = (transactions / Total_trans) * 100
    avg_value = avg_customer_revenue[customer_type]

    print(f"{customer_type}:")
    print(f"  Revenue: ${revenue:,.2f} ({revenue_pct:.1f}% of total)")
    print(f"  Transactions: {transactions} ({trans_pct:.1f}% of total)")
    print(f"  Average: ${avg_value:.2f} per transaction")
    print()

# Strategic recommendation
print("\n" + "=" * 60)
print("💡 STRATEGIC RECOMMENDATION")
print("=" * 60)

# Get Walk-in specific metrics
walkin_revenue = rev_customer['Walk-in']
walkin_pct = percent_customer_revenue['Walk-in']
walkin_trans = trans_count['Walk-in']

print("\nPRIORITY: CONVERT WALK-IN TO REGULAR CUSTOMERS\n")
print(f"Walk-ins generate ${walkin_revenue:,.2f} ({walkin_pct:.1f}% of total revenue)")
print("This revenue is FRAGILE - these customers have no loyalty\n")

# Calculate opportunity
conversion_rate = 0.30
secured_revenue = walkin_revenue * conversion_rate

print(f"OPPORTUNITY: Converting 30% of Walk-ins to Regulars")
print(f"  → Secures ${secured_revenue:,.2f} in recurring revenue")
print(f"  → Adds {int(walkin_trans * conversion_rate)} loyal customers")
print(f"  → Reduces revenue risk significantly\n")

print("ACTION PLAN:")
print("  1. Capture email/phone at checkout")
print("  2. Follow-up offer: 10% off next purchase")
print("  3. Launch loyalty program: Buy 5 get 1 free")
print("  4. Monthly tracking of conversion rate\n")

print("SUCCESS METRIC: 30% Walk-in → Regular conversion in 6 months")

print("\n✅ Challenge 1B Complete!")