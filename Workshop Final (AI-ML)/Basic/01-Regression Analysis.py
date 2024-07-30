# Predictive Analytics: Regression Analysis

from sklearn.linear_model import LinearRegression
import pandas as pd

# Example data
data = pd.DataFrame({
    'feature': [1, 2, 3, 4, 5],
    'target': [2, 4, 5, 4, 5]
})

X = data[['feature']]
y = data['target']

model = LinearRegression()
model.fit(X, y)

# Predict future values
predictions = model.predict([[6]])
print(predictions)
