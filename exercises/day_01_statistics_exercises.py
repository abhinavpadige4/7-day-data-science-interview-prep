# Statistics Practice Exercises
# Day 1: Statistics & Probability

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd
from math import comb, factorial

print("=== Statistics Practice Exercises - Day 1 ===\n")

# Exercise 1: Probability Calculations
print("Exercise 1: Probability Calculations")
print("Scenario: Data science team with 8 members (5 Python, 3 SQL specialists)")
print("Selecting 3 team members randomly\n")

# 1. Probability all 3 are Python specialists
# P = (5/8) * (4/7) * (3/6) = (5*4*3)/(8*7*6) = 60/336 = 5/28
p_all_python = (5/8) * (4/7) * (3/6)
print(f"1. Probability all 3 are Python specialists: {p_all_python:.4f} ({p_all_python*100:.2f}%)")

# 2. Probability exactly 2 are Python specialists
# P = (ways to choose 2 Python * ways to choose 1 SQL) / total ways
# P = [C(5,2) * C(3,1)] / C(8,3)
p_exactly_2_python = (comb(5, 2) * comb(3, 1)) / comb(8, 3)
print(f"2. Probability exactly 2 are Python specialists: {p_exactly_2_python:.4f} ({p_exactly_2_python*100:.2f}%)")

# 3. Probability at least 1 is SQL specialist
# P = 1 - P(no SQL) = 1 - P(all Python)
p_at_least_1_sql = 1 - p_all_python
print(f"3. Probability at least 1 is SQL specialist: {p_at_least_1_sql:.4f} ({p_at_least_1_sql*100:.2f}%)")

# 4. Conditional probability: given first is Python, probability second is also Python
# After first Python selected: 4 Python, 3 SQL left (7 total)
p_second_python_given_first = 4/7
print(f"4. Probability second is Python given first is Python: {p_second_python_given_first:.4f} ({p_second_python_given_first*100:.2f}%)\n")

# Exercise 2: Distribution Applications
print("Exercise 2: Distribution Applications\n")

# Part 1: Poisson distribution (clicks per hour, λ=7)
lam = 7
print("Part 1: Poisson distribution (clicks per hour, λ=7)")
p_exactly_10 = stats.poisson.pmf(10, lam)
p_fewer_than_5 = stats.poisson.cdf(4, lam)  # P(X < 5) = P(X ≤ 4)
print(f"  Probability of exactly 10 clicks: {p_exactly_10:.4f}")
print(f"  Probability of fewer than 5 clicks: {p_fewer_than_5:.4f}")

# Part 2: Exponential distribution (session duration, mean=5 min)
mean_duration = 5
lambda_exp = 1/mean_duration  # rate parameter
print("\nPart 2: Exponential distribution (session duration, mean=5 min)")
p_more_than_10 = 1 - stats.expon.cdf(10, scale=mean_duration)  # or stats.expon.sf(10, scale=mean_duration)
median_duration = mean_duration * np.log(2)  # For exponential: median = mean * ln(2)
print(f"  Probability session lasts more than 10 minutes: {p_more_than_10:.4f}")
print(f"  Median session duration: {median_duration:.2f} minutes")

# Part 3: Normal distribution (exam scores, μ=75, σ=10)
mu, sigma = 75, 10
print("\nPart 3: Normal distribution (exam scores, μ=75, σ=10)")
p_between_65_85 = stats.norm.cdf(85, mu, sigma) - stats.norm.cdf(65, mu, sigma)
score_90th = stats.norm.ppf(0.90, mu, sigma)
print(f"  Percentage scoring between 65 and 85: {p_between_65_85*100:.2f}%")
print(f"  Score representing 90th percentile: {score_90th:.2f}\n")

# Exercise 3: Hypothesis Testing & Confidence Intervals
print("Exercise 3: Hypothesis Testing & Confidence Intervals")
print("Scenario: Testing new recommendation algorithm\n")

# Current algorithm: μ1=45, σ1=12, n1=100
# New algorithm: μ2=48, σ2=15, n2=100
mu1, sigma1, n1 = 45, 12, 100
mu2, sigma2, n2 = 48, 15, 100

# 1. Hypotheses
print("1. Hypotheses:")
print("   H0: μ_new ≤ μ_current (no improvement or worse)")
print("   H1: μ_new > μ_current (improvement)")

# 2. Test statistic (z-test for two means)
# SE = sqrt(σ1²/n1 + σ2²/n2)
se = np.sqrt(sigma1**2/n1 + sigma2**2/n2)
z_score = (mu2 - mu1) / se
print(f"\n2. Test statistic (z-score): {z_score:.4f}")

# 3. p-value (one-tailed test)
p_value = 1 - stats.norm.cdf(z_score)
print(f"3. p-value (one-tailed): {p_value:.4f}")
print(f"   Significant at α=0.05? {'Yes' if p_value < 0.05 else 'No'}")

# 4. 95% confidence interval for difference
# CI = (μ2 - μ1) ± z* * SE
z_critical = stats.norm.ppf(0.975)  # 95% CI two-tailed
margin_of_error = z_critical * se
ci_lower = (mu2 - mu1) - margin_of_error
ci_upper = (mu2 - mu1) + margin_of_error
print(f"\n4. 95% Confidence Interval for difference: [{ci_lower:.2f}, {ci_upper:.2f}]")

# 5. Recommendation
print(f"\n5. Recommendation: {'Implement new algorithm' if p_value < 0.05 else 'Do not implement new algorithm'}")
print(f"   (Based on statistical significance at α=0.05)\n")

# Exercise 4: Bayes' Theorem Application
print("Exercise 4: Bayes' Theorem Application")
print("Scenario: Medical test for rare disease\n")

# Given:
# Sensitivity (true positive rate) = P(Test+ | Disease) = 0.99
# Specificity (true negative rate) = P(Test- | No Disease) = 0.95
# Prevalence = P(Disease) = 0.001

sensitivity = 0.99
specificity = 0.95
prevalence = 0.001

# P(Disease | Test+) = [P(Test+ | Disease) * P(Disease)] / P(Test+)
# P(Test+) = P(Test+ | Disease)*P(Disease) + P(Test+ | No Disease)*P(No Disease)
# P(Test+ | No Disease) = 1 - specificity = false positive rate

p_disease_given_positive = (sensitivity * prevalence) / \
                          (sensitivity * prevalence + (1 - specificity) * (1 - prevalence))

print(f"Given:")
print(f"  Sensitivity (true positive rate): {sensitivity}")
print(f"  Specificity (true negative rate): {specificity}")
print(f"  Disease prevalence: {prevalence}")
print(f"\nP(Disease | Test+) = {p_disease_given_positive:.4f} ({p_disease_given_positive*100:.2f}%)")

# With prevalence = 1%
prevalence_2 = 0.01
p_disease_given_positive_2 = (sensitivity * prevalence_2) / \
                            (sensitivity * prevalence_2 + (1 - specificity) * (1 - prevalence_2))
print(f"\nWith prevalence = 1%:")
print(f"P(Disease | Test+) = {p_disease_given_positive_2:.4f} ({p_disease_given_positive_2*100:.2f}%)")

print("\nImplication: Even with a highly accurate test, for rare diseases,")
print("most positive results are false positives when prevalence is very low.\n")

print("=== End of Statistics Practice Exercises ===")