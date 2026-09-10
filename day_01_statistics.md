# 📊 Day 1: Statistics & Probability

**Date:** 2026-09-11 | **Time:** 2-3 hours | **Focus:** Foundational statistics concepts for data science interviews

## 🎯 Learning Objectives
By the end of today, you should be able to:
- Explain probability distributions and when to use each
- Perform hypothesis testing and interpret p-values
- Calculate and interpret confidence intervals
- Apply Bayes' theorem to real-world problems
- Understand sampling techniques and bias

## 📚 Key Topics to Cover

### 1. Probability Fundamentals (30 min)
- Sample spaces, events, axioms of probability
- Conditional probability and independence
- Bayes' theorem and applications
- Random variables (discrete vs continuous)

### 2. Probability Distributions (45 min)
- **Discrete**: Bernoulli, Binomial, Poisson, Geometric
- **Continuous**: Uniform, Normal (Gaussian), Exponential, Gamma
- Properties: mean, variance, skewness, kurtosis
- When to use each distribution

### 3. Descriptive Statistics (30 min)
- Measures of central tendency: mean, median, mode
- Measures of dispersion: variance, standard deviation, IQR, range
- Shape measures: skewness, kurtosis
- Data summarization techniques

### 4. Inferential Statistics (45 min)
- Sampling methods and sampling distributions
- Central Limit Theorem
- Confidence intervals (proportions, means)
- Hypothesis testing framework
- Types of errors (Type I, Type II)
- p-values and significance levels
- Common tests: t-test, chi-square, ANOVA

### 5. Statistical Bias & Experimental Design (15 min)
- Selection bias, survivorship bias, confirmation bias
- A/B testing fundamentals
- Experimental vs observational studies
- Confounding variables

## 🔧 Practice Exercises

### Exercise 1: Probability Calculations (20 min)
**Scenario:** A data science team has 8 members: 5 Python specialists and 3 SQL specialists. 
If we randomly select 3 team members for a project:

1. What's the probability that all 3 are Python specialists?
2. What's the probability that exactly 2 are Python specialists?
3. What's the probability that at least 1 is a SQL specialist?
4. Given that the first selected is a Python specialist, what's the probability the second is also a Python specialist?

**Hint:** Use combinations and conditional probability formulas.

### Exercise 2: Distribution Applications (25 min)
**Scenario:** You're analyzing website traffic data.

1. The number of clicks per hour follows a Poisson distribution with λ=7. 
   - What's the probability of getting exactly 10 clicks in an hour?
   - What's the probability of getting fewer than 5 clicks in an hour?

2. User session durations follow an exponential distribution with mean 5 minutes.
   - What's the probability a session lasts more than 10 minutes?
   - What's the median session duration?

3. Exam scores are normally distributed with μ=75 and σ=10.
   - What percentage of students score between 65 and 85?
   - What score represents the 90th percentile?

### Exercise 3: Hypothesis Testing & Confidence Intervals (30 min)
**Scenario:** A company wants to test if a new recommendation algorithm increases user engagement.

- Current algorithm: average session time = 45 minutes (σ=12, n=100)
- New algorithm: average session time = 48 minutes (σ=15, n=100)

1. Formulate null and alternative hypotheses
2. Calculate the test statistic (z-test for two means)
3. Find the p-value and interpret at α=0.05
4. Calculate a 95% confidence interval for the difference in means
5. What would you recommend to the product team?

### Exercise 4: Bayes' Theorem Application (15 min)
**Scenario:** A medical test for a rare disease has:
- 99% sensitivity (true positive rate)
- 95% specificity (true negative rate)
- Disease prevalence: 0.1% in population

If a randomly selected person tests positive:
1. What's the probability they actually have the disease?
2. How does this change if prevalence is 1%?
3. Discuss implications for medical testing and screening programs.

## 💻 Coding Practice (Optional - 15 min)
Create a Python script to:
- Simulate the binomial distribution
- Calculate confidence intervals
- Perform basic hypothesis tests
- Visualize different probability distributions

## 📝 Reflection Questions
1. When would you use a t-test vs a z-test?
2. How does sample size affect the width of a confidence interval?
3. What's the difference between statistical significance and practical significance?
4. How do you explain p-value to a non-technical stakeholder?
5. When is it appropriate to use non-parametric tests?

## 🔗 Today's Resources
- [Edureka Statistics Section](https://www.edureka.co/blog/interview-questions/data-science-interview-questions#statistics)
- [MIT Probability Notes](https://missing.csail.mit.edu/6.042j/fall18/)
- [StatQuest: Probability Distributions](https://www.youtube.com/watch?v=FTQ226ifY7I)
- [Khan Academy: Hypothesis Testing](https://www.khanacademy.org/math/statistics-probability/significance-tests-one-sample)
- [Towards Data Science: Bayes' Theorem](https://towardsdatascience.com/bayes-theorem-with-examples-84b787274440)

## ✅ Daily Checklist
- [ ] Studied probability fundamentals
- [ ] Reviewed common probability distributions
- [ ] Practiced descriptive statistics concepts
- [ ] Learned hypothesis testing framework
- [ ] Completed all 4 practice exercises
- [ ] Spent 2-3 hours total study time
- [ ] Reviewed and understood solutions
- [ ] Created flashcards for key formulas

## 📈 Progress Tracking
**Concepts Mastered:** ⬜ Probability ⬜ Distributions ⬜ Hypothesis Testing ⬜ Confidence Intervals ⬜ Bayes' Theorem

**Time Spent:** ______ hours  
**Difficulty Rating (1-5):** ______  
**Areas to Review Tomorrow:** ___________________________

---
*Prepare for Day 2: Machine Learning Algorithms*