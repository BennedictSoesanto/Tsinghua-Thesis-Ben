import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, OrdinalEncoder, LabelEncoder
import xgboost as xgb
from xgboost import XGBClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# Step 1: Load dataset
df = pd.read_csv("final_cleaned.csv")

# Step 2: Define categorical, binary, and continuous variables
categorical_cols = [
    "BAC3",  # Estimated income (1, 2, 3, 4 categories)
    "BAC4",  # Education level (1, 2, 3, 4, 5 categories)
    "BAC6", # Commodity (1-16 categories)
    "BAC8"   # Province (1, 2, 3, 4 based on region)
]
binary_cols = [
    "IMP2",   # Binary 1 or 0 - valid from chi squared test
    "COM1_5", # Binary 1 or 0 - valid from chi squared test
    "BAC5",    # Access to smartphone? (binary 1 or 0)
    "BAC7"  # Access to agricultural services (Yes/No)
]
numeric_cols = [
    "BAC1",  # Age (value)
    "BAC2"   # Land size (value)
]

# Ordinal Likert scale dependent variable
y_col = "MAD1"

# Step 3: Handle missing data

# Independent variables (features)
X_cols = ["MAD3_1", "MAD3_2", "MAD3_3", "MAD3_4", "MAD3_5", 
    "MAD4", "INO1_1", "INO1_2", "INO1_3", "INO1_4", "INO1_5",
    "COM2_1", "COM2_2", "COM2_3", "COM2_4", "OUT1_1", "OUT1_2", 
    "OUT1_3", "ADO2", "ADO3", "SRI1", "SRI2", "ASI1_1", "ASI1_2",
    "ASI1_3", "BAC1", "BAC2", "BAC3", "BAC4", "BAC6", "BAC8",
    "IMP2", "COM1_5", "BAC5", "BAC7"]

df = df.dropna(subset=[y_col] + X_cols)

# Step 4: Adjust Likert scale variables (1-5 range) to be 0-4, except IMP1_1, IMP1_2, IMP1_3 (0-5 range)
likert_1_5_cols = [
    "MAD3_1", "MAD3_2", "MAD3_3", "MAD3_4", "MAD3_5", 
    "MAD4", "INO1_1", "INO1_2", "INO1_3", "INO1_4", "INO1_5",
    "COM2_1", "COM2_2", "COM2_3", "COM2_4", "OUT1_1", "OUT1_2", 
    "OUT1_3", "ADO2", "ADO3", "SRI1", "SRI2", "ASI1_1", "ASI1_2", "ASI1_3"
]
df[likert_1_5_cols] = df[likert_1_5_cols] - 1  # Shifting 1-5 to 0-4

# No adjustment needed for IMP1_1, IMP1_2, IMP1_3
imp1_cols = ["IMP1_1", "IMP1_2", "IMP1_3"]

# Step 5: Encode categorical variables using OrdinalEncoder
encoder = OrdinalEncoder()
df[categorical_cols] = encoder.fit_transform(df[categorical_cols])

# Step 6: Encode binary columns (IMP2, COM1_5, BAC5) if they are not already 0/1
label_encoder = LabelEncoder()
for col in binary_cols:
    df[col] = label_encoder.fit_transform(df[col])

# Step 7: Normalize numerical columns
custom_scaler = MinMaxScaler(feature_range=(18, 88))
df[['BAC1']] = custom_scaler.fit_transform(df[['BAC1']])
custom_scaler = MinMaxScaler(feature_range=(0.2, 20))
df[['BAC2']] = custom_scaler.fit_transform(df[['BAC2']])

# Step 8: Adjust the target variable 'MAD1' (Likert scale 1-5 to 0-4)
df['MAD1'] = df['MAD1'] - 1  # Shift target variable to 0-4

# Step 9: Define Features (X) and Target (y)
X = df[X_cols]
y = df[y_col]

print(X)

# Step 10: Initialize the XGBoost model
model = XGBClassifier(objective="multi:softmax", num_class=len(np.unique(y)), eval_metric="mlogloss", 
                      max_depth=4, min_child_weight=5, gamma=1)

# Step 11: Perform cross-validation (e.g., 5-fold cross-validation)
cv_scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')

# Step 12: Print cross-validation results
print(f"Cross-validation scores: {cv_scores}")
print(f"Mean cross-validation accuracy: {np.mean(cv_scores):.4f}")
print(f"Standard deviation of cross-validation accuracy: {np.std(cv_scores):.4f}")

# Step 13: Train the model using the entire dataset (since cross-validation is done)
model.fit(X, y)

# Step 14: Make predictions (optional if you want to evaluate a final model)
y_pred = model.predict(X)

# Step 15: Evaluate the model (optional)
accuracy = accuracy_score(y, y_pred)
print(f"Final Accuracy: {accuracy:.4f}")

# Confusion Matrix (optional)
cm = confusion_matrix(y, y_pred)

# Get unique values of the target variable (y) for x and y axis labels
classes = np.unique(y)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=classes, yticklabels=classes)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("confusion_matrix.png", bbox_inches="tight", dpi=1000)
plt.show()

# Classification Report
report = classification_report(y, y_pred)
print("Classification Report:")
print(report)

# Feature Importance
plt.figure(figsize=(20, 40))
xgb.plot_importance(model, importance_type='weight', max_num_features=35)
plt.title("Feature Importance")
plt.subplots_adjust(left=0.2)
plt.savefig("feature_importance.png", bbox_inches="tight", dpi=1000)
plt.show()

"""
# Analyze MAD1 vs Component
plt.figure(figsize=(10, 6))
sns.boxplot(x='MAD1', y='BAC1', data=df)
plt.title("Age vs. Target Variable (MAD1)")
plt.show()
"""
