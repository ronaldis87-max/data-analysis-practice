# Python Data Analysis - Complete Learning Reference
**Student Journey: Beginner to Business Analyst (5 Weeks)**

**Author:** Ronaldis (ronaldis87-max)  
**Goal:** Analyze family auto parts business with Lightspeed POS data  
**Status:** Week 5 - Data Visualization Complete

---

## 📚 Table of Contents
1. [Learning Journey Overview](#learning-journey-overview)
2. [Critical Concepts - Foundation](#critical-concepts---foundation)
3. [Pandas Core Operations](#pandas-core-operations)
4. [Business Analysis Framework](#business-analysis-framework)
5. [Data Visualization Principles](#data-visualization-principles)
6. [Strategic Thinking Patterns](#strategic-thinking-patterns)
7. [Common Mistakes & Solutions](#common-mistakes--solutions)
8. [Code Pattern Library](#code-pattern-library)
9. [Quick Reference Cheat Sheet](#quick-reference-cheat-sheet)

---

## Learning Journey Overview

### Week 1-2: Foundation (Restaurant Data)
**Key Achievement:** Learned pandas basics through restaurant sales analysis

**Skills Acquired:**
- Loading CSV files with pandas
- Basic data exploration (`.head()`, `.info()`, `.describe()`)
- Creating calculated columns (`df['revenue'] = df['price'] * df['quantity']`)
- Simple grouping and aggregation
- Time-based analysis (extracting day of week, month)

**Mindset Shift:** "Problem → Metric → Code" thinking established

**Critical Learning:** Break large challenges into 15-20 min micro-tasks for sustainable progress

---

### Week 3: Obstacle & Resilience (Laptop Broken)
**Challenge:** Laptop screen broke mid-learning

**Response:**
- Set up work computer with PyCharm
- Learned Git/GitHub for code syncing
- Maintained momentum despite setback
- Connected laptop to TV at home

**Key Lesson:** Obstacles are opportunities to learn professional workflows (Git became portfolio skill!)

**Mindset Shift:** "Quick feedback > perfectionism" - Ask questions early, iterate fast

---

### Week 4: Business Analysis (Retail Data)
**Key Achievement:** Completed full retail analytics with strategic recommendations

**Skills Acquired:**
- Multi-dimensional grouping (`df.groupby(['customer_type', 'product'])`)
- Customer segmentation analysis
- Location performance comparison
- Inventory management insights
- Strategic business recommendations with financial projections

**Business Thinking Breakthrough:** Identified Walk-in customers as "fragile revenue" requiring loyalty program conversion

**Projects Completed:**
- Product performance analysis
- Customer segmentation (Fleet/Regular/Walk-in)
- Location comparison (Downtown vs Suburb)
- Inventory optimization (fast movers vs slow movers)

---

### Week 5: Data Visualization (Current)
**Key Achievement:** Built professional analytics dashboard

**Skills Acquired:**
- Matplotlib basics
- Bar charts (category comparison)
- Line charts (time trends)
- Multi-panel dashboards (`plt.subplots()`)
- Chart formatting and styling

**Milestone:** Created boardroom-quality 4-panel dashboard showing complete business overview

---

## Critical Concepts - Foundation

### 1. DataFrames: The Core Structure

**What it is:**
DataFrame = Spreadsheet in Python

Rows = individual records/transactions
Columns = different attributes/fields
Index = row labels (often 0, 1, 2... or dates)
**Critical Understanding:**
```python
# DataFrame structure
df = pd.DataFrame({
    'product': ['Brake Pads', 'Oil Filter'],
    'price': [45.99, 12.50],
    'quantity': [2, 5]
})

# Result:
#       product  price  quantity
# 0  Brake Pads  45.99         2
# 1  Oil Filter  12.50         5
```

**Key Methods:**
- `df.head(10)` - View first 10 rows
- `df.info()` - Data types and missing values
- `df.describe()` - Statistical summary
- `df.shape` - (rows, columns)
- `len(df)` - Number of rows

---

### 2. Series: Single Column

**What it is:**
Series = One column from a DataFrame

Has an index (row labels)
Has values (the data)
Like a dictionary with extra powers
**Critical Understanding:**
```python
# Extract a Series
prices = df['price']

# Result:
# 0    45.99
# 1    12.50
# Name: price, dtype: float64

# Operations on Series
prices.sum()      # Total: 58.49
prices.mean()     # Average: 29.245
prices.max()      # Highest: 45.99
prices.idxmax()   # Index of max: 0
```

**Key Distinction:**
```python
df['price']        # Returns Series
df[['price']]      # Returns DataFrame (one column)
```

---

### 3. The GroupBy Operation (MOST CRITICAL!)

**What it does:**
Splits data into groups, applies function to each group, combines results

**The Pattern:**
```python
df.groupby('category')['revenue'].sum()
#    ↓         ↓          ↓        ↓
#  Split    By What    What to   How to
#  data     column    measure   combine
```

**Mental Model:**
Original Data:
product        revenue
Brake Pads     100
Oil Filter      50
Brake Pads     150
Oil Filter      75
After groupby('product')['revenue'].sum():
product        revenue
Brake Pads     250  ← 100 + 150
Oil Filter     125  ← 50 + 75
**Common Aggregations:**
- `.sum()` - Total
- `.mean()` - Average
- `.count()` - How many
- `.max()` / `.min()` - Highest/Lowest
- `.std()` - Standard deviation (consistency measure)

---

### 4. Multi-Level GroupBy (Advanced)

**Pattern:**
```python
df.groupby(['location', 'customer_type'])['revenue'].sum()
```

**What happens:**
Groups by BOTH location AND customer_type:
Downtown + Fleet      → $X
Downtown + Regular    → $Y
Downtown + Walk-in    → $Z
Suburb + Fleet        → $A
Suburb + Regular      → $B
Suburb + Walk-in      → $C
**Making it Readable with .unstack():**
```python
result = df.groupby(['location', 'customer_type'])['revenue'].sum().unstack()

# Creates a table:
#            Fleet  Regular  Walk-in
# Downtown    $X      $Y       $Z
# Suburb      $A      $B       $C
```

**Accessing Values:**
```python
# Get specific value
result.loc['Downtown', 'Fleet']  # Returns $X

# Get best customer type per location
for location in result.index:
    best_customer = result.loc[location].idxmax()
    best_revenue = result.loc[location].max()
    print(f"{location} best: {best_customer} (${best_revenue})")
```

---

### 5. Filtering Data

**Basic Filtering:**
```python
# Single condition
expensive = df[df['price'] > 100]

# Multiple conditions (AND)
high_value = df[(df['price'] > 100) & (df['quantity'] > 2)]

# Multiple conditions (OR)
items = df[(df['product'] == 'Battery') | (df['product'] == 'Tire')]
```

**Critical:** Use `&` (and) and `|` (or), NOT `and`/`or`!

**Filter then Analyze:**
```python
# Revenue from Walk-in customers only
walkin_revenue = df[df['customer_type'] == 'Walk-in']['revenue'].sum()

# Pattern: Filter first, then calculate
```

---

### 6. Creating Calculated Columns

**The Pattern:**
```python
df['new_column'] = calculation

# Examples:
df['revenue'] = df['price'] * df['quantity']
df['profit'] = df['revenue'] - df['cost']
df['margin_pct'] = (df['profit'] / df['revenue']) * 100
```

**Using Datetime:**
```python
df['date'] = pd.to_datetime(df['date'])
df['day_name'] = df['date'].dt.day_name()
df['month'] = df['date'].dt.month
df['week_number'] = df['date'].dt.isocalendar().week
```

---

## Pandas Core Operations

### Sorting

**By Values:**
```python
# Highest to lowest
df.sort_values('revenue', ascending=False)

# Lowest to highest
df.sort_values('price', ascending=True)

# Multiple columns
df.sort_values(['customer_type', 'revenue'], ascending=[True, False])
```

**By Index (for dates!):**
```python
# Chronological order
df.sort_index()

# Reverse chronological
df.sort_index(ascending=False)
```

**Critical Pattern:**
```python
# Always sort after groupby for rankings
top_products = df.groupby('product')['revenue'].sum().sort_values(ascending=False)
```

---

### Finding Maximum/Minimum

**Get the NAME of max:**
```python
series.idxmax()  # Returns the INDEX/NAME

# Example:
revenue_by_product.idxmax()  # Returns "Battery" (product name)
```

**Get the VALUE of max:**
```python
series.max()  # Returns the VALUE

# Example:
revenue_by_product.max()  # Returns 15234.56 (revenue amount)
```

**Common Pattern:**
```python
best_product = revenue_by_product.idxmax()
best_revenue = revenue_by_product.max()
print(f"{best_product} generated ${best_revenue:,.2f}")
```

---

### Iteration Patterns

**Iterating over Series:**
```python
# Method 1: .items() - get both name and value
for product, revenue in revenue_by_product.items():
    print(f"{product}: ${revenue}")

# Method 2: .index - just names
for product in revenue_by_product.index:
    print(product)

# Method 3: .values - just values
for revenue in revenue_by_product.values:
    print(revenue)
```

**With enumerate (for numbering):**
```python
for i, (product, revenue) in enumerate(revenue_by_product.items(), 1):
    print(f"{i}. {product}: ${revenue:,.2f}")

# Output:
# 1. Battery: $15,234.56
# 2. Tire: $12,456.78
```

---

### Percentage Calculations

**Pattern:**
```python
# Calculate percentage of total
percentage = (part / total) * 100

# Example:
total_revenue = df['revenue'].sum()
revenue_by_customer = df.groupby('customer_type')['revenue'].sum()
percentage_by_customer = (revenue_by_customer / total_revenue) * 100

# Result:
# Fleet      33.5%
# Regular    30.8%
# Walk-in    35.7%
```

---

### Counting Unique Values

**Pattern:**
```python
# Count unique values in a column
df['product'].nunique()  # How many different products?

# Count per group
df.groupby('category')['product'].nunique()  # Products per category

# Example:
# Brake System        2 products
# Fluids & Filters    7 products
# Electrical          2 products
```

---

## Business Analysis Framework

### The Strategic Analysis Pattern

**Every analysis follows this structure:**
DATA COLLECTION
↓
CALCULATION (groupby, sum, mean, etc.)
↓
INTERPRETATION (what does it mean?)
↓
INSIGHT (what's the opportunity/risk?)
↓
RECOMMENDATION (what should we DO?)
↓
IMPACT PROJECTION (what's the expected result?)

### Real Example: Walk-in Customer Analysis

**1. Data Collection:**
```python
df = pd.read_csv('retail_sales.csv')
```

**2. Calculation:**
```python
revenue_by_customer = df.groupby('customer_type')['revenue'].sum()
# Walk-in: $65,039 (35.7%)
# Fleet: $61,107 (33.5%)
# Regular: $56,037 (30.8%)
```

**3. Interpretation:**
Walk-in customers generate the MOST revenue but have NO loyalty

**4. Insight:**
This is FRAGILE revenue - they can shop anywhere, anytime
35.7% of revenue is at risk (zero-sum game)

**5. Recommendation:**
PRIORITY: Convert Walk-ins to Regular customers via loyalty program
- Capture contact info at checkout
- Follow-up: 10% off next purchase
- Loyalty card: Buy 5 get 1 free

**6. Impact Projection:**
```python
conversion_rate = 0.30  # Convert 30% of Walk-ins
walkin_revenue = $65,039
secured_revenue = walkin_revenue * conversion_rate  # $19,512

print(f"Securing ${secured_revenue:,.2f} in recurring revenue")
print(f"Adding {int(243 * 0.30)} loyal customers")
```

**Result:** Actionable strategy with measurable goals

---

### The Risk/Opportunity Framework

**Questions to ask for every metric:**

**Risk Assessment:**
- What could go wrong?
- What's fragile or unstable?
- Where are we vulnerable?

**Opportunity Identification:**
- What's working well that we can amplify?
- Where's untapped potential?
- What quick wins exist?

**Example:**
High Walk-in revenue = Risk (can disappear)
+ Opportunity (convert to loyal!)
---

## Data Visualization Principles

### Chart Type Selection

**The Decision Tree:**
What am I showing?
├─ COMPARING CATEGORIES → Bar Chart
│  Examples: Products, customer types, locations
│  Code: .plot(kind='bar')
│
├─ TREND OVER TIME → Line Chart
│  Examples: Daily revenue, weekly growth
│  Code: .plot(kind='line')
│
├─ PARTS OF WHOLE → Pie Chart
│  Examples: Revenue distribution, market share
│  Code: .plot(kind='pie')
│
└─ RELATIONSHIP BETWEEN TWO VARIABLES → Scatter Plot
Examples: Price vs quantity, age vs spending
Code: .plot(kind='scatter')
---

### The Universal Chart Pattern

**Same 6 steps for EVERY chart:**

```python
# 1. Get your data
data = df.groupby('column')['metric'].sum()

# 2. Sort it (by value for bars, by index for time)
data = data.sort_values(ascending=False)  # OR .sort_index()

# 3. Create figure
plt.figure(figsize=(width, height))

# 4. Plot it
data.plot(kind='bar', color='color_name')

# 5. Label it
plt.title('Chart Title', fontsize=16, fontweight='bold')
plt.xlabel('X Label', fontsize=12)
plt.ylabel('Y Label', fontsize=12)
plt.xticks(rotation=45)  # If needed
plt.tight_layout()

# 6. Show it
plt.show()
```

**Memorize this pattern - it's 90% of visualization!**

---

### Bar Chart Best Practices

**When to rotate labels:**
```python
# Many categories (>5) with long names → Rotate 45°
plt.xticks(rotation=45, ha='right')

# Few categories (≤3) with short names → Keep horizontal
plt.xticks(rotation=0)
```

**Choosing colors:**
- Different chart types = different colors (helps distinguish)
- Professional colors: steelblue, coral, green, purple
- Avoid: bright red/yellow (hard to read)

**Chart sizing:**
```python
# Regular charts
plt.figure(figsize=(8, 6))

# Time series (wider to fit dates)
plt.figure(figsize=(12, 6))

# Single category comparison
plt.figure(figsize=(7, 6))
```

---

### Line Chart for Time Series

**Critical differences from bar charts:**

```python
# 1. Sort by INDEX (dates), not values
daily_revenue = df.groupby('date')['revenue'].sum()
daily_revenue = daily_revenue.sort_index()  # ← Chronological!

# 2. Use 'line' kind with markers
daily_revenue.plot(kind='line', linewidth=2, marker='o')

# 3. Wider figure for many dates
plt.figure(figsize=(12, 6))

# 4. Lighter grid
plt.grid(True, alpha=0.3)
```

---

### Dashboard Layout (Advanced)

**Creating multi-panel dashboards:**

```python
# Create 2x2 grid (4 charts)
fig, axes = plt.subplots(2, 2, figsize=(16, 10))

# Main title
fig.suptitle('DASHBOARD TITLE', fontsize=20, fontweight='bold')

# Plot to specific positions
data1.plot(kind='bar', ax=axes[0, 0])  # Top-left
data2.plot(kind='bar', ax=axes[0, 1])  # Top-right
data3.plot(kind='line', ax=axes[1, 0])  # Bottom-left
data4.plot(kind='bar', ax=axes[1, 1])  # Bottom-right

# Format each subplot
axes[0, 0].set_title('Chart 1 Title')
axes[0, 0].set_xlabel('X Label')
axes[0, 0].set_ylabel('Y Label')

# Prevent overlap
plt.tight_layout()
plt.show()
```

**Grid positions:**
axes[0, 0]  axes[0, 1]
axes[1, 0]  axes[1, 1]
[row, column]
---

## Strategic Thinking Patterns

### Pattern 1: Risk Identification

**Framework:**
---

## Strategic Thinking Patterns

### Pattern 1: Risk Identification

**Framework:**
High value + Low stability = HIGH RISK
**Example:**
- Walk-in customers: 35.7% revenue + zero loyalty = RISK
- Action: Convert to stable customer base

---

### Pattern 2: Opportunity Sizing

**Framework:**
Current performance × Realistic improvement % = Opportunity size
**Example:**
```python
current_walkin_revenue = $65,039
conversion_rate = 0.30  # Conservative estimate
opportunity = current_walkin_revenue * conversion_rate
# = $19,512 in secured revenue
```

**Always quantify opportunities!**

---

### Pattern 3: Cost-Benefit Thinking

**Not just revenue - consider costs!**

**Example: Location Analysis**
Downtown: $95k revenue
Suburb: $87k revenue
Surface analysis: "Downtown is better!"
Deeper analysis:

Downtown rent: $8k/month
Suburb rent: $3k/month
Net profit might favor Suburb!

Recommendation: Expand with Suburb model (better margins)
**Think: Revenue, Costs, Profit, ROI**

---

### Pattern 4: Portfolio Approach

**Don't optimize for ONE metric - balance multiple:**

**Example: Customer Mix**
Fleet: High value per transaction (premium)
Regular: Stable recurring revenue (foundation)
Walk-in: Volume/discovery (growth potential)
Strategy: Optimize ALL THREE, not just one
**Diversification reduces risk!**

---

## Common Mistakes & Solutions

### Mistake 1: Relying on Loop Order

**WRONG:**
```python
for customer_type in revenue_by_customer.index:
    revenue = revenue_by_customer[customer_type]

# Later...
print(f"Walk-in revenue: ${revenue}")  
# ← BUG! "revenue" is last in loop, might not be Walk-in!
```

**RIGHT:**
```python
# Get specific value explicitly
walkin_revenue = revenue_by_customer['Walk-in']
print(f"Walk-in revenue: ${walkin_revenue}")
```

**Lesson:** Always reference by key, never assume loop order!

---

### Mistake 2: Printing Series Instead of Values

**WRONG:**
```python
top_customer = customer_revenue_table[location]
print(f"Top customer: {top_customer}")

# Prints entire Series, not just the best one!
```

**RIGHT:**
```python
top_customer = customer_revenue_table.loc[location].idxmax()
top_revenue = customer_revenue_table.loc[location].max()
print(f"Top customer: {top_customer} (${top_revenue})")
```

**Lesson:** Use `.idxmax()` to get NAME, `.max()` to get VALUE

---

### Mistake 3: Sorting Time Series by Value

**WRONG:**
```python
daily_revenue = df.groupby('date')['revenue'].sum()
daily_revenue = daily_revenue.sort_values(ascending=False)
# ← Shows highest revenue days first, not chronological!
```

**RIGHT:**
```python
daily_revenue = df.groupby('date')['revenue'].sum()
daily_revenue = daily_revenue.sort_index()
# ← Chronological order for time trends!
```

**Lesson:** 
- Bar charts: Sort by VALUE
- Line charts: Sort by INDEX (time)

---

### Mistake 4: Perfectionism Paralysis

**WRONG MINDSET:**
"I need to figure this out perfectly alone before asking"
→ Spends 2 hours stuck
→ Gets frustrated
→ Loses momentum

**RIGHT MINDSET:**
"I'll try for 10-15 minutes, then ask for feedback"
→ Quick iteration
→ Learns faster
→ Maintains momentum

**Lesson:** Quick feedback > perfectionism!

---

## Code Pattern Library

### Pattern 1: Top N Analysis

```python
# Get top 5 products by revenue
top_products = df.groupby('product')['revenue'].sum().sort_values(ascending=False).head(5)

# Display with ranking
for i, (product, revenue) in enumerate(top_products.items(), 1):
    print(f"{i}. {product}: ${revenue:,.2f}")
```

---

### Pattern 2: Percentage Breakdown

```python
# Revenue distribution
total = df['revenue'].sum()
by_category = df.groupby('category')['revenue'].sum()
percentage = (by_category / total) * 100

for category in percentage.index:
    pct = percentage[category]
    amount = by_category[category]
    print(f"{category}: ${amount:,.2f} ({pct:.1f}%)")
```

---

### Pattern 3: Comparison Analysis

```python
# Compare two groups
group_a = df[df['location'] == 'Downtown']['revenue'].sum()
group_b = df[df['location'] == 'Suburb']['revenue'].sum()

if group_a > group_b:
    difference = group_a - group_b
    pct_diff = (difference / group_b) * 100
    print(f"Downtown outperforms by ${difference:,.2f} ({pct_diff:.1f}%)")
else:
    print("Suburb performs better")
```

---

### Pattern 4: Efficiency Metric

```python
# Revenue per transaction
total_revenue = df['revenue'].sum()
total_transactions = len(df)
efficiency = total_revenue / total_transactions

print(f"Average transaction: ${efficiency:.2f}")

# By category
category_revenue = df.groupby('category')['revenue'].sum()
category_transactions = df.groupby('category').size()
category_efficiency = category_revenue / category_transactions
```

---

### Pattern 5: Time-Based Aggregation

```python
# Daily aggregation
daily = df.groupby('date')['revenue'].sum().sort_index()

# Weekly aggregation
df['week'] = df['date'].dt.isocalendar().week
weekly = df.groupby('week')['revenue'].sum()

# Monthly aggregation
df['month'] = df['date'].dt.month
monthly = df.groupby('month')['revenue'].sum()
```

---

## Quick Reference Cheat Sheet

### Essential Imports
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

### Loading Data
```python
df = pd.read_csv('filename.csv')
df['date'] = pd.to_datetime(df['date'])
```

### Exploration
```python
df.head(10)          # First 10 rows
df.info()            # Data types, missing values
df.describe()        # Statistics
df['column'].unique()  # Unique values
df['column'].nunique() # Count unique
```

### Grouping & Aggregating
```python
# Single column
df.groupby('category')['revenue'].sum()
df.groupby('category')['revenue'].mean()
df.groupby('category').size()

# Multiple columns
df.groupby(['location', 'customer_type'])['revenue'].sum().unstack()
```

### Filtering
```python
df[df['price'] > 100]
df[df['customer_type'] == 'Fleet']
df[(df['price'] > 100) & (df['quantity'] > 2)]
```

### Sorting
```python
df.sort_values('revenue', ascending=False)
df.sort_index()  # For dates
```

### Finding Max/Min
```python
series.idxmax()  # Name of max
series.max()     # Value of max
series.idxmin()  # Name of min
series.min()     # Value of min
```

### Date Operations
```python
df['day_name'] = df['date'].dt.day_name()
df['month'] = df['date'].dt.month
df['week'] = df['date'].dt.isocalendar().week
```

### Visualization
```python
# Bar chart
data.plot(kind='bar', color='steelblue')
plt.title('Title')
plt.xlabel('X')
plt.ylabel('Y')
plt.tight_layout()
plt.show()

# Line chart
data.plot(kind='line', marker='o', linewidth=2)

# Dashboard
fig, axes = plt.subplots(2, 2, figsize=(16, 10))
data.plot(ax=axes[0, 0])
```

### String Formatting
```python
f"{value:,.2f}"     # 1,234.56 (2 decimals, comma thousands)
f"{value:+.1f}%"    # +15.3% (show + sign)
f"{value:.0f}"      # 1234 (no decimals)
```

---

## Next Steps

### Upcoming: Day 6 - Data Cleaning
**Skills to learn:**
- Handling missing values (`.isnull()`, `.fillna()`, `.dropna()`)
- Fixing data types (`.astype()`, `pd.to_datetime()`)
- Removing duplicates (`.drop_duplicates()`)
- Text cleaning (`.str.replace()`, `.str.strip()`)

**Why it matters:**
Real-world data (like Lightspeed exports) is ALWAYS messy!

---

### Goal: Lightspeed POS Analysis
**Timeline:** 1-2 weeks

**Workflow:**
1. Export data from Lightspeed
2. Clean it (Day 6 skills)
3. Analyze it (Day 4 skills)
4. Visualize it (Day 5 skills)
5. Present insights to family business

**Impact:**
- Identify top-selling auto parts
- Optimize inventory levels
- Understand customer segments
- Track revenue trends
- Make data-driven business decisions

---

## Key Mindset Principles

1. **Problem → Metric → Code**
   - Understand the business question first
   - Identify the right metric to measure
   - Then write code to calculate it

2. **Quick Feedback > Perfectionism**
   - Try for 10-15 minutes
   - Ask for help if stuck
   - Iterate quickly

3. **Small Wins = Momentum**
   - Break large tasks into 15-20 min chunks
   - Celebrate each completion
   - Build confidence incrementally

4. **Resilience Through Adaptation**
   - Obstacles are learning opportunities
   - Find alternative paths
   - Never give up

5. **Code is a Tool, Thinking is the Skill**
   - 80% business thinking, 20% syntax
   - Understand WHY before HOW
   - Reference code patterns as needed

---

## Portfolio Highlights

**GitHub Repository:** `ronaldis87-max/data-analysis-practice`

**Completed Projects:**
1. Restaurant Sales Analysis (Days 1-2)
2. Retail Store Analytics Dashboard (Day 4)
   - Product performance
   - Customer segmentation  
   - Location comparison
   - Inventory optimization
3. Data Visualization Suite (Day 5)
   - 4-panel analytics dashboard
   - Bar charts, line charts
   - Professional formatting

**Skills Demonstrated:**
- Python/pandas proficiency
- Business strategy thinking
- Data visualization
- Git/GitHub workflow
- Professional documentation

---

## Resources

**Python/Pandas Learning:**
- Real Python (articles)
- Corey Schafer (YouTube)
- pandas documentation

**Practice Datasets:**
- Kaggle (real-world data)
- Your own Lightspeed exports

**Tools:**
- PyCharm (IDE)
- Git/GitHub (version control)
- matplotlib (visualization)

---

**Document Version:** 1.0  
**Last Updated:** Day 5 Complete  
**Next Review:** After Day 6 (Data Cleaning)
