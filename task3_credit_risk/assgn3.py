import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import math
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_curve, auc
from sklearn.preprocessing import LabelEncoder, StandardScaler
import seaborn as sns


# Models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier




df = pd.read_csv("./JPMorgan/task34.csv")
"""print(df.info())
print(df.shape)

print(df.head())
print(df.tail())"""
X = df.drop(columns= ["default", "customer_id"])
y = df["default"]

scalers = []
X_cols = ["credit_lines_outstanding", "loan_amt_outstanding", "total_debt_outstanding", "income",
          "years_employed", "fico_score"]
for col in X_cols:
    se = StandardScaler()
    X[col] = se.fit_transform(X[[col]]).ravel()
    scalers.append(se)

"""for col in X_cols:
    plt.figure(figsize=(6,4))
    sns.histplot(X[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.show()"""

X_train, X_temp, Y_train, Y_temp = train_test_split(X, y, train_size=0.6)
X_val, X_test, Y_val, Y_test = train_test_split(X_temp, Y_temp, train_size=0.5)

models = {
    "LogisticRegression" : LogisticRegression(random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "XGBoost": XGBClassifier(random_state=42)
}
cv_results = {}

for name, model in models.items():
    cv_scores = cross_val_score(model, X_train, Y_train, cv=5, scoring='accuracy')
    cv_results[name] = cv_scores
    print(f"{name} - CV Accuracy: {cv_scores.mean()}")
    print(f"CV Standard Deviation: {cv_scores.std()}")

final_model = LogisticRegression(random_state=42).fit(X_train, Y_train)
Y_train_pred = final_model.predict(X_train)
Y_val_pred = final_model.predict(X_val)
Y_test_pred = final_model.predict(X_test)
print(accuracy_score(Y_train_pred, Y_train))
print(accuracy_score(Y_val_pred, Y_val))
print(accuracy_score(Y_test_pred, Y_test))

RECOVERY_RATE = 0.10
LGD = 1 - RECOVERY_RATE
def expected_loss(model, borrower):
    borrower = borrower.drop(columns=["customer_id"]).copy()
    for i in range(len(X_cols)):
        borrower[X_cols[i]] = scalers[i].transform(borrower[[X_cols[i]]]).ravel()
    pd = model.predict_proba(borrower)[0][1]
    exposure = borrower1["loan_amt_outstanding"].iloc[0] 
    return pd * LGD * exposure

borrower1 = pd.DataFrame({
    "customer_id": [100001],
    "credit_lines_outstanding": [3],
    "loan_amt_outstanding": [25000],
    "total_debt_outstanding": [32000],
    "income": [50000],
    "years_employed": [6],
    "fico_score": [680]
})
loss = expected_loss(final_model, borrower1)
print(loss)

