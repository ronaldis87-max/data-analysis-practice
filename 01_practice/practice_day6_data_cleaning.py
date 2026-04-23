import pandas as pd
import numpy as np

print("=" * 60)
print("DAY 6: DATA CLEANING")
print("=" * 60)
print()

# Create messy retail data (realistic problems!)
messy_data = {
    'date': ['2024-01-15', '01/16/2024', '2024-01-17', None, '2024-01-19',
             '2024-01-20', 'INVALID', '2024-01-22', '2024-01-23', '2024-01-24'],

    'product': ['Brake Pads', None, 'Oil Filter', 'Spark Plugs', 'Battery',
                'Brake Pads', 'Wiper Blades', 'Oil Filter', 'Spark Plugs', 'Battery'],

    'price': [45.99, 39.99, 'MISSING', 12.50, 89.99,
              45.99, None, 15.50, 12.50, 89.99],

    'quantity': [2, None, 5, 3, 1,
                 2, 4, None, 3, 1],

    'customer_type': ['Regular', 'Walk-in', 'Fleet', 'Regular', None,
                      'Regular', 'Walk-in', 'Fleet', 'UNKNOWN', 'Regular'],

    'location': ['Downtown', 'Suburb', 'Downtown', 'Suburb', 'Downtown',
                 'Downtown', 'Suburb', 'Downtown', 'Suburb', 'Downtown']
}

df = pd.DataFrame(messy_data)

print("🚨 MESSY DATA LOADED!")
print(f"Total rows: {len(df)}")
print()
print("First look at the data:")
print(df)
print()
# ============================================
# CHALLENGE 6A: Detecting Data Problems
# ============================================
print("\n" + "=" * 60)
print("🔍 CHALLENGE 6A: Data Quality Report")
print("=" * 60)
print()

# TODO: Check data types
print("1️⃣ DATA TYPES:")
print(df.dtypes)
print()

# TODO: Count missing values
print("2️⃣ MISSING VALUES:")
missing_count = df.isnull().sum()
missing_percent = (df.isnull().sum() / len(df)) * 100

missing_report = pd.DataFrame({
    'Missing_Count': missing_count,
    'Missing_Percent': missing_percent
})
print(missing_report)
print()

# TODO: Check for 'MISSING' or 'UNKNOWN' text values
print("3️⃣ INVALID TEXT VALUES:")
# Check price column for text issues
if df['price'].dtype == 'object':  # If it's text instead of number
    print(f"⚠️ Price column is TEXT, not numbers!")
    print(f"Unique values: {df['price'].unique()}")
print()

# Check customer_type for invalid values
print("Customer types found:")
print(df['customer_type'].value_counts(dropna=False))
print()

# TODO: Summary statistics (shows problems in numbers)
print("4️⃣ SUMMARY STATISTICS:")
print(df.describe())
print()

# TODO: Total data quality score
total_cells = len(df) * len(df.columns)
missing_cells = df.isnull().sum().sum()
quality_score = ((total_cells - missing_cells) / total_cells) * 100

print("=" * 60)
print(f"📊 DATA QUALITY SCORE: {quality_score:.1f}%")
print(f"Total cells: {total_cells}")
print(f"Missing cells: {missing_cells}")
print(f"Clean cells: {total_cells - missing_cells}")
print("=" * 60)

print("\n✅ Challenge 6A Complete!")
# ============================================
# CHALLENGE 6B: Fixing Missing Values
# ============================================
print("\n" + "=" * 60)
print("🛠️ CHALLENGE 6B: Fixing the Data")
print("=" * 60)
print()

# Make a COPY to work with (keep original for comparison)
df_clean = df.copy()

print("BEFORE CLEANING:")
print(f"Missing values: {df_clean.isnull().sum().sum()}")
print()

# ──────────────────────────────────────────
# FIX 1: Handle 'MISSING' and 'UNKNOWN' text
# ──────────────────────────────────────────
print("🔧 FIX 1: Replace invalid text with NaN")

# Replace 'MISSING' in price with NaN
df_clean['price'] = df_clean['price'].replace('MISSING', np.nan)

# Replace 'UNKNOWN' in customer_type with NaN
df_clean['customer_type'] = df_clean['customer_type'].replace('UNKNOWN', np.nan)

# Replace 'INVALID' in date with NaN
df_clean['date'] = df_clean['date'].replace('INVALID', np.nan)

print("✅ Invalid text replaced with NaN")
print(f"Missing values now: {df_clean.isnull().sum().sum()}")
print()

# ──────────────────────────────────────────
# FIX 2: Fill missing customer_type
# ──────────────────────────────────────────
print("🔧 FIX 2: Fill missing customer_type")

# Strategy: Fill with most common value
most_common_customer = df_clean['customer_type'].mode()[0]
df_clean['customer_type'] = df_clean['customer_type'].fillna(most_common_customer)

print(f"✅ Filled missing customer_type with: {most_common_customer}")
print(f"Missing values now: {df_clean.isnull().sum().sum()}")
print()

# ──────────────────────────────────────────
# FIX 3: Fill missing product names
# ──────────────────────────────────────────
print("🔧 FIX 3: Fill missing product names")

# Strategy: Fill with a placeholder
df_clean['product'] = df_clean['product'].fillna('Unknown Product')

print("✅ Filled missing products with 'Unknown Product'")
print(f"Missing values now: {df_clean.isnull().sum().sum()}")
print()

# ──────────────────────────────────────────
# FIX 4: Convert price to numeric
# ──────────────────────────────────────────
print("🔧 FIX 4: Convert price to numbers")

# Convert price from text to float
df_clean['price'] = pd.to_numeric(df_clean['price'], errors='coerce')

# Fill missing prices with median price
median_price = df_clean['price'].median()
df_clean['price'] = df_clean['price'].fillna(median_price)

print(f"✅ Price converted to numbers, filled missing with median: ${median_price:.2f}")
print(f"Missing values now: {df_clean.isnull().sum().sum()}")
print()

# ──────────────────────────────────────────
# FIX 5: Fill missing quantity
# ──────────────────────────────────────────
print("🔧 FIX 5: Fill missing quantity")

# Strategy: Fill with median (middle value)
median_qty = df_clean['quantity'].median()
df_clean['quantity'] = df_clean['quantity'].fillna(median_qty)

print(f"✅ Filled missing quantity with median: {median_qty}")
print(f"Missing values now: {df_clean.isnull().sum().sum()}")
print()

# ──────────────────────────────────────────
# FIX 6: Fix dates and drop unfixable rows
# ──────────────────────────────────────────
print("🔧 FIX 6: Fix date formats")

# Convert to datetime (handles different formats automatically!)
df_clean['date'] = pd.to_datetime(df_clean['date'], errors='coerce')

# Count how many dates couldn't be parsed
invalid_dates = df_clean['date'].isnull().sum()
print(f"⚠️ Found {invalid_dates} invalid dates")

# Decision: Drop rows with invalid dates (can't fix them!)
if invalid_dates > 0:
    print(f"🗑️ Dropping {invalid_dates} rows with invalid dates...")
    df_clean = df_clean.dropna(subset=['date'])
    print(f"✅ Rows remaining: {len(df_clean)}")
print()

# ──────────────────────────────────────────
# FINAL CHECK
# ──────────────────────────────────────────
print("=" * 60)
print("📊 FINAL DATA QUALITY CHECK")
print("=" * 60)
print()

print("Missing values per column:")
print(df_clean.isnull().sum())
print()

print("Data types:")
print(df_clean.dtypes)
print()

# Calculate final quality score
total_cells_clean = len(df_clean) * len(df_clean.columns)
missing_cells_clean = df_clean.isnull().sum().sum()
quality_score_clean = ((total_cells_clean - missing_cells_clean) / total_cells_clean) * 100

print(f"✅ BEFORE: {len(df)} rows, {quality_score:.1f}% quality")
print(f"✅ AFTER:  {len(df_clean)} rows, {quality_score_clean:.1f}% quality")
print()

print("Clean data preview:")
print(df_clean)
print()

print("✅ Challenge 6B Complete!")
# ============================================
# CHALLENGE 6C: Export Clean Data
# ============================================
print("\n" + "=" * 60)
print("📤 CHALLENGE 6C: Export Clean Data")
print("=" * 60)
print()

# Create exports folder if needed
import os

if not os.path.exists('exports'):
    os.makedirs('exports')

# Export 1: Clean data CSV
df_clean.to_csv('exports/cleaned_data.csv', index=False)
print("✅ Exported: exports/cleaned_data.csv")

# Export 2: Data cleaning report
with open('exports/data_cleaning_report.txt', 'w') as f:
    f.write("=" * 60 + "\n")
    f.write("DATA CLEANING REPORT\n")
    f.write("=" * 60 + "\n\n")

    f.write(f"Original Data:\n")
    f.write(f"  Rows: {len(df)}\n")
    f.write(f"  Missing cells: {df.isnull().sum().sum()}\n")
    f.write(f"  Quality score: {quality_score:.1f}%\n\n")

    f.write(f"Cleaned Data:\n")
    f.write(f"  Rows: {len(df_clean)}\n")
    f.write(f"  Missing cells: {df_clean.isnull().sum().sum()}\n")
    f.write(f"  Quality score: {quality_score_clean:.1f}%\n\n")

    f.write(f"Actions Taken:\n")
    f.write(f"  1. Replaced 'MISSING' and 'UNKNOWN' with NaN\n")
    f.write(f"  2. Filled missing customer_type with most common: {most_common_customer}\n")
    f.write(f"  3. Filled missing products with 'Unknown Product'\n")
    f.write(f"  4. Converted price to numeric, filled with median: ${median_price:.2f}\n")
    f.write(f"  5. Filled missing quantity with median: {median_qty}\n")
    f.write(f"  6. Dropped {len(df) - len(df_clean)} rows with invalid dates\n\n")

    f.write(f"Result:\n")
    f.write(f"  ✅ Data is now 100% clean and ready for analysis!\n")

print("✅ Exported: exports/data_cleaning_report.txt")
print()

# Export 3: Before/After comparison
comparison = pd.DataFrame({
    'Metric': ['Total Rows', 'Missing Cells', 'Quality Score'],
    'Before': [len(df), df.isnull().sum().sum(), f"{quality_score:.1f}%"],
    'After': [len(df_clean), df_clean.isnull().sum().sum(), f"{quality_score_clean:.1f}%"],
    'Change': [
        f"{len(df_clean) - len(df):+d}",
        f"{df_clean.isnull().sum().sum() - df.isnull().sum().sum():+d}",
        f"{quality_score_clean - quality_score:+.1f}%"
    ]
})

comparison.to_csv('exports/cleaning_comparison.csv', index=False)
print("✅ Exported: exports/cleaning_comparison.csv")

print()
print("📁 All exports saved to 'exports/' folder!")
print()

print("✅ Challenge 6C Complete!")
print()
print("=" * 60)
print("🎉 DAY 6 COMPLETE - Data Cleaning Mastered!")
print("=" * 60)