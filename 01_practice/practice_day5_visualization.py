import pandas as pd
import matplotlib.pyplot as plt

# Set style for better-looking charts
plt.style.use('ggplot')

print("=" * 60)
print("DAY 5: DATA VISUALIZATION")
print("=" * 60)
print()

# Load your retail data
df = pd.read_csv('retail_sales.csv')
df['date'] = pd.to_datetime(df['date'])
df['revenue'] = df['price'] * df['quantity']

print(f"✅ Loaded {len(df)} transactions")
print()

# ============================================
# CHALLENGE 5A: Revenue by Product Bar Chart
# ============================================
print("📊 CHALLENGE 5A: Your First Bar Chart\n")

# TODO: Calculate revenue by product
rev_by_product = df.groupby('product')['revenue'].sum()

# TODO: Sort values (highest first)
rev_by_product = rev_by_product.sort_values(ascending=False)

# TODO: Create the bar chart
plt.figure(figsize=(10, 6))  # Size of chart
rev_by_product.plot(kind='bar', color='steelblue')

# TODO: Add labels and title
plt.title('Revenue by Product', fontsize=16, fontweight='bold')
plt.xlabel('Product', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.xticks(rotation=45, ha='right')  # Rotate product names
plt.tight_layout()  # Prevent labels from getting cut off

# TODO: Show the chart
plt.show()

print("✅ Challenge 5A Complete!")
# ============================================
# CHALLENGE 5B: Customer Type Comparison
# ============================================
print("\n📊 CHALLENGE 5B: Customer Type Bar Chart\n")

# TODO: Calculate revenue by customer type
rev_by_customer = df.groupby('customer_type')['revenue'].sum()

# TODO: Sort values (highest first)
rev_by_customer = rev_by_customer.sort_values(ascending=False)

# TODO: Create the bar chart
plt.figure(figsize=(8, 6))
rev_by_customer.plot(kind='bar', color='coral')

# TODO: Add labels and title
plt.title('Revenue by Customer Type', fontsize=16, fontweight='bold')
plt.xlabel('Customer Type', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

print("✅ Challenge 5B Complete!")
# ============================================
# CHALLENGE 5C: Daily Revenue Trend Line
# ============================================
print("\n📈 CHALLENGE 5C: Daily Revenue Trend\n")

# TODO: Calculate daily revenue
daily_revenue = df.groupby('date')['revenue'].sum()
daily_revenue = daily_revenue.sort_index()

# TODO: Create the line chart
plt.figure(figsize=(12, 6))
daily_revenue.plot(kind='line', color='green', linewidth=2, marker='o')
# TODO: Add labels and title
plt.title('Daily Revenue Trend', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
print("✅ Challenge 5C Complete!")
# ============================================
# CHALLENGE 5D: Location Performance
# ============================================
print("\n📊 CHALLENGE 5D: Location Comparison\n")

# TODO: Calculate revenue by location
rev_by_location = df.groupby('location')['revenue'].sum()
rev_by_location = rev_by_location.sort_values(ascending=False)

# TODO: Create the bar chart
plt.figure(figsize=(7, 6))
rev_by_location.plot(kind='bar', color='purple')
# TODO: Add labels and title
plt.title('Revenue by Location', fontsize=16, fontweight='bold')
plt.xlabel('Location', fontsize=12)
plt.ylabel('Revenue ($)', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# Pie chart version (for comparison)
plt.figure(figsize=(8, 8))
colors = ['purple', 'mediumpurple']
rev_by_location.plot(kind='pie', autopct='%1.1f%%', colors=colors, startangle=90)
plt.title('Revenue Distribution by Location', fontsize=16, fontweight='bold')
plt.ylabel('')  # Remove default ylabel
plt.tight_layout()
plt.show()
print("✅ Challenge 5D Complete!")
# ============================================
# CHALLENGE 5E: COMPLETE DASHBOARD
# ============================================
print("\n🎨 CHALLENGE 5E: Multi-Chart Dashboard\n")

# Create a figure with 4 subplots (2 rows, 2 columns)
fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle('RETAIL ANALYTICS DASHBOARD', fontsize=20, fontweight='bold', y=0.995)

# Chart 1: Products (top-left)
rev_by_product = df.groupby('product')['revenue'].sum().sort_values(ascending=False)
rev_by_product.plot(kind='bar', color='steelblue', ax=axes[0, 0])
axes[0, 0].set_title('Revenue by Product', fontsize=14, fontweight='bold')
axes[0, 0].set_xlabel('Product', fontsize=10)
axes[0, 0].set_ylabel('Revenue ($)', fontsize=10)
axes[0, 0].tick_params(axis='x', rotation=45, labelsize=8)

# Chart 2: Customers (top-right)
rev_by_customer = df.groupby('customer_type')['revenue'].sum().sort_values(ascending=False)
rev_by_customer.plot(kind='bar', color='coral', ax=axes[0, 1])
axes[0, 1].set_title('Revenue by Customer Type', fontsize=14, fontweight='bold')
axes[0, 1].set_xlabel('Customer Type', fontsize=10)
axes[0, 1].set_ylabel('Revenue ($)', fontsize=10)
axes[0, 1].tick_params(axis='x', rotation=0, labelsize=10)

# Chart 3: Daily Trend (bottom-left)
daily_revenue = df.groupby('date')['revenue'].sum().sort_index()
daily_revenue.plot(kind='line', color='green', linewidth=2, marker='o', ax=axes[1, 0])
axes[1, 0].set_title('Daily Revenue Trend', fontsize=14, fontweight='bold')
axes[1, 0].set_xlabel('Date', fontsize=10)
axes[1, 0].set_ylabel('Revenue ($)', fontsize=10)
axes[1, 0].grid(True, alpha=0.3)

# Chart 4: Locations (bottom-right)
rev_by_location = df.groupby('location')['revenue'].sum().sort_values(ascending=False)
rev_by_location.plot(kind='bar', color='purple', ax=axes[1, 1])
axes[1, 1].set_title('Revenue by Location', fontsize=14, fontweight='bold')
axes[1, 1].set_xlabel('Location', fontsize=10)
axes[1, 1].set_ylabel('Revenue ($)', fontsize=10)
axes[1, 1].tick_params(axis='x', rotation=0, labelsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()
plt.show()

print("✅ Challenge 5E Complete!")
print("\n🎉 DAY 5 COMPLETE - You're a Data Visualization Master!")