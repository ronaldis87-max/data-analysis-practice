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
# ============================================
# CHALLENGE 2A: Location Performance
# ============================================
print("\n" + "=" * 60)
print("🗺️ CHALLENGE 2A: Location Performance")
print("=" * 60)
print()

# Total revenue by location
loc_revenue = df.groupby('location')['revenue'].sum()
best_loc = loc_revenue.idxmax()
best_loc_rev = loc_revenue.max()
percent_loc_revenue = (loc_revenue / Total_revenue) * 100

for location in loc_revenue.index:
    revenue = loc_revenue[location]
    revenue_pct = percent_loc_revenue[location]
    print(f"{location} generates ${revenue:,.2f} ({revenue_pct:.1f}% of total)")

print(f"\n🏆 {best_loc} has more revenue with ${best_loc_rev:,.2f}")
print()

# Average transaction value by location
loc_avg = df.groupby('location')['revenue'].mean()
highest_loc_avg = loc_avg.idxmax()
print(f"The location with higher-value customers: {highest_loc_avg}")

# Transaction count
loc_trans = df.groupby('location')['revenue'].count()
highest_loc_trans = loc_trans.idxmax()
print(f"The busiest location: {highest_loc_trans}")
print()

# Customer type mix by location
loc_cust_rev = df.groupby(['location', 'customer_type'])['revenue'].sum().unstack()
print("Customer Type Revenue by Location:")
for location in loc_cust_rev.index:
    top_cust = loc_cust_rev.loc[location].idxmax()
    top_cust_rev = loc_cust_rev.loc[location].max()
    print(f"{location} → Top customer: {top_cust} (${top_cust_rev:,.2f})")
print()

# Top products by location
loc_prod_rev = df.groupby(['location', 'product'])['revenue'].sum().unstack()
print("Top Product by Location:")
for location in loc_prod_rev.index:
    top_prod = loc_prod_rev.loc[location].idxmax()
    top_prod_rev = loc_prod_rev.loc[location].max()
    print(f"{location} → Top product: {top_prod} (${top_prod_rev:,.2f})")
print()

# Efficiency
loc_efficiency = loc_revenue / loc_trans

# SUMMARY FOR RECOMMENDATION
print("\n" + "=" * 60)
print("📋 SUMMARY OF FINDINGS")
print("=" * 60)
print()

for location in loc_revenue.index:
    # Gather all metrics
    revenue = loc_revenue[location]
    revenue_pct = percent_loc_revenue[location]
    transactions = loc_trans[location]
    trans_pct = (transactions / Total_trans) * 100
    avg_transaction = loc_avg[location]
    efficiency = loc_efficiency[location]

    # Top customer and product
    top_customer = loc_cust_rev.loc[location].idxmax()
    top_customer_rev = loc_cust_rev.loc[location].max()
    top_product = loc_prod_rev.loc[location].idxmax()
    top_product_rev = loc_prod_rev.loc[location].max()

    # Print comprehensive summary
    print(f"{location}:")
    print(f"  Revenue: ${revenue:,.2f} ({revenue_pct:.1f}% of total)")
    print(f"  Transactions: {transactions} ({trans_pct:.1f}% of total)")
    print(f"  Average transaction: ${avg_transaction:.2f}")
    print(f"  Efficiency: ${efficiency:.2f} per transaction")
    print(f"  Top customer type: {top_customer} (${top_customer_rev:,.2f})")
    print(f"  Top product: {top_product} (${top_product_rev:,.2f})")
    print()
print("\n" + "=" * 60)
print("💡 STRATEGIC RECOMMENDATION")
print("=" * 60)

# Get metrics
downtown_revenue = loc_revenue['Downtown']
downtown_pct = percent_loc_revenue['Downtown']
sub_revenue = loc_revenue['Suburb']
sub_pct = percent_loc_revenue['Suburb']
sub_trans = loc_trans['Suburb']

print("\nRECOMMENDATION: Open New SUBURB Location\n")

print("WHY SUBURB MODEL:")
print(f"• Suburb generates ${sub_revenue:,.2f} ({sub_pct:.1f}% of revenue)")
print(f"• Downtown generates ${downtown_revenue:,.2f} ({downtown_pct:.1f}% of revenue)")
print(f"• Nearly EQUAL performance, but Suburb likely has:")
print(f"  - Lower rent costs")
print(f"  - Lower operating expenses")
print(f"  - More parking (better customer experience)")
print()

print("TARGET LOCATION: South region of city")
print("• Currently underserved")
print(f"• Customers travel to Downtown for quality parts")
print("• Bring parts closer = capture this demand")
print()

# Calculate opportunity
new_store_target = sub_revenue * 0.35

print("FINANCIAL PROJECTION:")
print(f"• Target: 35% of existing Suburb revenue")
print(f"• Expected Year 1 revenue: ${new_store_target:,.2f}")
print(f"• With lower costs, profit margin higher than Downtown")
print()

print("ACTION PLAN:")
print("1. Market analysis: South city demographics & competition")
print("2. Site selection: High visibility, good parking")
print("3. Business plan: Projected costs vs revenue")
print("4. Leadership buy-in & funding approval")
print("5. Launch & monthly performance tracking")
print()

print("SUCCESS METRICS:")
print(f"• Year 1: ${new_store_target:,.2f} revenue")
print("• Month 6: 30% Walk-in → Regular conversion")
print("• Month 12: Positive cash flow")
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
print("\n" + "=" * 60)
print("📊 INVENTORY MANAGEMENT STRATEGY")
print("=" * 60)

# Get specific values for fast/slow movers
fastest_mover = qty_product.idxmax()
fastest_qty = qty_product.max()
slowest_mover = qty_product.idxmin()
slowest_qty = qty_product.min()

print("\n🚀 STOCK MORE (Fast Movers):")
print(f"\nTop 5 products by volume:")
for i, (product, quantity) in enumerate(qty_product.sort_values(ascending=False).head(5).items(), 1):
    rev_per_unit = unit_rev[product]
    print(f"  {i}. {product}: {quantity} units sold (${rev_per_unit:.2f}/unit)")

print(f"\nAction: Increase inventory levels by 50% for these items")
print(f"Risk: Running out of {fastest_mover} loses {fastest_qty} monthly sales!")

print("\n📉 STOCK LESS (Slow Movers):")
print(f"\nBottom 5 products by volume:")
for i, (product, quantity) in enumerate(qty_product.sort_values().head(5).items(), 1):
    rev_per_unit = unit_rev[product]
    print(f"  {i}. {product}: {quantity} units sold (${rev_per_unit:.2f}/unit)")

print(f"\nAction: Reduce inventory to 2-week supply")
print(f"Benefit: Free up capital tied in slow-moving stock")

print("\n💰 HIGH-VALUE FOCUS:")
print(f"\nHighest revenue per unit: {top_unit_rev} (${rev_unit_rev:.2f}/unit)")
print(f"Category dominance: {best_catbyrev}")
print(f"\nAction: Train staff to upsell high-margin items")
print(f"Ensure {top_unit_rev} is ALWAYS in stock - premium customers expect it!")

print("\n📦 CATEGORY STRATEGY:")
for category in cat_rev.sort_values(ascending=False).head(3).index:
    cat_revenue = cat_rev[category]
    cat_pct = (cat_revenue / cat_rev.sum()) * 100
    num_products = prod_in_cat[category]
    avg_per_product = avg_pro_cat[category]

    print(f"\n{category}:")
    print(f"  Revenue: ${cat_revenue:,.2f} ({cat_pct:.1f}% of total)")
    print(f"  {num_products} products, ${avg_per_product:,.2f} avg per product")

    if num_products >= 5:
        print(f"  Strategy: Volume category - maintain variety, competitive pricing")
    else:
        print(f"  Strategy: Premium category - focus on quality, margins")

print("\n🎯 KEY METRICS TO TRACK:")
print(f"1. Stock-out rate for top 5 fast movers (Target: 0%)")
print(f"2. Inventory turnover for slow movers (Target: reduce by 30%)")
print(f"3. {top_unit_rev} sales growth (Target: +20% through staff training)")
print(f"4. {best_catbyrev} category share (Maintain dominance)")

print("\n✅ Challenge 2B Complete!")
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