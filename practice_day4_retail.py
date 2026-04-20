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
# Let's summarize what we found:
print("\n📋 SUMMARY OF FINDINGS:\n")

for customer_type in rev_customer.index:
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
print("Recommendation: Focus on Walk-In customers")
print(f"They generate ${revenue:,.2f} ({revenue_pct:.1f}% of total)") #how can i get the exact value for customer segment i want? right now it works because walkin is last in loop, right?
print(f"Action: Offer Strong Fidelity Program to make them part of Regular customer These are our wilds card this month they shop with us if next month they go away we lose that Revenue")
# ============================================
# CHALLENGE 2A: Location Performance
# ============================================
print("\n" + "=" * 60)
print("🗺️ CHALLENGE 2A: Location Performance")
print("=" * 60)
print()
#Total revenue by location
loc_revenue = df.groupby('location')['revenue'].sum()
best_loc = loc_revenue.idxmax()
best_loc_rev = loc_revenue.max()
percent_loc_revenue = (loc_revenue / Total_revenue)*100
for location in loc_revenue.index:
    revenue = loc_revenue[location]
    revenue_pct = percent_loc_revenue[location]
    print(f"{location} generate ${revenue:,.2f} ({revenue_pct:.1f}% of total)")
print(f"{best_loc} has more revenue with ${best_loc_rev}")
print()
#Average transaction value by location
loc_avg = df.groupby('location')['revenue'].mean()
highest_loc_avg = loc_avg.idxmax()
print(f"The location with higher-value customers is {highest_loc_avg}")
loc_trans = df.groupby('location')['revenue'].count()
highest_loc_trans = loc_trans.idxmax()
print(f"The busiest location is {highest_loc_trans}")
print()
#Customer type mix by location
loc_cust_rev = df.groupby(['location', 'customer_type'])['revenue'].sum().unstack()
for location in loc_cust_rev.index:
    top_cust = loc_cust_rev.loc[location].idxmax()
    top_cust_rev = loc_cust_rev.loc[location].max()
    print(f"{location} top customer: {top_cust} with ${top_cust_rev}")
print()
#Top products by location
loc_prod_rev = df.groupby(['location', 'product'])['revenue'].sum().unstack()
for location in loc_prod_rev.index:
    top_prod = loc_prod_rev.loc[location].idxmax()
    top_prod_rev = loc_prod_rev.loc[location].max()
    print(f"{location} top products: {top_prod} with ${top_prod_rev}")
#effeciciency
loc_efficiency = loc_revenue / loc_trans
#recommendation
print("\n📋 SUMMARY OF FINDINGS:\n")
for location in loc_revenue.index:
    revenue = loc_revenue[location]
    revenue_pct = percent_loc_revenue[location]
    transactions = loc_trans[location]
    avg_transaction = loc_avg[location]
    efficiency = loc_efficiency[location]
    top_cust = loc_cust_rev.loc[location].idxmax()
    top_cust_rev = loc_cust_rev.loc[location].max()
    top_prod = loc_prod_rev.loc[location].idxmax()
    top_prod_rev = loc_prod_rev.loc[location].max()

    # Print summary
    print(f"{location}:")
    print(f"  Revenue: ${revenue:,.2f} ({revenue_pct:.1f}% of total)")
    print(f"  Transactions: {transactions} ({(transactions/Total_trans)*100:.1f}% of total)")
    print(f"  Average transaction: ${avg_transaction:.2f}")
    print(f"  Efficiency: ${efficiency:.2f} per transaction")
    print(f"  Top customer type: {top_cust} (${top_cust_rev:,.2f})")
    print(f"  Top product: {top_prod} (${top_prod_rev:,.2f})")
# Strategic recommendation
print("\n" + "=" * 60)
print("💡 STRATEGIC RECOMMENDATION")
print("=" * 60)
# Get Walk-in specific metrics
sub_revenue = loc_revenue['Suburb']
sub_pct = percent_loc_revenue['Suburb']
sub_trans = loc_trans['Suburb']

print("\nPRIORITY: OPEN NEW SUBURB Location in parts of city we are not present\n")
print(f"Suburb location generate ${sub_revenue:,.2f} ({sub_pct:.1f}% of total revenue) with {sub_trans} transactions")
print("This revenue is closed to Downtown Revenue - with more transanctions than dowtown, we can easily speculates that dowtown store is more expensive to operates making suburb focus strategy more cost effective\n")

# Calculate opportunity
conversion_rate = 0.35
new_revenue = sub_revenue * conversion_rate

print(f"OPPORTUNITY: Converting 35% of south regin of city population in our Walk-ins customers")
print(f"  → Secures ${new_revenue:,.2f} in newly obtained revenue")
print(f"  → We are not present in the south a dynamic and poorly served region customer who need better quality parts goes to downtown, let's bring part closer to them and convert newly acquired walkins in regular customer with time\n")

print("ACTION PLAN:")
print("  1. Analyse South city region needs and business opportunities")
print("  2. Make business plan and get buy-in from leadership")
print("  3. Launch new store")
print("  4. Monthly tracking of conversion rate\n")

print("SUCCESS METRIC: New Suburb store revenue equal 35%  first suburb store")

print("\n✅ Challenge 2A Complete!")
# ============================================
# CHALLENGE 2B: Inventory & Product Insights
# ============================================
print("\n" + "=" * 60)
print("📦 CHALLENGE 2B: Inventory & Product Insights")
print("=" * 60)
print()
#Product velocity (how fast items sell)
qty_product = df.groupby('product')['quantity'].sum()
print("Top 5 fast movers Products:")
for i, (product, quantity) in enumerate(qty_product.sort_values(ascending=False).head(5).items(), 1):
    print(f"  {i}. {product}: {quantity} units")
print("\nBottom 5 slow movers Products:")
for i, (product, quantity) in enumerate(qty_product.sort_values().head(5).items(), 1):
    print(f"  {i}. {product}: {quantity} units")
print()
#Revenue per unit analysis
unit_rev = rev_product/qty_product
top_unit_rev = unit_rev.idxmax()
rev_unit_rev = unit_rev.max()
print(f" {top_unit_rev} generate most revenue per unit sold with ${rev_unit_rev:,.2f} per unit sold")
#Category performance
cat_rev = df.groupby('category')['revenue'].sum()
qty_cat = df.groupby('category')['quantity'].sum()
best_catbyrev = cat_rev.idxmax()
best_catbyqty = qty_cat.idxmax()
print(f"{best_catbyrev} dominates in revenue and {best_catbyqty} dominates by quantity")
print()
#Count products in each category
prod_in_cat = df.groupby('category')['product'].nunique()
print(prod_in_cat)
#Average revenue per product within each category
avg_pro_cat = cat_rev/prod_in_cat
print("Average Revenue Per Product by Category:")
for category in avg_pro_cat.index:
    avg = avg_pro_cat[category]
    num_prod = prod_in_cat[category]
    total = cat_rev[category]
    print(f"{category}:")
    print(f"  {num_prod} products genarating ${total:,.2f} total revenue")
    print(f"  Average ${avg:,.2f} per product")
    print()
#Which categories have the most expensive products?
most_exp_prod = avg_pro_cat.idxmax()
print(f"{most_exp_prod} has the most expensive product")
print()
print("Inventory recommendations")
print("Management should Focus on:")
print(f" -{best_catbyrev} which dominates in revenue and by quantity")
print(f" -{top_unit_rev} which generates most revenue per unit sold")
print(f" -Stock more of the top 5 products identified and less of the bottom 5 products")
# ============================================
# CHALLENGE 3: Export Key Summaries
# ============================================
print("\n" + "=" * 60)
print("📤 CHALLENGE 3: Exporting Analysis")
print("=" * 60)
print()

# Create exports folder if it doesn't exist
import os
if not os.path.exists('exports'):
    os.makedirs('exports')
    print("✅ Created 'exports' folder")

# Export 1: Product Performance Summary
product_summary = pd.DataFrame({
    'product': rev_product.index,
    'total_revenue': rev_product.values,
    'total_quantity': qty_product.values,
    'revenue_per_unit': unit_rev.values
})
product_summary = product_summary.sort_values('total_revenue', ascending=False)
product_summary.to_csv('exports/product_performance.csv', index=False)
print("✅ Exported: product_performance.csv")

# Export 2: Customer Segmentation Summary
customer_summary = pd.DataFrame({
    'customer_type': rev_customer.index,
    'total_revenue': rev_customer.values,
    'revenue_percentage': percent_customer_revenue.values,
    'transaction_count': trans_count.values,
    'average_transaction': avg_customer_revenue.values
})
customer_summary = customer_summary.sort_values('total_revenue', ascending=False)
customer_summary.to_csv('exports/customer_segmentation.csv', index=False)
print("✅ Exported: customer_segmentation.csv")

# Export 3: Location Performance Summary
location_summary = pd.DataFrame({
    'location': loc_revenue.index,
    'total_revenue': loc_revenue.values,
    'revenue_percentage': percent_loc_revenue.values,
    'transaction_count': loc_trans.values,
    'average_transaction': loc_avg.values
})
location_summary.to_csv('exports/location_performance.csv', index=False)
print("✅ Exported: location_performance.csv")

# Export 4: Category Analysis
category_summary = pd.DataFrame({
    'category': cat_rev.index,
    'total_revenue': cat_rev.values,
    'total_quantity': qty_cat.values,
    'num_products': prod_in_cat.values,
    'avg_revenue_per_product': avg_pro_cat.values
})
category_summary = category_summary.sort_values('total_revenue', ascending=False)
category_summary.to_csv('exports/category_analysis.csv', index=False)
print("✅ Exported: category_analysis.csv")

# Export 5: Inventory Recommendations (Fast & Slow Movers)
inventory_rec = pd.DataFrame({
    'product': qty_product.index,
    'quantity_sold': qty_product.values,
    'total_revenue': rev_product.values,
    'revenue_per_unit': unit_rev.values
})
inventory_rec = inventory_rec.sort_values('quantity_sold', ascending=False)
inventory_rec['recommendation'] = inventory_rec['quantity_sold'].apply(
    lambda x: 'STOCK MORE' if x > qty_product.median() else 'STOCK LESS'
)
inventory_rec.to_csv('exports/inventory_recommendations.csv', index=False)
print("✅ Exported: inventory_recommendations.csv")

print()
print("📁 All summaries exported to 'exports/' folder!")
print("\n✅ Challenge 3 Complete!")