# Data Analysis Practice

Python data analysis journey - from beginner to business analyst.

**Portfolio:** [github.com/ronaldis87-max/data-analysis-practice](https://github.com/ronaldis87-max/data-analysis-practice)

---

## 📚 Project Structure

### 01_practice/ - Learning Exercises
Foundation training with sample datasets (restaurant & retail).

**Completed:**
- Days 1-3: Restaurant sales analysis
- Day 4: Retail analytics & business strategy
- Day 5: Data visualization & dashboards
- Day 6: Data cleaning techniques

**Skills:** pandas, matplotlib, groupby, pivot tables, data cleaning, strategic analysis

---

### 02_lightspeed/ - Real Business Analysis (IN PROGRESS)
Production analysis of family auto parts business using Lightspeed POS data.

**Structure:**
- `data/raw/` - Original Lightspeed exports (private, not committed)
- `data/cleaned/` - Cleaned datasets ready for analysis
- `analysis/` - Python analysis scripts
- `exports/` - Business reports and summaries
- `reports/` - Strategic recommendations

**Objectives:**
1. Identify top-performing products
2. Optimize inventory (fast vs slow movers)
3. Analyze customer segments
4. Detect seasonal trends
5. Generate actionable business insights

---

### docs/ - Reference Documentation
- Learning reference guide
- Business analysis frameworks
- Common errors & solutions

---

## 🎯 Previous Work

# Data Analysis Practice

Python data analysis learning journey - from beginner to business analyst.

## 📊 Day 4: Retail Store Analysis

**Dataset:** 30 days of auto parts retail sales data (679 transactions)

**Analysis Completed:**

### Challenge 1A: Product Performance
- Identified top 5 revenue-generating products
- Analyzed sales volume vs revenue patterns
- Found highest margin items

### Challenge 1B: Customer Segmentation
- Analyzed 3 customer types: Fleet, Regular, Walk-in
- Walk-in customers = 35.7% of revenue (highest risk!)
- **Strategic Recommendation:** Convert Walk-ins to Regulars via loyalty program
- Projected impact: Secure $19,512 in recurring revenue

### Challenge 2A: Location Performance
- Compared Downtown vs Suburb locations
- Both locations perform equally (~50% revenue each)
- **Strategic Recommendation:** Open new Suburb location in underserved south region
- Lower operating costs + geographic expansion opportunity

### Challenge 2B: Inventory Management
- Identified fast movers (stock more) vs slow movers (stock less)
- Analyzed revenue per unit for pricing strategy
- Category analysis: Fluids & Filters dominates volume
- **Key Insight:** High-volume items need availability, high-margin items need promotion

## 📁 Exports

All analysis summaries available in `exports/` folder:
- `product_performance.csv` - Product rankings by revenue/quantity
- `customer_segmentation.csv` - Customer type analysis
- `location_performance.csv` - Downtown vs Suburb comparison
- `category_analysis.csv` - Category-level insights
- `inventory_recommendations.csv` - Stock more/less recommendations

## 🛠️ Technologies

- Python 3
- pandas
- NumPy

## 📚 Skills Demonstrated

- Data grouping and aggregation
- Multi-dimensional analysis
- Customer segmentation
- Business strategy recommendations
- Data export and reporting