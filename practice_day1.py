import pandas as pd
df = pd.read_csv('restaurant_sales.csv')
#display settings
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

print("=" * 50)
print("DAY 1: RESTAURANT SALES ANALYSIS")
print("=" * 50)
#========================================
#CHALLENGE 1: Data Loading & Exploration
#========================================
print("Data Loaded Successfully")
print()
print("📊 CHALLENGE 1: Data Loading")
print("Basics information:")
print(f"The numbers of transaction is: {len(df)}")
n_servers = df.groupby('server')
print(f"Number of unique servers: {len(n_servers)}")
n_items = df.groupby('item_name')
print(f"Number of unique items: {len(n_items)}")
df['date'] = pd.to_datetime(df['date'])
print(f"Date range: {df['date'].min().date()} - {df['date'].max().date()}")
#add revenue column
df['revenue']=df['price']*df['quantity']
print(df[['revenue']].head(10))
print()
#========================================
#CHALLENGE 2: Basic Calculations
#========================================
print("💰 CHALLENGE 2: Basic Calculations")
total_revenue = df['revenue'].sum()
print(f"Total revenue: ${total_revenue}")
Average_revenue = total_revenue / len(df)
print(f"Average revenue: ${Average_revenue:.2f}")
highest_revenue = df['revenue'].max()
lowest_revenue = df['revenue'].min()
print(f"Highest revenue: ${highest_revenue:.2f}")
print(f"Lowest revenue: ${lowest_revenue:.2f}")
total_items = df['quantity'].sum()
print(f"Total items: {total_items} Items")
print()
#========================================
#CHALLENGE 3: Grouping & Aggregation
#========================================
print("📊 CHALLENGE 3: Grouping Analysis")
#Revenue by meal type
meal_revenue = df.groupby('meal_type')['revenue'].sum()
highest_meal_revenue = meal_revenue.max()
highest_meal = meal_revenue.idxmax()
print(f"The most selling meal is: {highest_meal} with ${highest_meal_revenue:.2f}")
for meal in meal_revenue.index:
    rev = meal_revenue[meal]
    percent = (rev/total_revenue)* 100
    print(f"{meal}: ${rev} ({percent:.2f}% of Total)")
print()
#performance by server
server_revenue = df.groupby('server')['revenue'].sum()
server_transaction = df.groupby('server').size()
average_server_revenue = server_revenue/server_transaction
print(average_server_revenue)
for server in server_revenue.index:
    server_rev = server_revenue[server]
    server_trans = server_transaction[server]
    avg_rev = average_server_revenue[server]
    print(f"{server}, has a revenue of ${server_rev:.2f} with {server_trans} transactions and ${avg_rev:.2f} in Average")
top_server = server_revenue.idxmax()
top_server_revenue = server_revenue.max()
print(f"{top_server} is Top Server with ${top_server_revenue}")
print()
#Category analysis
category_revenue = df.groupby('category')['revenue'].sum()
top_category_revenue = category_revenue.max()
top_category = category_revenue.idxmax()
print(f"{top_category} is Top Category with ${top_category_revenue}")
category_transaction = df.groupby('category').size()
average_category_revenue = category_revenue/category_transaction
for category in category_transaction.index:
    avg_cat = average_category_revenue[category]
    print(f"{category}, has a revenue of ${avg_cat:.2f}")
print()
#transactions grouping for export
trans_payment = df.groupby('payment_method').size()
payment_revenue = df.groupby('payment_method')['revenue'].sum()
#========================================
#CHALLENGE 4: Filtering
#========================================
print("🔍 CHALLENGE 4: Filtering")
#order over 100$
order_over_100 = len(df[df['revenue']>100])
print(f"There is {order_over_100} orders over $100")
cash_payment = len(df[df['payment_method']=='Cash'])
print(f"There are {cash_payment} cash payments")
alice_sales = len(df[df['server'] == 'Alice'])
print(f"Alice has {alice_sales} sales")
high_dinner = len(df[(df['meal_type']=='Dinner') & (df['revenue']>80)])
print(f"There is {high_dinner} high value dinner sales")
breakfast_items = len(df[df['meal_type']=='Breakfast'])
print(f"There is {breakfast_items} breakfast items")
print()
# ============================================
# CHALLENGE 5: EXPORT SUMMARIES
# ============================================
print("💾 CHALLENGE 5: Export")
server_performance = pd.DataFrame({
    'server': df['server'].unique(),
    'revenue': server_revenue.values,
    'transactions': server_transaction.values,
    'Avg_transactions': average_server_revenue.values.round(2),
}).sort_values('revenue', ascending=False)
server_performance.to_csv('server_performance.csv', index=False) #not sure how to make it from highest lo smallest revenue
meal_type_summary = pd.DataFrame({
    'meal_type': df['meal_type'].unique(),
    'revenue': meal_revenue.values,
    'percentage': ((meal_revenue.values/total_revenue)*100).round(2)
}).sort_values('revenue', ascending=False)
meal_type_summary.to_csv('meal_type_summary.csv', index=False)
payment_summary = pd.DataFrame({
    'payment_method': df['payment_method'].unique(),
    'transactions_count': trans_payment.values,
    'total_revenue': payment_revenue.values,
})
payment_summary.to_csv('payment_summary.csv')
print("All files created")
print()
print("✅ Day 1 Complete!")