import pandas as pd
#display setting
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
#load Data
df = pd.read_csv('restaurant_sales.csv')
df['date'] = pd.to_datetime(df['date'])
df['revenue'] = df['price'] * df['quantity']

print("=" * 60)
print("DAY 3: TIME-BASED ANALYSIS")
print("=" * 60)
print()
# ============================================
# CHALLENGE 1A: Extract Time Components
# ============================================
print("📅 CHALLENGE 1A: Extract Time Components\n")
df['day_of_month'] = df['date'].dt.day
df['day_name'] = df['date'].dt.day_name()
df['week_number'] = df['date'].dt.isocalendar().week
# Order days properly
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df['day_name'] = pd.Categorical(df['day_name'], categories=day_order, ordered=True)
print("First 10 rows with time components:")
print(df[['date', 'item_name', 'revenue', 'day_name', 'week_number', 'day_of_month']].head(10))
print()
print("✅ Challenge 1A Complete!")
# ============================================
# CHALLENGE 1B: Group by Day of Week
# ============================================
print("\n📊 CHALLENGE 1B: Group by Day of Week\n")
#revenue by day of week
revenue_weekday = df.groupby('day_name')['revenue'].sum()
print("Revenue by day of week:")
print(revenue_weekday) #should i order the date early on in my code?
print()
#Find which day has highest revenue
highest_day = revenue_weekday.idxmax()
highest_day_value = revenue_weekday.max()
print(f"-{highest_day} is the highest revenue day with ${highest_day_value}")
print()
#Find which day has most transactions
daily_transactions = df.groupby('day_name')['revenue'].count()
most_trans = daily_transactions.idxmax()
most_trans_value = daily_transactions.max()
print(f"-{most_trans} with {most_trans_value} has the most transactions\n")
#Calculate average transaction value by day
avg_trans = df.groupby('day_name')['revenue'].mean()
print("Average transactions per day: ")
print(avg_trans.round(2))
print()
print("✅ Challenge 1B Complete!")
# ============================================
# CHALLENGE 2A: Revenue Trends
# ============================================
print("\n📈 CHALLENGE 2A: Revenue Trends Over Time\n")
#Calculate daily total revenue
daily_rev = df.groupby('date')['revenue'].sum()
daily_rev = daily_rev.sort_index() #was this line really needed? it seems to me that pandas keep it in order smallest to greatest date
print("Daily Revenue (First 10 days):")
print(daily_rev.head(10))
print()
best_day = daily_rev.idxmax()
best_day_value = daily_rev.max()
worst_day = daily_rev.idxmin()
worst_day_value = daily_rev.min()
print(f"-{best_day.date()} is the highest revenue day with ${best_day_value}")
print(f"-{worst_day.date()} is the lowest revenue day with ${worst_day_value}")
print()
#Calculate week-over-week growth
weekly_revenue = df.groupby('week_number')['revenue'].sum()
print("Weekly Revenue:")
for week, revenue in weekly_revenue.items(): #when to use .index vs .items()
    print(f"Week {week}: ${revenue:.2f}")

for i in range(1, len(weekly_revenue)): #explain especially len
    current_week = weekly_revenue.iloc[i]
    previous_week = weekly_revenue.iloc[i-1]
    growth_rate = ((current_week-previous_week)/previous_week)*100
    print(f"Week {i} to Week {i+1} :{growth_rate:+.1f}%") # .1f i understand why the + in front is a novelty
# ============================================
# CHALLENGE 2B: Weekend vs Weekday
# ============================================
print("\n📊 CHALLENGE 2B: Weekend vs Weekday Analysis\n")
df['is_weekend'] = df['day_name'].isin(['Saturday', 'Sunday'])
print(df[['day_name', 'is_weekend']].head(5))
print()
weekend_df = df[df['is_weekend'] == True]
weekday_df = df[df['is_weekend'] == False]
#2. **Calculate total revenue:**
weekend_rev = weekend_df['revenue'].sum()
weekday_rev = weekday_df['revenue'].sum()
print(f"Weekend ")
weekend_count = weekend_df.nunique()
weekday_count = weekday_df.nunique()
