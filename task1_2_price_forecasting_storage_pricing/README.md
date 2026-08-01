## Task 1: Natural Gas Price Forecasting

### Objective
Estimate natural gas prices for arbitrary historical and future dates.

### Approach
- Historical market data analysis
- Seasonal feature engineering
- Linear regression
- Sin/Cos periodic encoding
- Time extrapolation

### Features
- Date interpolation
- One-year extrapolation
- Seasonal trend modeling
- Price prediction API

## Task 2: Commodity Storage Contract Pricing

### Objective
Build a pricing engine for natural gas storage contracts.

### Inputs
- Injection dates
- Withdrawal dates
- Injection rate
- Withdrawal rate
- Storage capacity
- Storage cost
- Commodity prices

### Model
The contract value is computed as:

**Profit = Selling Value − Purchase Cost − Storage Costs**

While enforcing:
- Storage capacity constraints
- Injection limits
- Withdrawal limits
- Inventory consistency
