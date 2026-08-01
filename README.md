# JPMorgan Quantitative Research Virtual Internship

## Overview

This repository contains my solutions to the JPMorgan Chase Quantitative Research Virtual Experience Program through Forage.
The internship focused on solving real-world quantitative finance and risk management problems commonly encountered by quantitative researchers and financial engineers.
Throughout the program, I worked on:
- Commodity price forecasting
- Natural gas storage contract valuation
- Credit risk modeling
- Probability of Default estimation
- Expected Loss calculation
- Dynamic Programming for optimal FICO score bucketing
The implementation combines quantitative finance, machine learning, statistics, optimization, and Python programming.

## Project Workflow

```
Historical Market Data
        │
        ▼
Price Forecasting
        │
        ▼
Storage Contract Pricing
        │
        ▼
Credit Risk Modeling
        │
        ▼
Probability of Default
        │
        ▼
Expected Loss Estimation
        │
        ▼
Dynamic Programming for FICO Quantization
```

## Skills Demonstrated
- Quantitative Research
- Financial Engineering
- Derivative Pricing
- Commodity Markets
- Machine Learning
- Credit Risk Analytics
- Dynamic Programming
- Optimization
- Statistical Modeling
- Data Visualization
- Python

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-Learn
- XGBoost
- Matplotlib
- Seaborn
- Dynamic Programming
- Linear Regression
- Logistic Regression
- Random Forest
- Decision Trees

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

## Task 3: Credit Risk Analysis

### Objective
Predict Probability of Default (PD) for retail loans.

### Models Compared
- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

### Pipeline
```
Loan Data
    ↓
Feature Scaling
    ↓
Train / Validation / Test Split
    ↓
Model Training
    ↓
Cross Validation
    ↓
PD Prediction
    ↓
Expected Loss
```

### Expected Loss
Assuming:
- Recovery Rate = 10%
- Loss Given Default (LGD) = 1 − Recovery Rate

**Expected Loss = PD × LGD × Exposure**

## Task 4: Optimal FICO Score Bucketing

### Objective
Convert continuous FICO scores into optimal categorical credit ratings.

### Method
Implemented Dynamic Programming to maximize bucket log-likelihood.

The algorithm computes:
- Prefix sums
- Bucket likelihood
- DP optimization
- Boundary reconstruction

This approach is more statistically rigorous than using arbitrary bucket intervals.

## Algorithms Used

| Task | Algorithm |
|------|-----------|
| Forecasting | Linear Regression |
| Pricing | Cash Flow Simulation |
| Credit Risk | Logistic Regression |
| Comparison | Decision Tree |
| Comparison | Random Forest |
| Comparison | XGBoost |
| Quantization | Dynamic Programming |

## Repository Highlights

- Commodity forecasting
- Derivative pricing
- Credit risk analytics
- Machine learning
- Dynamic programming
- Financial modeling
- Model evaluation

## Results

- Seasonal gas price forecasting model
- Flexible storage contract pricing engine
- PD prediction framework
- Expected Loss calculator
- Optimal FICO bucket generation using DP

## Future Improvements

- Geometric Brownian Motion forecasting
- ARIMA / Prophet implementation
- Monte Carlo commodity pricing
- Black-Scholes extensions
- Gradient Boosting PD models
- SHAP explainability
- Portfolio Expected Loss
- LGD & EAD estimation
- Basel III capital calculations

## Author

Bhrigu Uppal
Duke University
Computer Science

Interested in:
- Quantitative Research
- Machine Learning
- Quantitative Trading
- Financial Engineering
