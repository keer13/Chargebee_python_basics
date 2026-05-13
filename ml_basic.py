-------Linear Regression-----------

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
# Example data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 3, 2, 5, 4])
# Create and train the model
model = LinearRegression()
model.fit(X, y)
# Make predictions
y_pred = model.predict(X)
# Output the coefficients and intercept
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)
# Plot the results
plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')
plt.xlabel("X")
plt.ylabel("y")
plt.title("Simple Linear Regression")
plt.show()


-------LOGISTIC REGRESSION-----------

import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
# Example data
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
# Create and train the model
model = LogisticRegression()
model.fit(X, y)
# Make predictions
y_pred = model.predict(X)
# Output the model parameters
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)
print("Predictions:", y_pred)
# Plot the results
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict_proba(X)[:, 1], color='red')
plt.xlabel("X")
plt.ylabel("Probability of Class 1")
plt.title("Simple Logistic Regression")
plt.show()


-------DECISION TREE-----------

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# Initialize the Decision Tree Classifier
clf = DecisionTreeClassifier()
# Train the classifier
clf.fit(X_train, y_train)
# Make predictions on the testing set
y_pred = clf.predict(X_test)
# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
# Optional: Visualize the decision tree (requires graphviz and matplotlib)
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)
plt.show()


-------overfitting-----------

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
# Generate some data
np.random.seed(0)
X = np.random.rand(20, 1) * 10
y = 2 * X ** 2 - 3 * X + np.random.randn(20, 1) * 10
# Fit a polynomial regression model
poly_features = PolynomialFeatures(degree=10)
X_poly = poly_features.fit_transform(X)
poly_reg_model = LinearRegression()
poly_reg_model.fit(X_poly, y)
# Predict using the polynomial model
X_fit = np.linspace(0, 10, 100).reshape(-1, 1)
X_fit_poly = poly_features.transform(X_fit)
y_fit = poly_reg_model.predict(X_fit_poly)
# Plot the results
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X_fit, y_fit, color='red', label='Polynomial Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title('Overfitting Example')
plt.show()


-----------Regularization---------------

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
# Generate some data
np.random.seed(0)
X = np.random.rand(20, 1) * 10
y = 2 * X ** 2 - 3 * X + np.random.randn(20, 1) * 10
# Fit a polynomial regression model with Ridge regularization
poly_features = PolynomialFeatures(degree=10)
X_poly = poly_features.fit_transform(X)
ridge_reg_model = Ridge(alpha=1.0)
ridge_reg_model.fit(X_poly, y)
# Predict using the Ridge model
X_fit = np.linspace(0, 10, 100).reshape(-1, 1)
X_fit_poly = poly_features.transform(X_fit)
y_fit_ridge = ridge_reg_model.predict(X_fit_poly)
# Plot the results
plt.scatter(X, y, color='blue', label='Data')
plt.plot(X_fit, y_fit_ridge, color='green', label='Ridge Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.title('Regularization Example')
plt.show()
