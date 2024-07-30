# Anomaly Detection: Isolation Forest

from sklearn.ensemble import IsolationForest
import numpy as np

# Example data
X = np.array([[1], [2], [3], [4], [5], [100]])

model = IsolationForest(contamination=0.1)
model.fit(X)
predictions = model.predict(X)
print(predictions)
