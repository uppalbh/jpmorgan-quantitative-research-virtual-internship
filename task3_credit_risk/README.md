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
