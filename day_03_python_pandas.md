# 🐍 Day 3: Python & Pandas

**Date:** 2026-09-13 | **Time:** 2-3 hours | **Focus:** Python programming and data manipulation with Pandas

## 🎯 Learning Objectives
By the end of today, you should be able to:
- Write efficient Python code using best practices
- Manipulate and clean data using Pandas
- Handle missing data, duplicates, and outliers
- Perform groupby operations and aggregations
- Merge, join, and concatenate DataFrames
- Work with time series data
- Optimize Pandas operations for performance

## 📚 Key Topics to Cover

### 1. Python Fundamentals Review (30 min)
- Data types: strings, lists, tuples, dictionaries, sets
- Control flow: if/else, for/while loops, list comprehensions
- Functions: arguments, return values, lambda, map, filter
- Object-oriented programming basics (classes, inheritance)
- Error handling: try/except, custom exceptions
- Modules and packages: importing, creating

### 2. Pandas Data Structures (30 min)
- Series: creation, indexing, operations
- DataFrame: creation from various sources (CSV, JSON, SQL, dict)
- Essential attributes: shape, dtypes, head, tail, info, describe
- Indexing and selection: loc, iloc, at, iat, boolean indexing
- Setting and resetting index

### 3. Data Cleaning & Preparation (45 min)
- Handling missing values: dropna, fillna, interpolation
- Detecting and handling outliers
- Removing duplicates
- Data type conversion (astype, to_numeric, to_datetime)
- String methods in Pandas (str accessor)
- Applying functions: apply, applymap, map
- Renaming columns and index

### 4. Data Transformation & Aggregation (45 min)
- GroupBy operations: split-apply-combine
- Aggregation functions: sum, mean, count, std, min, max, custom
- Transform and filter operations
- Pivot tables and cross-tabs
- Melting and unmelting (wide to long format)
- Binning and discretization (cut, qcut)

### 5. Merging, Joining & Concatenating (30 min)
- Database-style joins: inner, left, right, outer
- Merging on multiple columns
- Concatenating DataFrames (axis=0, axis=1)
- Handling overlapping columns in merges
- Using merge with indicator

### 6. Time Series in Pandas (20 min)
- Creating DatetimeIndex
- Resampling: frequency conversion (upsampling, downsampling)
- Rolling windows and moving averages
- Shifting and lagging
- Time zone handling

### 7. Performance Optimization (15 min)
- Vectorization vs iteration
- Using built-in Pandas methods
- Categorical data for memory efficiency
- Query method for filtering
- Chaining operations

## 🔧 Practice Exercises

### Exercise 1: Data Cleaning Challenge (30 min)
**Scenario:** You've received a messy dataset of customer transactions.

**Tasks:**
1. Load the CSV file into a Pandas DataFrame
2. Identify and handle missing values appropriately (different strategies for different columns)
3. Detect and treat outliers in transaction amounts
4. Remove duplicate transactions
5. Standardize date formats and extract features (day of week, month, etc.)
6. Clean text data (remove special characters, standardize categories)
7. Save the cleaned dataset

### Exercise 2: Sales Data Analysis (35 min)
**Scenario:** Analyze monthly sales data for a retail company.

**Tasks:**
1. Load sales data with columns: date, product_id, category, quantity, price, store_id
2. Calculate total revenue per product and per category
3. Find top 10 selling products by quantity and revenue
4. Analyze month-over-month growth using resampling
5. Create a pivot table showing sales by category and month
6. Identify seasonal trends in sales data
7. Calculate customer lifetime value (if customer data available) or average transaction value

### Exercise 3: User Behavior Data (30 min)
**Scenario:** Analyze user engagement data from a mobile app.

**Tasks:**
1. Load user session data with timestamps
2. Calculate session duration and engagement metrics
3. Group users by behavior cohorts (weekly cohorts)
4. Calculate retention rates (day 1, day 7, day 30 retention)
5. Identify power users (top 10% by session count or duration)
6. Analyze feature adoption rates
7. Create a summary report of key metrics

### Exercise 4: Data Transformation & Joins (25 min)
**Scenario:** Combine data from multiple sources for a 360-degree customer view.

**Tasks:**
1. Load customer demographics, transaction history, and support tickets datasets
2. Clean and standardize customer IDs across datasets
3. Perform left joins to combine transaction and support data with demographics
4. Handle missing values in joined data appropriately
5. Create aggregated features (total spend, average ticket resolution time)
6. Detect and resolve conflicts in merged data
7. Prepare final dataset for modeling or analysis

### Exercise 5: Time Series Analysis (20 min)
**Scenario:** Analyze website traffic data over time.

**Tasks:**
1. Load timestamped website traffic data
2. Set datetime column as index
3. Resample data to daily, weekly, and monthly frequencies
4. Calculate rolling averages (7-day and 30-day)
5. Identify trends and seasonality
6. Detect anomalies using statistical methods
7. Prepare data for forecasting models

## 💻 Coding Practice (Optional - 15 min)
Create a Python script that:
- Demonstrates at least 5 different Pandas operations
- Includes data cleaning, transformation, and analysis
- Uses method chaining where appropriate
- Includes comments explaining each step

## 📝 Reflection Questions
1. When would you use `apply` vs vectorized operations in Pandas?
2. How do you handle a dataset that doesn't fit in memory?
3. What's the difference between `merge` and `join` in Pandas?
4. How do you efficiently handle string operations in Pandas?
5. When would you use `pivot_table` vs `groupby`?
6. How do you optimize Pandas code for performance?
7. What are the advantages of using categorical data types?

## 🔗 Today's Resources
- [Edureka Python/Pandas Section](https://www.edureka.co/blog/interview-questions/data-science-interview-questions#python)
- [TryExponent Python Guide](https://www.tryexponent.com/blog/data-science-interview-questions#python-pandas)
- [Corey Schafer Pandas Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)
- [DataCamp: Data Manipulation with Pandas](https://www.datacamp.com/courses/data-manipulation-with-pandas)
- [Pandas Official Documentation](https://pandas.pydata.org/docs/)
- [Modern Pandas Tutorial](https://tomaugspurger.github.io/modern-1.html)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)

## ✅ Daily Checklist
- [ ] Reviewed Python fundamentals
- [ ] Mastered Pandas data structures (Series, DataFrame)
- [ ] Practiced data cleaning and preparation techniques
- [ ] Learned groupBy operations and aggregations
- [ ] Understood merging, joining, and concatenating
- [ ] Worked with time series data in Pandas
- [ ] Completed all 5 practice exercises
- [ ] Spent 2-3 hours total study time
- [ ] Reviewed and understood solutions
- [ ] Created flashcards for key Pandas functions and methods

## 📈 Progress Tracking
**Concepts Mastered:** ⬜ Python Basics ⬜ Pandas Structures ⬜ Data Cleaning ⬜ GroupBy & Aggregation ⬜ Merging/Joining ⬜ Time Series ⬜ Performance

**Time Spent:** ______ hours  
**Difficulty Rating (1-5):** ______  
**Areas to Review Tomorrow:** ___________________________

---
*Prepare for Day 4: SQL*