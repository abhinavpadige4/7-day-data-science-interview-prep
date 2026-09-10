# Machine Learning Practice Exercises
# Day 2: ML Algorithms

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.datasets import make_classification, make_blobs
import matplotlib.pyplot as plt

print("=== Machine Learning Practice Exercises - Day 2 ===\n")

# Exercise 1: Linear Regression Implementation
print("Exercise 1: Linear Regression Implementation")
print("Scenario: Predict house prices\n")

# Generate sample data
np.random.seed(42)
n_samples = 100
size = np.random.normal(2000, 500, n_samples)  # square feet
bedrooms = np.random.randint(1, 6, n_samples)   # number of bedrooms
age = np.random.randint(0, 50, n_samples)       # years old
price = size * 0.1 + bedrooms * 10000 - age * 500 + np.random.normal(0, 10000, n_samples)

X = np.column_stack([size, bedrooms, age])
y = price

# Simple linear regression (size only)
X_simple = size.reshape(-1, 1)
model_simple = LinearRegression()
model_simple.fit(X_simple, y)
y_pred_simple = model_simple.predict(X_simple)

# Multiple linear regression
model_multi = LinearRegression()
model_multi.fit(X, y)
y_pred_multi = model_multi.predict(X)

# Ridge regression
model_ridge = Ridge(alpha=1.0)
model_ridge.fit(X, y)
y_pred_ridge = model_ridge.predict(X)

print(f"Simple Linear Regression (size only):")
print(f"  Coefficient: {model_simple.coef_[0]:.2f}")
print(f"  Intercept: {model_simple.intercept_:.2f}")

print(f"\nMultiple Linear Regression:")
print(f"  Coefficients: size={model_multi.coef_[0]:.2f}, bedrooms={model_multi.coef_[1]:.2f}, age={model_multi.coef_[2]:.2f}")
print(f"  Intercept: {model_multi.intercept_:.2f}")

print(f"\nRidge Regression (alpha=1.0):")
print(f"  Coefficients: size={model_ridge.coef_[0]:.2f}, bedrooms={model_ridge.coef_[1]:.2f}, age={model_ridge.coef_[2]:.2f}")
print(f"  Intercept: {model_ridge.intercept_:.2f}\n")

# Exercise 2: Classification Algorithms Comparison
print("Exercise 2: Classification Algorithms Comparison")
print("Scenario: Predict customer churn\n")

# Generate binary classification dataset
X_clf, y_clf = make_classification(n_samples=1000, n_features=10, n_redundant=0, 
                                  n_informative=8, n_clusters_per_class=1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X_clf, y_clf, test_size=0.3, random_state=42)

# Logistic Regression
lr = LogisticRegression(random_state=42, max_iter=1000)
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
y_pred_proba_lr = lr.predict_proba(X_test)[:, 1]

# Decision Tree
dt = DecisionTreeClassifier(random_state=42, max_depth=5)
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)

# Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

# Calculate metrics
def calculate_metrics(y_true, y_pred, y_proba=None):
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred)
    rec = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    auc = roc_auc_score(y_true, y_proba) if y_proba is not None else None
    return acc, prec, rec, f1, auc

metrics_lr = calculate_metrics(y_test, y_pred_lr, y_pred_proba_lr)
metrics_dt = calculate_metrics(y_test, y_pred_dt)
metrics_rf = calculate_metrics(y_test, y_pred_rf)

print("Model Performance Comparison:")
print(f"{'Model':<15} {'Accuracy':<10} {'Precision':<10} {'Recall':<10} {'F1-Score':<10} {'AUC':<10}")
print("-" * 65)
print(f"{'Logistic Regression':<15} {metrics_lr[0]:.4f}     {metrics_lr[1]:.4f}     {metrics_lr[2]:.4f}     {metrics_lr[3]:.4f}     {metrics_lr[4]:.4f}")
print(f"{'Decision Tree':<15} {metrics_dt[0]:.4f}     {metrics_dt[1]:.4f}     {metrics_dt[2]:.4f}     {metrics_dt[3]:.4f}     {'N/A':<10}")
print(f"{'Random Forest':<15} {metrics_rf[0]:.4f}     {metrics_rf[1]:.4f}     {metrics_rf[2]:.4f}     {metrics_rf[3]:.4f}     {'N/A':<10}\n")

# Exercise 3: Clustering & Dimensionality Reduction
print("Exercise 3: Clustering & Dimensionality Reduction")
print("Scenario: Customer segmentation\n")

# Generate sample data for clustering
X_cluster, _ = make_blobs(n_samples=300, centers=4, n_features=2, random_state=42)

# K-means clustering
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(X_cluster)

# PCA for dimensionality reduction
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_cluster)

print(f"K-Means Clustering:")
print(f"  Number of clusters: 4")
print(f"  Cluster centers:\n{kmeans.cluster_centers_}")

print(f"\nPCA Dimensionality Reduction:")
print(f"  Original shape: {X_cluster.shape}")
print(f"  Reduced shape: {X_pca.shape}")
print(f"  Explained variance ratio: {pca.explained_variance_ratio_}")
print(f"  Total variance explained: {sum(pca.explained_variance_ratio_):.4f}\n")

# Exercise 4: SVM & Kernel Trick
print("Exercise 4: SVM & Kernel Trick")
print("Scenario: Iris flower classification\n")

from sklearn.datasets import load_iris
iris = load_iris()
X_iris = iris.data[:, :2]  # Use only first 2 features for visualization
y_iris = iris.target

# Binary classification for simplicity (classes 0 and 1)
mask = y_iris < 2
X_iris_binary = X_iris[mask]
y_iris_binary = y_iris[mask]

# Split data
X_train_svm, X_test_svm, y_train_svm, y_test_svm = train_test_split(
    X_iris_binary, y_iris_binary, test_size=0.3, random_state=42)

# Linear SVM
svm_linear = SVC(kernel='linear', C=1.0, random_state=42)
svm_linear.fit(X_train_svm, y_train_svm)
y_pred_linear = svm_linear.predict(X_test_svm)
acc_linear = accuracy_score(y_test_svm, y_pred_linear)

# RBF Kernel SVM
svm_rbf = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
svm_rbf.fit(X_train_svm, y_train_svm)
y_pred_rbf = svm_rbf.predict(X_test_svm)
acc_rbf = accuracy_score(y_test_svm, y_pred_rbf)

print(f"SVM Classification Results:")
print(f"  Linear Kernel Accuracy: {acc_linear:.4f}")
print(f"  RBF Kernel Accuracy: {acc_rbf:.4f}")
print(f"  Support vectors (linear): {svm_linear.n_support_}")
print(f"  Support vectors (RBF): {svm_rbf.n_support_}\n")

# Exercise 5: Model Evaluation & Validation
print("Exercise 5: Model Evaluation & Validation")
print("Scenario: Proper model validation\n")

# Demonstrate overfitting vs underfitting
from sklearn.model_selection import learning_curve

# Generate data with noise
X_reg, y_reg = make_classification(n_samples=200, n_features=4, n_redundant=0,
                                  n_informative=2, n_clusters_per_class=1, random_state=42)
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
    X_reg, y_reg, test_size=0.3, random_state=42)

# Cross-validation scores
lr_cv = LogisticRegression(random_state=42, max_iter=1000)
cv_scores = cross_val_score(lr_cv, X_train_reg, y_train_reg, cv=5)

print(f"Cross-Validation Scores: {cv_scores}")
print(f"Mean CV Score: {np.mean(cv_scores):.4f} (+/- {np.std(cv_scores) * 2:.4f})")

# Simple train/test split for comparison
lr_cv.fit(X_train_reg, y_train_reg)
train_score = lr_cv.score(X_train_reg, y_train_reg)
test_score = lr_cv.score(X_test_reg, y_test_reg)

print(f"Training Accuracy: {train_score:.4f}")
print(f"Test Accuracy: {test_score:.4f}")
print(f"Overfitting Gap: {train_score - test_score:.4f}\n")

print("=== End of Machine Learning Practice Exercises ===")