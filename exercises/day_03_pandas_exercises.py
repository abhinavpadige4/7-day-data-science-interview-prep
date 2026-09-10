# Python & Pandas Practice Exercises
# Day 3: Python & Pandas

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json

print("=== Python & Pandas Practice Exercises - Day 3 ===\n")

# Exercise 1: Data Cleaning Challenge
print("Exercise 1: Data Cleaning Challenge")
print("Scenario: Messy customer transactions dataset\n")

# Create sample messy data
np.random.seed(42)
n_rows = 1000

# Generate transaction data with various issues
data = {
    'transaction_id': [f'TXN{i:06d}' for i in range(n_rows)],
    'customer_id': np.random.choice([f'CUST{i:04d}' for i in range(100)], n_rows),
    'transaction_date': pd.date_range('2023-01-01', periods=n_rows, freq='H'),
    'amount': np.random.exponential(50, n_rows),
    'product_category': np.random.choice(['Electronics', 'Clothing', 'Books', 'Home', 'Sports'], n_rows),
    'payment_method': np.random.choice(['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer'], n_rows),
    'city': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'], n_rows),
    'discount_code': np.random.choice(['SAVE10', 'SAVE20', 'NONE', '', np.nan], n_rows, p=[0.1, 0.05, 0.7, 0.1, 0.05]),
    'customer_rating': np.random.choice([1, 2, 3, 4, 5, np.nan], n_rows, p=[0.05, 0.1, 0.15, 0.3, 0.3, 0.1])
}

df = pd.DataFrame(data)

# Introduce data quality issues
# 1. Missing values in amount (5%)
missing_amount_idx = np.random.choice(df.index, size=int(0.05 * n_rows), replace=False)
df.loc[missing_amount_idx, 'amount'] = np.nan

# 2. Duplicate transactions (3%)
duplicate_idx = np.random.choice(df.index, size=int(0.03 * n_rows), replace=False)
duplicates = df.loc[duplicate_idx].copy()
df = pd.concat([df, duplicates], ignore_index=True)

# 3. Outliers in amount (2%)
outlier_idx = np.random.choice(df.index, size=int(0.02 * n_rows), replace=False)
df.loc[outlier_idx, 'amount'] = df.loc[outlier_idx, 'amount'] * 100

# 4. Inconsistent date formats (some as strings)
string_date_idx = np.random.choice(df.index, size=int(0.1 * n_rows), replace=False)
df.loc[string_date_idx, 'transaction_date'] = df.loc[string_date_idx, 'transaction_date'].dt.strftime('%Y-%m-%d')

# 5. Inconsistent category casing
df['product_category'] = df['product_category'].apply(lambda x: x.upper() if np.random.random() > 0.7 else x)

print(f"Original dataset shape: {df.shape}")
print(f"Missing values:\n{df.isnull().sum()}")
print(f"Duplicate rows: {df.duplicated().sum()}")
print(f"Amount outliers (>$5000): {(df['amount'] > 5000).sum()}\n")

# Data cleaning steps
print("Performing data cleaning...")

# 1. Handle missing values
# For amount: fill with median (robust to outliers)
df['amount_clean'] = df['amount'].fillna(df['amount'].median())
# For discount_code: fill with 'NONE'
df['discount_code'] = df['discount_code'].fillna('NONE')
# For customer_rating: fill with mode
df['customer_rating'] = df['customer_rating'].fillna(df['customer_rating'].mode()[0])

# 2. Remove duplicates
df_clean = df.drop_duplicates(subset=['transaction_id'], keep='first')

# 3. Handle outliers (cap at 99th percentile)
upper_limit = df_clean['amount_clean'].quantile(0.99)
df_clean['amount_clean'] = np.where(df_clean['amount_clean'] > upper_limit, upper_limit, df_clean['amount_clean'])

# 4. Standardize date formats
df_clean['transaction_date'] = pd.to_datetime(df_clean['transaction_date'], errors='coerce')

# 5. Standardize text data
df_clean['product_category'] = df_clean['product_category'].str.title()
df_clean['payment_method'] = df_clean['payment_method'].str.title()
df_clean['city'] = df_clean['city'].str.title()
df_clean['discount_code'] = df_clean['discount_code'].str.upper()

# 6. Feature engineering
df_clean['transaction_month'] = df_clean['transaction_date'].dt.month
df_clean['transaction_day_of_week'] = df_clean['transaction_date'].dt.dayofweek
df_clean['is_weekend'] = df_clean['transaction_day_of_week'].isin([5, 6])
df_clean['amount_log'] = np.log1p(df_clean['amount_clean'])

print(f"Cleaned dataset shape: {df_clean.shape}")
print(f"Remaining missing values:\n{df_clean.isnull().sum().sum()}")
print(f"Sample of cleaned data:")
print(df_clean[['transaction_id', 'amount_clean', 'product_category', 'city']].head())\n"

# Exercise 2: Sales Data Analysis
print("Exercise 2: Sales Data Analysis")
print("Scenario: Monthly sales data for retail company\n")

# Create sales data
np.random.seed(123)
dates = pd.date_range('2023-01-01', '2023-12-31', freq='D')
n_days = len(dates)

sales_data = {
    'date': np.repeat(dates, 50),  # 50 transactions per day
    'product_id': np.random.choice([f'P{i:04d}' for i in range(1, 101)], n_days * 50),
    'category': np.random.choice(['Electronics', 'Clothing', 'Home & Garden', 'Books', 'Sports'], n_days * 50),
    'quantity': np.random.poisson(3, n_days * 50) + 1,
    'price': np.random.exponential(25, n_days * 50) + 5,
    'store_id': np.random.choice([f'S{i:02d}' for i in range(1, 11)], n_days * 50),
    'customer_id': np.random.choice([f'C{i:05d}' for i in range(1, 1001)], n_days * 50)
}

sales_df = pd.DataFrame(sales_data)
sales_df['revenue'] = sales_df['quantity'] * sales_df['price']

print(f"Sales dataset shape: {sales_df.shape}")
print(f"Date range: {sales_df['date'].min()} to {sales_df['date'].max()}\n")

# Analysis tasks
print("Performing sales analysis...")

# 1. Total revenue per product and category
revenue_by_product = sales_df.groupby('product_id')['revenue'].sum().sort_values(ascending=False)
revenue_by_category = sales_df.groupby('category')['revenue'].sum().sort_values(ascending=False)

print("Top 10 products by revenue:")
print(revenue_by_product.head(10))
print(f"\nRevenue by category:")
print(revenue_by_category)

# 2. Top 10 selling products
top_by_quantity = sales_df.groupby('product_id')['quantity'].sum().sort_values(ascending=False).head(10)
top_by_revenue = revenue_by_product.head(10)

print(f"\nTop 10 products by quantity sold:")
print(top_by_quantity)
print(f"\nTop 10 products by revenue:")
print(top_by_revenue)

# 3. Month-over-month growth
sales_df['month'] = sales_df['date'].dt.to_period('M')
monthly_revenue = sales_df.groupby('month')['revenue'].sum()
mom_growth = monthly_revenue.pct_change() * 100

print(f"\nMonthly revenue:")
print(monthly_revenue.head())
print(f"\nMonth-over-month growth (%):")
print(mom_growth.head())

# 4. Pivot table: sales by category and month
pivot_table = sales_df.pivot_table(
    values='revenue',
    index='category',
    columns='month',
    aggfunc='sum',
    fill_value=0
)

print(f"\nPivot table (Category x Month):")
print(pivot_table.head())

# 5. Seasonal trends
sales_df['day_of_year'] = sales_df['date'].dt.dayofyear
seasonal_trend = sales_df.groupby('day_of_year')['revenue'].mean()

print(f"\nAverage revenue by day of year (showing first 10 days):")
print(seasonal_trend.head(10))

# 6. Customer lifetime value approximation
customer_value = sales_df.groupby('customer_id').agg({
    'revenue': 'sum',
    'date': ['min', 'max']
})
customer_value.columns = ['total_revenue', 'first_purchase', 'last_purchase']
customer_value['customer_lifetime_days'] = (customer_value['last_purchase'] - customer_value['first_purchase']).dt.days
customer_value['avg_order_value'] = customer_value['total_revenue'] / sales_df.groupby('customer_id').size()

print(f"\nCustomer value metrics (top 10 customers):")
print(customer_value.sort_values('total_revenue', ascending=False).head(10))\n"

# Exercise 3: User Behavior Data
print("Exercise 3: User Behavior Data")
print("Scenario: Mobile app user engagement analysis\n")

# Create user session data
np.random.seed(456)
n_sessions = 5000

# Generate user IDs with power-law distribution (few power users)
user_ids = np.random.zipf(1.5, n_sessions)  # Zipf distribution
user_ids = np.clip(user_ids, 1, 1000)  # Limit to 1000 users
user_ids = [f'USER{id:04d}' for id in user_ids]

session_data = {
    'session_id': [f'SESS{i:08d}' for i in range(n_sessions)],
    'user_id': user_ids,
    'session_start': pd.date_range('2023-06-01', periods=n_sessions, freq='5T'),
    'session_duration': np.random.exponential(300, n_sessions),  # seconds
    'screens_visited': np.random.poisson(8, n_sessions) + 1,
    'features_used': np.random.choice(['home', 'search', 'profile', 'settings', 'notifications', 'messages'], n_sessions),
    'device_type': np.random.choice(['iOS', 'Android', 'Web'], n_sessions, p=[0.4, 0.4, 0.2]),
    'country': np.random.choice(['US', 'UK', 'Canada', 'Australia', 'Germany'], n_sessions, p=[0.5, 0.2, 0.1, 0.1, 0.1])
}

sessions_df = pd.DataFrame(session_data)
sessions_df['session_end'] = sessions_df['session_start'] + pd.to_timedelta(sessions_df['session_duration'], unit='s')

print(f"Session dataset shape: {sessions_df.shape}")
print(f"Date range: {sessions_df['session_start'].min()} to {sessions_df['session_start'].max()}\n")

# Analysis tasks
print("Analyzing user behavior...")

# 1. Session duration and engagement metrics
print("Session duration statistics:")
print(sessions_df['session_duration'].describe())
print(f"\nMedian session duration: {sessions_df['session_duration'].median():.0f} seconds")
print(f"90th percentile session duration: {sessions_df['session_duration'].quantile(0.9):.0f} seconds")

# 2. User cohorts (weekly cohorts)
sessions_df['cohort_week'] = sessions_df['session_start'].dt.to_period('W')
cohort_data = sessions_df.groupby(['user_id', 'cohort_week']).size().reset_index(name='sessions_per_week')

print(f"\nNumber of active users per week:")
print(cohort_data.groupby('cohort_week').size().head())

# 3. Retention rates (simplified)
# For demonstration, we'll calculate week-over-week retention
cohort_pivot = cohort_data.pivot_table(
    index='user_id',
    columns='cohort_week',
    values='sessions_per_week',
    fill_value=0
)

# Convert to binary (active/inactive)
cohort_binary = (cohort_pivot > 0).astype(int)

if len(cohort_binary.columns) >= 2:
    week1_active = cohort_binary.iloc[:, 0].sum()
    week2_active = cohort_binary.iloc[:, 1].sum()
    week2_from_week1 = ((cohort_binary.iloc[:, 0] > 0) & (cohort_binary.iloc[:, 1] > 0)).sum()
    
    if week1_active > 0:
        retention_rate = week2_from_week1 / week1_active * 100
        print(f"\nWeek 1 to Week 2 retention: {retention_rate:.1f}%")
    else:
        print("\nNot enough data for retention calculation")
else:
    print("\nNot enough weeks for retention calculation")

# 4. Power users (top 10% by session count or duration)
user_stats = sessions_df.groupby('user_id').agg({
    'session_id': 'count',
    'session_duration': ['sum', 'mean']
})
user_stats.columns = ['session_count', 'total_duration', 'avg_duration']

power_users_by_count = user_stats.nlargest(int(len(user_stats) * 0.1), 'session_count')
power_users_by_duration = user_stats.nlargest(int(len(user_stats) * 0.1), 'total_duration')

print(f"\nPower users (top 10% by session count):")
print(power_users_by_count.head())
print(f"\nPower users (top 10% by total duration):")
print(power_users_by_duration.head())

# 5. Feature adoption rates
feature_usage = sessions_df['features_used'].value_counts(normalize=True) * 100
print(f"\nFeature adoption rates:")
print(feature_usage.head())\n"

# Exercise 4: Data Transformation & Joins
print("Exercise 4: Data Transformation & Joins")
print("Scenario: 360-degree customer view\n")

# Create three datasets
np.random.seed(789)

# 1. Customer demographics
n_customers = 500
demographics = {
    'customer_id': [f'CUST{i:04d}' for i in range(1, n_customers + 1)],
    'age': np.random.randint(18, 80, n_customers),
    'gender': np.random.choice(['Male', 'Female', 'Other'], n_customers),
    'income_level': np.random.choice(['Low', 'Medium', 'High'], n_customers, p=[0.3, 0.5, 0.2]),
    'education': np.random.choice(['High School', 'Bachelor', 'Master', 'PhD'], n_customers),
    'signup_date': pd.date_range('2020-01-01', periods=n_customers, freq='D')
}
demographics_df = pd.DataFrame(demographics)

# 2. Transaction history
n_transactions = 2000
transactions = {
    'transaction_id': [f'TXN{i:06d}' for i in range(n_transactions)],
    'customer_id': np.random.choice([f'CUST{i:04d}' for i in range(1, n_customers + 1)], n_transactions),
    'transaction_date': pd.date_range('2023-01-01', periods=n_transactions, freq='H'),
    'amount': np.random.exponential(100, n_transactions),
    'product_category': np.random.choice(['Electronics', 'Clothing', 'Home', 'Books'], n_transactions),
    'payment_method': np.random.choice(['Credit Card', 'Debit Card', 'PayPal'], n_transactions)
}
transactions_df = pd.DataFrame(transactions)

# 3. Support tickets
n_tickets = 300
tickets = {
    'ticket_id': [f'TKT{i:05d}' for i in range(n_tickets)],
    'customer_id': np.random.choice([f'CUST{i:04d}' for i in range(1, n_customers + 1)], n_tickets),
    'ticket_date': pd.date_range('2023-01-01', periods=n_tickets, freq='2H'),
    'issue_type': np.random.choice(['Technical', 'Billing', 'Shipping', 'Product'], n_tickets),
    'priority': np.random.choice(['Low', 'Medium', 'High'], n_tickets, p=[0.5, 0.3, 0.2]),
    'resolution_time_hours': np.random.exponential(24, n_tickets)
}
tickets_df = pd.DataFrame(tickets)

print(f"Demographics shape: {demographics_df.shape}")
print(f"Transactions shape: {transactions_df.shape}")
print(f"Support tickets shape: {tickets_df.shape}\n")

# Data transformation and joining
print("Performing data transformation and joins...")

# 1. Clean and standardize customer IDs (already consistent in this example)
# In real scenario, we might have different formats to reconcile

# 2. Aggregate transaction data
transaction_agg = transactions_df.groupby('customer_id').agg({
    'transaction_id': 'count',
    'amount': ['sum', 'mean', 'std'],
    'transaction_date': ['min', 'max']
})
transaction_agg.columns = ['transaction_count', 'total_spent', 'avg_transaction', 'std_transaction', 'first_transaction', 'last_transaction']
transaction_agg['customer_lifetime_days'] = (transaction_agg['last_transaction'] - transaction_agg['first_transaction']).dt.days
transaction_agg = transaction_agg.reset_index()

# 3. Aggregate support ticket data
ticket_agg = tickets_df.groupby('customer_id').agg({
    'ticket_id': 'count',
    'resolution_time_hours': ['mean', 'max'],
    'issue_type': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'None',
    'priority': lambda x: x.mode().iloc[0] if len(x.mode()) > 0 else 'Low'
})
ticket_agg.columns = ['ticket_count', 'avg_resolution_time', 'max_resolution_time', 'most_common_issue', 'priority_level']
ticket_agg = ticket_agg.reset_index()

# 4. Perform left joins to combine data
customer_view = demographics_df.merge(transaction_agg, on='customer_id', how='left')
customer_view = customer_view.merge(ticket_agg, on='customer_id', how='left')

# 5. Handle missing values in joined data
customer_view['transaction_count'] = customer_view['transaction_count'].fillna(0)
customer_view['total_spent'] = customer_view['total_spent'].fillna(0)
customer_view['avg_transaction'] = customer_view['avg_transaction'].fillna(0)
customer_view['std_transaction'] = customer_view['std_transaction'].fillna(0)
customer_view['ticket_count'] = customer_view['ticket_count'].fillna(0)
customer_view['avg_resolution_time'] = customer_view['avg_resolution_time'].fillna(0)
customer_view['max_resolution_time'] = customer_view['max_resolution_time'].fillna(0)
customer_view['most_common_issue'] = customer_view['most_common_issue'].fillna('None')
customer_view['priority_level'] = customer_view['priority_level'].fillna('Low')

# 6. Create additional features
customer_view['days_since_signup'] = (datetime.now() - customer_view['signup_date']).dt.days
customer_view['engagement_score'] = (
    customer_view['transaction_count'] * 0.4 +
    customer_view['total_spent'] / 1000 * 0.3 +
    (1 - customer_view['ticket_count'] / (customer_view['ticket_count'] + 1)) * 0.3
)

# 7. Detect and resolve conflicts (example: inconsistent income levels)
# In this synthetic data, no conflicts, but we'd check for inconsistencies

print(f"Final customer view shape: {customer_view.shape}")
print(f"Columns: {list(customer_view.columns)}")
print(f"\nSample customer view:")
print(customer_view[['customer_id', 'age', 'gender', 'income_level', 'transaction_count', 'total_spent', 'ticket_count']].head())\n"

# Exercise 5: Time Series Analysis
print("Exercise 5: Time Series Analysis")
print("Scenario: Website traffic analysis\n")

# Create website traffic data
np.random.seed(999)
n_days = 365
dates = pd.date_range('2023-01-01', periods=n_days, freq='D')

# Generate traffic with trend, seasonality, and noise
trend = np.linspace(1000, 2000, n_days)  # Increasing trend
weekly_seasonality = 200 * np.sin(2 * np.pi * np.arange(n_days) / 7)  # Weekly pattern
yearly_seasonality = 500 * np.sin(2 * np.pi * np.arange(n_days) / 365)  # Yearly pattern
noise = np.random.normal(0, 100, n_days)

traffic = trend + weekly_seasonality + yearly_seasonality + noise
traffic = np.maximum(traffic, 100)  # Ensure positive traffic

traffic_df = pd.DataFrame({
    'date': dates,
    'visitors': traffic.astype(int),
    'pageviews': (traffic * np.random.uniform(2, 5, n_days)).astype(int),
    'bounce_rate': np.random.uniform(0.2, 0.6, n_days),
    'conversion_rate': np.random.uniform(0.01, 0.05, n_days)
})

print(f"Traffic dataset shape: {traffic_df.shape}")
print(f"Date range: {traffic_df['date'].min()} to {traffic_df['date'].max()}\n")

# Time series analysis
print("Performing time series analysis...")

# 1. Set datetime column as index
traffic_ts = traffic_df.set_index('date')

# 2. Resample data to different frequencies
traffic_weekly = traffic_ts.resample('W').sum()
traffic_monthly = traffic_ts.resample('M').mean()

print(f"Daily data points: {len(traffic_ts)}")
print(f"Weekly data points: {len(traffic_weekly)}")
print(f"Monthly data points: {len(traffic_monthly)}\n")

# 3. Calculate rolling averages
traffic_ts['visitors_7day_avg'] = traffic_ts['visitors'].rolling(window=7).mean()
traffic_ts['visitors_30day_avg'] = traffic_ts['visitors'].rolling(window=30).mean()

# 4. Identify trends and seasonality
from scipy import signal

# Detrend to analyze seasonality
visitors_detrended = signal.detrend(traffic_ts['visitors'])

# 5. Detect anomalies using statistical methods
# Using IQR method
Q1 = traffic_ts['visitors'].quantile(0.25)
Q3 = traffic_ts['visitors'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

anomalies = traffic_ts[(traffic_ts['visitors'] < lower_bound) | (traffic_ts['visitors'] > upper_bound)]

print(f"Traffic statistics:")
print(f"  Mean daily visitors: {traffic_ts['visitors'].mean():.0f}")
print(f"  Median daily visitors: {traffic_ts['visitors'].median():.0f}")
print(f"  Std daily visitors: {traffic_ts['visitors'].std():.0f}")
print(f"\nAnomaly detection (IQR method):")
print(f"  Lower bound: {lower_bound:.0f}")
print(f"  Upper bound: {upper_bound:.0f}")
print(f"  Number of anomalies: {len(anomalies)}")

if len(anomalies) > 0:
    print(f"  Anomaly dates: {anomalies.index.strftime('%Y-%m-%d').tolist()[:5]}...")  # Show first 5

# 6. Prepare data for forecasting (create features)
traffic_ts['day_of_week'] = traffic_ts.index.dayofweek
traffic_ts['day_of_month'] = traffic_ts.index.day
traffic_ts['month'] = traffic_ts.index.month
traffic_ts['is_weekend'] = traffic_ts['day_of_week'].isin([5, 6]).astype(int)

print(f"\nFeature-engineered dataset shape: {traffic_ts.shape}")
print(f"Sample with features:")
print(traffic_ts[['visitors', 'visitors_7day_avg', 'day_of_week', 'is_weekend']].head())\n"

print("=== End of Python & Pandas Practice Exercises ===")