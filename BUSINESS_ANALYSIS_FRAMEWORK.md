# Business Analysis Framework for Retail/Auto Parts

## Strategic Analysis Template

### 1. Customer Segmentation Analysis

**Questions to Answer:**
- Who are our customer segments?
- What % of revenue does each generate?
- Which segments are most profitable?
- Which segments are most stable/fragile?
- What's the lifetime value by segment?

**Metrics to Calculate:**
- Total revenue by segment
- Average transaction value by segment
- Transaction count by segment
- Revenue percentage by segment
- Customer retention rate (if data available)

**Strategic Actions:**
- High value + Low loyalty = RISK → Retention programs
- High volume + Low value = VOLUME → Operational efficiency
- Low engagement = OPPORTUNITY → Activation campaigns

**Example Insights:**
- Walk-in customers: High revenue but fragile (no loyalty)
- Fleet customers: Lower frequency but high value per transaction
- Regular customers: Foundation of stable recurring revenue

**Recommendation Framework:**
IF segment_revenue > 30% AND loyalty_score < 5
THEN Priority = Convert to loyal customers
ACTION = Loyalty program, follow-up campaigns
IF segment_margin > 25% AND frequency < 2/month
THEN Priority = Increase purchase frequency
ACTION = Reminders, subscriptions, bundles
IF segment_revenue < 10% AND declining
THEN Priority = Evaluate discontinuation
ACTION = Cost-benefit analysis

---

### 2. Product Performance Analysis

**Questions to Answer:**
- Which products drive revenue?
- Which products are fast movers vs slow movers?
- What's the revenue per unit by product?
- Which products have best margins?
- Any products to discontinue?

**Metrics to Calculate:**
- Total revenue by product
- Total quantity sold by product
- Revenue per unit (revenue ÷ quantity)
- Inventory turnover rate
- Stock-out frequency

**Product Categories:**

**Fast Movers (High Volume):**
- Characteristics: Sold frequently, lower margins
- Strategy: Never stock out, competitive pricing, maintain availability
- Inventory: Higher stock levels, quick replenishment
- Examples: Oil filters, air filters, brake pads

**Slow Movers (Low Volume):**
- Characteristics: Infrequent sales, ties up capital
- Strategy: Reduce inventory, order on-demand
- Inventory: Minimal stock, longer lead times acceptable
- Examples: Specialty parts, seasonal items

**High Margin (Premium):**
- Characteristics: Higher price, good profit per sale
- Strategy: Train staff to upsell, ensure availability
- Marketing: Emphasize quality, warranty, peace of mind
- Examples: Batteries, premium tires

**Recommendation Framework:**
IF quantity_sold > median AND revenue_per_unit < median
THEN Category = Fast Mover (Volume)
ACTION = Stock 2x average, monitor stock-out rate
IF quantity_sold < 25th_percentile AND revenue < 25th_percentile
THEN Category = Discontinuation Candidate
ACTION = Analyze profitability, consider removal
IF revenue_per_unit > 75th_percentile
THEN Category = Premium Product
ACTION = Staff training, prominent placement
---

### 3. Location/Channel Performance

**Questions to Answer:**
- Which locations generate most revenue?
- What are operating costs by location?
- Which locations are most profitable (not just revenue!)?
- Different customer mixes by location?
- Should we expand, consolidate, or optimize?

**Metrics to Calculate:**
- Revenue by location
- Profit by location (revenue - costs)
- Revenue per square foot
- Customer traffic by location
- Average transaction by location

**Cost Considerations:**
- Rent/mortgage
- Utilities
- Staff wages (may vary by location)
- Security, insurance
- Maintenance

**Location Analysis Framework:**
Location A: High revenue, High costs → Check profit margin
Location B: Medium revenue, Low costs → May be most profitable!
Don't optimize for revenue alone!
Profit = Revenue - Costs
ROI = Profit / Investment

**Recommendation Framework:**
IF profit_margin > company_average AND growth_trend = positive
THEN Priority = Replicate this model
ACTION = Open similar location
IF revenue > company_average AND profit_margin < average
THEN Priority = Cost optimization
ACTION = Review rent, staffing, operations
IF declining_revenue AND high_costs
THEN Priority = Turnaround or exit
ACTION = 90-day improvement plan or close
---

### 4. Inventory Optimization

**Questions to Answer:**
- What's our inventory turnover rate?
- Which items are overstocked?
- Which items frequently stock out?
- What's the carrying cost of inventory?
- Optimal reorder points and quantities?

**Key Metrics:**
- Inventory turnover = Cost of Goods Sold ÷ Average Inventory
- Days of inventory = 365 ÷ Inventory Turnover
- Stock-out rate = (Days out of stock ÷ Total days) × 100
- Carrying cost = Storage + Insurance + Obsolescence + Capital cost

**ABC Analysis:**

**A Items (20% of products, 80% of revenue):**
- Strategy: Never stock out, tight monitoring
- Inventory: Higher safety stock
- Reorder: Frequent, automated

**B Items (30% of products, 15% of revenue):**
- Strategy: Moderate monitoring
- Inventory: Standard safety stock
- Reorder: Regular intervals

**C Items (50% of products, 5% of revenue):**
- Strategy: Minimal stock, order on-demand
- Inventory: Low or zero stock
- Reorder: When requested

**Seasonal Considerations:**
- Summer: Air conditioning parts, coolant
- Winter: Batteries (cold weather), antifreeze
- Year-round: Brake pads, oil filters

---

### 5. Trend Analysis (Time-Based)

**Questions to Answer:**
- Is revenue growing, declining, or stable?
- Are there seasonal patterns?
- Day-of-week patterns?
- Impact of promotions/events?
- Forecast for next period?

**Metrics to Calculate:**
- Week-over-week growth %
- Month-over-month growth %
- Year-over-year growth %
- Moving averages (smooth out noise)
- Trend line (overall direction)

**Pattern Recognition:**

**Growing Trend:**
- Positive: Business expanding
- Action: Prepare for scale (inventory, staff, space)

**Declining Trend:**
- Warning: Losing market share or seasonality
- Action: Investigate causes, corrective action

**Cyclical/Seasonal:**
- Pattern: Predictable ups and downs
- Action: Adjust inventory and staffing accordingly

**Volatile/Unstable:**
- Pattern: Large unpredictable swings
- Action: Investigate root causes, stabilize operations

---

## Real-World Application: Auto Parts Business

### Customer Segmentation in Auto Parts

**Typical Segments:**

**1. DIY Individual Customers**
- Characteristics: Weekend repairs, price-sensitive, need guidance
- Value: Moderate per transaction, sporadic frequency
- Strategy: Educational content, how-to guides, loyalty rewards

**2. Professional Mechanics**
- Characteristics: Bulk purchases, quality-focused, regular buyers
- Value: High volume, consistent revenue
- Strategy: Trade accounts, volume discounts, priority service

**3. Fleet Operators** 
- Characteristics: Large orders, scheduled maintenance
- Value: Highest per transaction, predictable schedule
- Strategy: Contracts, dedicated account manager, just-in-time delivery

**4. Walk-in Emergency**
- Characteristics: Urgent need, less price-sensitive
- Value: Moderate-high per transaction, one-time
- Strategy: Fast service, convert to regular with follow-up

---

### Product Mix in Auto Parts

**Fast Movers:**
- Oil filters, air filters
- Brake pads, brake fluid
- Wiper blades
- Spark plugs
- Strategy: Never stock out, competitive pricing

**Slow Movers:**
- Specialty gaskets
- Rare model parts
- Seasonal items (snow tires in warm climate)
- Strategy: Minimal inventory, order on-demand

**High Margin:**
- Batteries
- Premium brake systems
- Performance parts
- Strategy: Staff training, upsell opportunities

---

### Seasonal Patterns in Auto Parts

**Summer (May-August):**
- High demand: Air conditioning parts, coolant, radiators
- Road trips: Tires, alignment, fluids
- Strategy: Stock up on cooling system parts

**Winter (November-February):**
- High demand: Batteries (cold weather failure), antifreeze
- Weather-related: Wiper blades, de-icer, heating systems
- Strategy: Battery testing promotions, winter prep packages

**Spring/Fall (Transition):**
- Maintenance season: Oil changes, tune-ups
- Vehicle prep: Pre-summer and pre-winter checks
- Strategy: Maintenance bundles, inspection services

---

## Decision-Making Framework

### When to Stock More
✅ Fast mover (high quantity sold)
✅ High margin (profitable per unit)
✅ Low stock-out tolerance (customers expect availability)
✅ Seasonal peak approaching
✅ Supplier lead time is long
ACTION: Increase safety stock by 50-100%

### When to Stock Less
✅ Slow mover (low quantity sold)
✅ High carrying cost (expensive to store)
✅ Short supplier lead time (can reorder quickly)
✅ Declining demand trend
✅ Approaching obsolescence (model year change)
ACTION: Reduce to 2-week supply or discontinue

### When to Promote/Market
✅ High margin item
✅ Seasonal opportunity (winter batteries)
✅ Excess inventory (need to move)
✅ New product launch
✅ Competitive advantage (exclusive item)
ACTION: Email campaign, in-store signage, bundle deals

### When to Discontinue
✅ Sales declining for 3+ months
✅ Supplier discontinued or unreliable
✅ Better alternative available
✅ Negative profit margin
✅ Regulatory/safety concerns
ACTION: Clearance sale, then remove from catalog

---

## Key Performance Indicators (KPIs)

### Revenue KPIs
- Total revenue (monthly, quarterly, yearly)
- Revenue per customer segment
- Revenue per location
- Revenue per product category
- Revenue per square foot (retail space efficiency)

### Profitability KPIs
- Gross margin % (by product, category, overall)
- Net profit margin %
- Profit per transaction
- Profit per customer

### Operational KPIs
- Inventory turnover ratio (target: 6-12x per year for auto parts)
- Stock-out rate (target: <2%)
- Average transaction value
- Transactions per day
- Revenue per employee

### Customer KPIs
- Customer retention rate
- Customer acquisition cost
- Repeat purchase rate
- Average customer lifetime value

### Growth KPIs
- Month-over-month growth %
- Year-over-year growth %
- New customer growth rate
- Market share (if data available)

---

## Data-Driven Culture Principles

### 1. Measure Everything
- If you can't measure it, you can't improve it
- Track KPIs consistently
- Regular reporting cadence

### 2. Question Assumptions
- "We've always done it this way" ← RED FLAG
- Test hypotheses with data
- A/B test when possible

### 3. Act on Insights
- Analysis without action = wasted effort
- Set clear success metrics
- Review results, iterate

### 4. Democratize Data
- Share insights with team
- Train staff on key metrics
- Celebrate data-driven wins

### 5. Balance Data with Intuition
- Data shows WHAT happened
- Experience/intuition explains WHY
- Both are needed for good decisions

---

**Document End**
