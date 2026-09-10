# 🤖 Day 2: Machine Learning Algorithms

**Date:** 2026-09-12 | **Time:** 2-3 hours | **Focus:** Core ML algorithms, theory, and applications

## 🎯 Learning Objectives
By the end of today, you should be able to:
- Explain the bias-variance tradeoff
- Describe and implement linear and logistic regression
- Understand tree-based methods (decision trees, random forests, gradient boosting)
- Explain support vector machines and kernel trick
- Clustering algorithms: K-means, hierarchical
- Dimensionality reduction: PCA, t-SNE
- Model evaluation metrics and cross-validation

## 📚 Key Topics to Cover

### 1. Supervised Learning Fundamentals (30 min)
- Bias-variance tradeoff
- Overfitting vs underfitting
- Regularization (L1, L2, Elastic Net)
- Cross-validation techniques (k-fold, stratified)
- Evaluation metrics for regression (MSE, RMSE, MAE, R²)
- Evaluation metrics for classification (accuracy, precision, recall, F1, ROC-AUC)

### 2. Linear Models (45 min)
- **Linear Regression**: assumptions, gradient descent, normal equation
- **Logistic Regression**: sigmoid function, loss function, interpretation
- Regularization: Ridge, Lasso, Elastic Net
- Feature scaling and normalization
- When to use linear models vs alternatives

### 3. Tree-Based Methods (45 min)
- **Decision Trees**: entropy, Gini impurity, information gain
- Pruning techniques (pre-pruning, post-pruning)
- **Random Forests**: bagging, feature randomness, OOB error
- **Gradient Boosting**: AdaBoost, XGBoost, LightGBM, CatBoost
- Handling categorical features, missing values
- Feature importance interpretation

### 4. Support Vector Machines (30 min)
- Maximum margin classifier
- Kernel trick (linear, polynomial, RBF, sigmoid)
- Soft margin and slack variables
- SVM for regression (SVR)
- Computational complexity and scalability

### 5. Unsupervised Learning (30 min)
- **Clustering**: K-means (elbow method, silhouette score), hierarchical, DBSCAN
- **Dimensionality Reduction**: PCA (variance explained), t-SNE, UMAP
- Applications: anomaly detection, recommendation systems, visualization

### 6. Model Selection & Ensemble Methods (15 min)
- Bagging vs Boosting vs Stacking
- Model stacking and blending
- Hyperparameter tuning (grid search, random search, Bayesian optimization)
- Handling imbalanced datasets (SMOTE, class weights, threshold moving)

## 🔧 Practice Exercises

### Exercise 1: Linear Regression Implementation (25 min)
**Scenario:** Predict house prices based on features like size, bedrooms, location.

1. Implement simple linear regression from scratch (using gradient descent)
2. Implement multiple linear regression
3. Add L2 regularization (Ridge regression)
4. Evaluate using RMSE and R² on a sample dataset
5. Interpret the coefficients

**Bonus:** Compare with scikit-learn's LinearRegression and Ridge.

### Exercise 2: Classification Algorithms Comparison (30 min)
**Scenario:** Predict customer churn (binary classification) using telecom dataset.

1. Implement logistic regression from scratch
2. Implement a decision tree (ID3 algorithm)
3. Implement a random forest (simplified version)
4. Compare accuracy, precision, recall, F1-score on test set
5. Plot ROC curves for each model

### Exercise 3: Clustering & Dimensionality Reduction (25 min)
**Scenario:** Segment customers based on purchasing behavior.

1. Apply K-means clustering to a sample dataset (try different K values)
2. Use elbow method and silhouette score to choose optimal K
3. Apply PCA to reduce dimensions to 2D for visualization
4. Compare original vs reconstructed data after PCA
5. Apply t-SNE for visualization and compare with PCA

### Exercise 4: SVM & Kernel Trick (20 min)
**Scenario:** Classify iris flower species.

1. Implement a linear SVM from scratch (using optimization library like cvxopt or simple gradient)
2. Apply kernel trick with RBF kernel
3. Visualize decision boundaries
4. Compare performance with and without kernel

### Exercise 5: Model Evaluation & Validation (20 min)
**Scenario:** You have built a model and need to validate it properly.

1. Implement k-fold cross-validation from scratch
2. Demonstrate data leakage and how to avoid it
3. Calculate confidence intervals for model performance
4. Plot learning curves to diagnose bias/variance issues

## 💻 Coding Practice (Optional - 15 min)
Create a Python script that:
- Implements at least one algorithm from scratch (linear regression, logistic regression, or K-means)
- Uses scikit-learn for comparison
- Includes proper evaluation and visualization

## 📝 Reflection Questions
1. When would you choose linear regression over a tree-based model?
2. How does the kernel trick work in SVMs?
3. What's the difference between bagging and boosting?
4. How do you handle imbalanced datasets in classification?
5. When would you use PCA vs t-SNE for visualization?
6. What are the assumptions of linear regression and how do you check them?

## 🔗 Today's Resources
- [TryExponent ML Section](https://www.tryexponent.com/blog/data-science-interview-questions#machine-learning)
- [StatQuest: Machine Learning Series](https://www.youtube.com/playlist?list=PLblh5JKOoLUICTaGLRoHQDuF_7q2GfuJF)
- [Coursera: Machine Learning by Andrew Ng](https://www.coursera.org/learn/machine-learning)
- [Towards Data Science: ML Algorithms Explained](https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761)
- [Google's Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)

## ✅ Daily Checklist
- [ ] Studied supervised learning fundamentals
- [ ] Reviewed linear and logistic regression
- [ ] Learned tree-based methods (decision trees, RF, boosting)
- [ ] Understood SVMs and kernel methods
- [ ] Covered clustering and dimensionality reduction
- [ ] Completed all 5 practice exercises
- [ ] Spent 2-3 hours total study time
- [ ] Reviewed and understood solutions
- [ ] Created flashcards for key algorithms and formulas

## 📈 Progress Tracking
**Concepts Mastered:** ⬜ Linear Models ⬜ Tree-Based Methods ⬜ SVMs ⬜ Clustering ⬜ Dimensionality Reduction ⬜ Model Evaluation

**Time Spent:** ______ hours  
**Difficulty Rating (1-5):** ______  
**Areas to Review Tomorrow:** ___________________________

---
*Prepare for Day 3: Python & Pandas*