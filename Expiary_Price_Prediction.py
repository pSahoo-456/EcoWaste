import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.multioutput import MultiOutputRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

#Load clean dataset
df = pd.read_csv("expiry_price_data.csv")

# Encode categorical features
product_encoder = LabelEncoder()
brand_encoder = LabelEncoder()
usage_encoder = LabelEncoder()

df['Product_Type'] = product_encoder.fit_transform(df['Product_Type'])
df['Brand'] = brand_encoder.fit_transform(df['Brand'])
df['Usage_Pattern'] = usage_encoder.fit_transform(df['Usage_Pattern'])

# Define Features & Targets
X = df.drop(columns=['Expiry_Years', 'Current_Price'])  # Features
y = df[['Expiry_Years', 'Current_Price']]  # Targets (Two Outputs)

# Improve Data Splitting (Shuffling for randomness)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)

# Fix Overfitting by Tweaking Hyperparameters
model = MultiOutputRegressor(XGBRegressor(
    n_estimators=150,  
    learning_rate=0.1,  # Increase learning rate (prevents memorization)
    max_depth=4,  # Reduce depth (prevent deep memorization)
    subsample=0.8,  # Train on 80% of data per iteration (prevent overfitting)
    colsample_bytree=0.7,  # Train on 70% of features per tree (diversify learning)
    reg_lambda=5,  # Add L2 regularization (prevent large weights)
    reg_alpha=1,  # Add L1 regularization (prevent model complexity)
    random_state=42
))
model.fit(X_train, y_train)

# Predict on Test Data
y_pred = model.predict(X_test)

# Evaluate Model
mae = mean_absolute_error(y_test, y_pred, multioutput='raw_values')
rmse = np.sqrt(mean_squared_error(y_test, y_pred, multioutput='raw_values'))
r2 = r2_score(y_test, y_pred, multioutput='raw_values')

print(f"Fixed Model Performance:")
print(f"Expiry Prediction - MAE: {mae[0]:.2f} years, RMSE: {rmse[0]:.2f}, R²: {r2[0]:.3f}")
print(f"Price Prediction - MAE: ₹{mae[1]:.2f}, RMSE: ₹{rmse[1]:.2f}, R²: {r2[1]:.3f}")

# Save Fixed Model & Encoders
joblib.dump(model, "fixed_multi_output_model.pkl")
joblib.dump(product_encoder, "product_encoder.pkl")
joblib.dump(brand_encoder, "brand_encoder.pkl")
joblib.dump(usage_encoder, "usage_encoder.pkl")

print("Fixed Model & Encoders Saved Successfully!")

