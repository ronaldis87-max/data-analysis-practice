# Common Python/Pandas Errors & Solutions

## Error 1: KeyError

**What you see:**
KeyError: 'column_name'

**What it means:**
Column doesn't exist in DataFrame

**Solution:**
```python
# Check column names first
print(df.columns)

# Use correct name
df['correct_column_name']
```

---

## Error 2: ModuleNotFoundError

**What you see:**
ModuleNotFoundError: No module named 'matplotlib'

**What it means:**
Package not installed in current Python environment

**Solution:**
```bash
# PyCharm: Use package manager (bottom-right → Settings → +)
# OR Terminal:
pip3 install matplotlib
```

---

## Error 3: TypeError with groupby

**What you see:**
TypeError: unsupported operand type(s) for /

**What it means:**
Trying math on non-numeric data

**Solution:**
```python
# Check data type
print(df['column'].dtype)

# Convert if needed
df['column'] = df['column'].astype(float)
```

---

## Error 4: AttributeError: 'DataFrame' object has no attribute

**What you see:**
AttributeError: 'DataFrame' object has no attribute 'dt'

**What it means:**
Using datetime method on non-datetime column

**Solution:**
```python
# Convert to datetime first
df['date'] = pd.to_datetime(df['date'])

# Then use .dt methods
df['date'].dt.day_name()
```

---

## Error 5: Matplotlib not displaying

**What you see:**
Code runs but no chart appears

**Solution:**
```python
# Add this at the end
plt.show()

# If still not working, try interactive mode
import matplotlib
matplotlib.use('TkAgg')  # Add at top of file
```

---

## Error 6: SettingWithCopyWarning

**What you see:**
SettingWithCopyWarning: A value is trying to be set on a copy

**Solution:**
```python
# Use .loc explicitly
df.loc[df['price'] > 100, 'category'] = 'Expensive'

# OR make explicit copy
filtered_df = df[df['price'] > 100].copy()
```

---

