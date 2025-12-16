import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Hours
y = np.array([2, 3, 5, 4, 6])                # Scores

# Fit linear regression
model = LinearRegression()
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# Plot
plt.scatter(X, y, color='blue')         # Original points
plt.plot(X, y_pred, color='red')        # Regression line
plt.xlabel('Hours')
plt.ylabel('Score')
plt.show()
