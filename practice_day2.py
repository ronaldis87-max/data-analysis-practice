from itertools import combinations

import pandas as pd
#display setting
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

#load data
df = pd.read_csv('restaurant_sales.csv')
df['date'] = pd.to_datetime(df['date'])
df['revenue'] = df['price'] * df['quantity']
print("=" * 60)
print("DAY 2: MULTI-LEVEL ANALYSIS")
print("=" * 60)
print()
print(f"✅ Loaded {len(df)} transactions ")
print(f"📅 Period: {df['date'].min().date()} to {df['date'].max().date()}")
print()
# ============================================
# CHALLENGE 1: Multi-Level Grouping
# ============================================
print("📊 CHALLENGE 1: Multi-Level Grouping\n")
#1A. Revenue by Meal Type AND Category
print("1A. Revenue by Meal Type & Category:")
rev_meal_cat = df.groupby(['meal_type','category'])['revenue'].sum().unstack()
#the loop way i was stuck here because unlike before i needed to loop through 2 value, found the answer through google
for meal in rev_meal_cat.index:
    for cat in rev_meal_cat.columns:
        rev = rev_meal_cat.loc[meal, cat]
        print(f"{meal} -> {cat}: ${rev}")
print()
print("The Stacked way")
# I usually use the for loop, now i found out a second way! Stacking, the apprentice looking for his own style :)
stack_meal_cat = rev_meal_cat.stack()
for (meal,cat), rev in stack_meal_cat.items(): #what blows my mind is how does it know meal refers to meal_type and cat category problably the format of syntax...
    print(f"{meal} -> {cat}: ${rev}")
print()
#1B. Server Performance by Meal Type
print("1B. Server Performance by Meal Type:")
rev_server_meal = df.groupby(['server', 'meal_type'])['revenue'].sum().unstack()
# Revenue by server AND meal_type
stack_server_meal = rev_server_meal.stack()
for (server, meal), rev in stack_server_meal.items():
    print(f"{server} -> {meal}: ${rev}")
# Find each server's best meal type
best = stack_server_meal.groupby(level=0).idxmax() #would need master explanations
best_meal = stack_server_meal[best]
for server, revenue in best_meal.items():
    print(f"{server} -> ${revenue}")
print()
#Show total revenue per server-meal combination
print("Total Revenue by Server & Meal Type:")
for (server, meal), revenue in stack_server_meal.items():
    print(f"{server} at {meal}: ${revenue:.2f}")
#1C. Average Transaction by Payment Method AND Meal Type
print("1C. Payment Method × Meal Type Analysis:")
avg_pay_meal = df.groupby(['payment_method', 'meal_type'])['revenue'].mean().unstack()
print(avg_pay_meal)
dinner_avg = avg_pay_meal['Dinner']
print("Average Dinner Transaction by Payment Method:")
for payment in dinner_avg.index:
    avg_payment = dinner_avg[payment]
    print(f"{payment}: ${avg_payment:.2f}")
print()
#Do mobile payers spend more at dinner?
mobile_dinner = avg_pay_meal.loc['Mobile', 'Dinner']
overall_dinner_avg = df[df['meal_type'] == 'Dinner']['revenue'].mean()
print(f"\nMobile at dinner: ${mobile_dinner:.2f}")
print(f"Overall dinner Average: ${overall_dinner_avg:.2f}")
if mobile_dinner > overall_dinner_avg:
    print("✅ Yes, mobile payers spend MORE at dinner!")
else:
    print("❌ No, mobile payers spend LESS at dinner")
# ============================================
# CHALLENGE 2: Pivot Tables
# ============================================
print("📊 CHALLENGE 2: Pivot Tables\n")
#2A. Category × Meal Type Revenue Matrix
cat_meal_pivot = df.pivot_table(
    index='category',
    columns='meal_type',
    values='revenue',
    aggfunc=sum,
)
print(cat_meal_pivot)
#Which category-meal combo generates most revenue?
stacked_meal_pivot = cat_meal_pivot.stack()
highest_combo_rev = stacked_meal_pivot.max()
highest_combo = stacked_meal_pivot.idxmax()
print(f"\nThe {highest_combo} Combo generates the most revenue with ${highest_combo_rev}")
#Do desserts sell better at dinner or lunch?
dessert_dinner = cat_meal_pivot.loc['Dessert', 'Dinner']
dessert_lunch = cat_meal_pivot.loc['Dessert', 'Lunch']
if dessert_dinner > dessert_lunch:
    print("✅ Yes, Dessert sells MORE at dinner!")
else:
    print("❌ No, Dessert sells Less at dinner!")
#Which category is most consistent across meals?
cat_dev = cat_meal_pivot.std(axis=1)
#consistency report
consistency = cat_dev.sort_values()
highest_dev = consistency.idxmin()
highest_dev_value = consistency.min()
print(f"The most consistent category is {highest_dev} with a standard deviation of ${highest_dev_value:.2f}")
# 2B: Server × Meal Type Performance
print("\n2B. Server Performance Matrix:")
server_meal_pivot = df.pivot_table(
    index='server',
    columns='meal_type',
    values='revenue',
    aggfunc=sum,
    margins=True,
) # you ask add margins? what do you mean?
print(server_meal_pivot)
#Which server is most balanced across meal types?
server_dev = server_meal_pivot.std(axis=1)
most_balanced = server_dev.idxmin()
most_balanced_value = server_dev.min()
print(f"The most balanced Server is {most_balanced} with a standard deviation of ${most_balanced_value:.2f}")
#Who's the dinner specialist?
dinner_specialist_rev = server_meal_pivot['Dinner'].max()
dinner_specialist = server_meal_pivot['Dinner'].idxmax()
print(f"The Dinner specialist is: {dinner_specialist} with ${dinner_specialist_rev:.2f}")
#Who needs to improve at breakfast?
worst_breakfast_rev = server_meal_pivot['Breakfast'].min()
worst_breakfast = server_meal_pivot['Breakfast'].idxmin()
print(f"{worst_breakfast} with ${worst_breakfast_rev:.2f} Needs to improve at breakfast")
print()
#2C. Payment Preferences Heatmap
meal_payment_pivot = df.pivot_table(
    index='meal_type',
    columns='payment_method',
    values='category',
    aggfunc='count',
    fill_value=0,
)
print(meal_payment_pivot)
#Is cash more common at breakfast?
breakfast_cash = meal_payment_pivot.loc['Breakfast', 'Cash']
breakfast_card = meal_payment_pivot.loc['Breakfast', 'Card']
breakfast_mobile = meal_payment_pivot.loc['Breakfast', 'Mobile']
if breakfast_cash > breakfast_mobile and breakfast_cash > breakfast_card: #this works because i'm comparing only three things but if i had 10 variables to check?
    print("✅ Yes, Cash is most common at breakfast!")
else:
    print("❌ No, Cash is not most common at breakfast!")
#Do dinner customers prefer cards?
dinner_cash = meal_payment_pivot.loc['Dinner', 'Cash']
dinner_card = meal_payment_pivot.loc['Dinner', 'Card']
dinner_mobile = meal_payment_pivot.loc['Dinner', 'Mobile']
if dinner_card > dinner_mobile and dinner_card > dinner_cash:
    print("✅ Yes, Card is most common at Dinner!")
else:
    print("❌ No, Card is not most common at Dinner!")
#Which payment method is most popular overall?
payment_total = meal_payment_pivot.sum() #Here i struggle a little bit sometimes the answer is simple but we overthink and make it complicated
most_popular = payment_total.idxmax()
most_popular_value = payment_total.max()
print(f"The most popular payment is {most_popular} with {most_popular_value} Transactions")
print()
# ============================================
# CHALLENGE 3: Advanced Multi-Metric
# ============================================
print("🔥 CHALLENGE 3: Multi-Metric Analysis\n")
pivot_server_meal = df.pivot_table(
    index='server',
    columns='meal_type',
    values='revenue',
    aggfunc=['sum', 'mean','count'],
    margins=True,
)
print(pivot_server_meal)
#3B. Category Deep Dive
pivot_cat_meal = df.pivot_table(
    index='category',
    columns='meal_type',
    values='revenue', # - Total revenue, - Total quantity sold, how to work with 2 differents values
    aggfunc=['sum', 'mean','count'],
    margins=True,
)
print(pivot_cat_meal)
#"Which server has highest average but lowest volume?"
overall_mean = pivot_server_meal[('mean', 'All')]
overall_count = pivot_server_meal[('count', 'All')]
efficiency = overall_mean/overall_count
most_efficient = efficiency.idxmax()
print(f"The most efficient server is {most_efficient}") #ok this i'm loving it i mean when i look at the questions, they are hard! i was thinking i will just rebuild what we work on but your questions forces me to do research and understand questions and meaning at higher level
#"Who makes their money from quantity vs quality?"
quantity_max = overall_count.drop('All').idxmax()
quantity_max_value = overall_count.drop('All').max()
print(f"{quantity_max} with {quantity_max_value} Transactions, makes their money from quantity") #how i can return the two servers at 222 they both have exact same numbers of transactions but i can print only one name, your questions uses plural so you want both names
#"What's each server's efficiency (revenue per transaction)
overall_revenue = pivot_server_meal[('sum', 'All')]
rev_trans_efficiency = overall_revenue/overall_count
print(rev_trans_efficiency.round(2))
print()
# ============================================
# CHALLENGE 4: Finding Patterns
# ============================================
print("🎯 CHALLENGE 4: Pattern Analysis\n")
#Best Combo: Which category-meal combination generates most revenue?
overall_revenue_cat_meal = pivot_cat_meal['sum']
cat_meal_high = overall_revenue_cat_meal.drop('All').idxmax()
print("The best combo is:")
print(cat_meal_high.drop('All'))
print()
#Server Specialization:
#First begin using a loop to slove this but All values creep in
for server in pivot_server_meal.index:
    best_server_meal = pivot_server_meal.loc[server].idxmax()
    best_server_meal_value = pivot_server_meal.loc[server].max()
    print(f"{server}, Specializes in {best_server_meal} with ${best_server_meal_value:.2f}")
#Solution found with Gemini help
filtered_pivot = pivot_server_meal.drop('All', axis=0)
revenue_only = filtered_pivot['sum'].drop('All', axis=1)
best_ser_meal = revenue_only.idxmax(axis=1)
best_ser_meal_value = revenue_only.max(axis=1)
for server in best_ser_meal.index:
    print(f"{server} specializes in {best_ser_meal[server]} with ${best_ser_meal_value[server]:.2f}")
#Underperformers:
cat_meal_low = overall_revenue_cat_meal.drop('All').idxmin()
print("The worst combo is:")
print(cat_meal_low.drop('All'))
print()
#Should the restaurant remove it from the menu? not sure how to answer that with a code but it return main course for each category which seems logical, we go in restaurant for main course everything else is upsell, imposible to drop it
#if cat_meal_low['category'] == 'Main Course':
    #print("❌ No,we can't remove it from me")
#else:
    #print("✅ Yes, we can look at the possibility of removing it")
#Payment Insights: What percentage of dinner sales are card payments?

