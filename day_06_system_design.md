# 🛠️ Day 6: System Design & Product Sense

**Date:** 2026-09-16 | **Time:** 2-3 hours | **Focus:** Designing data systems, metrics, and product thinking

## 🎯 Learning Objectives
By the end of today, you should be able to:
- Design end-to-end data pipelines and systems
- Define and evaluate key metrics for products
- Understand A/B testing fundamentals and statistical significance
- Think about data privacy, ethics, and bias
- Approach product sense questions systematically
- Communicate trade-offs in system design

## 📚 Key Topics to Cover

### 1. Data Pipeline Design (40 min)
- Batch vs streaming processing
- ETL vs ELT
- Data ingestion methods (APIs, databases, streaming, file uploads)
- Data storage options (data lakes, data warehouses, databases)
- Data transformation and processing (Spark, Flink, Airflow)
- Data quality and validation
- Monitoring and alerting
- Pipeline orchestration (Airflow, Prefect, Dagster)

### 2. Metrics & Measurement (35 min)
- North Star metric and key product metrics
- Leading vs lagging indicators
- Vanity metrics vs actionable metrics
- Framework for choosing metrics (HEART, GSM, etc.)
- Segmenting metrics by user cohorts
- Metric drift and data quality issues
- Creating metric dashboards

### 3. A/B Testing & Experimentation (40 min)
- Hypothesis formulation for experiments
- Experimental design: control vs treatment groups
- Sample size calculation and power analysis
- Randomization and confounding variables
- Interpreting results: p-values, confidence intervals, effect size
- Multiple testing problem and corrections (Bonferroni, FDR)
- Sequential testing and peeking
- Common pitfalls in A/B testing
- Beyond A/B testing: multivariate, bandit tests

### 4. Data Privacy, Ethics & Bias (25 min)
- GDPR, CCPA, and other privacy regulations
- Anonymization and pseudonymization techniques
- Data minimization and purpose limitation
- Bias in data and algorithms (selection bias, confirmation bias, etc.)
- Fairness metrics and mitigation strategies
- Ethical considerations in data science
- Model interpretability and explainability

### 5. Product Sense Framework (30 min)
- Clarifying the problem and goals
- Understanding users and use cases
- Defining success metrics
- Brainstorming solutions and trade-offs
- Prioritization frameworks (RICE, MoSCoW, etc.)
- MVP definition and rollout strategy
- Post-launch analysis and iteration

### 6. System Design Case Studies (30 min)
- Designing a recommendation system
- Building a fraud detection system
- Creating a data dashboard for executives
- Designing a feature flag system
- Building a real-time analytics pipeline
- Designing a data marketplace or internal data platform

## 🔧 Practice Exercises

### Exercise 1: Metric Design (25 min)
**Scenario:** You're working on a new social media feature that allows users to react to posts with emojis.

**Tasks:**
1. Define the goal of this feature
2. Identify potential user behaviors you want to encourage
3. Propose 3-5 metrics to measure success (mix of engagement, satisfaction, business impact)
4. For each metric, define how you would calculate it
5. Identify potential confounding factors
6. Discuss how you would track these metrics over time

### Exercise 2: A/B Test Analysis (30 min)
**Scenario:** An e-commerce company tested a new recommendation algorithm on 10% of users.

**Data:**
- Control group: 1000 users, average revenue per user = $45
- Treatment group: 1000 users, average revenue per user = $48
- Standard deviation in both groups ≈ $12

**Tasks:**
1. Formulate null and alternative hypotheses
2. Calculate the appropriate test statistic
3. Find the p-value and interpret at α=0.05
4. Calculate a 95% confidence interval for the difference
5. Discuss practical significance vs statistical significance
6. What would you recommend to the product team?

### Exercise 3: Data Pipeline Design (30 min)
**Scenario:** Design a pipeline to process user clickstream data for real-time personalization.

**Requirements:**
- Ingest clickstream data from web and mobile apps
- Process data to update user profiles in real-time
- Serve personalized recommendations based on updated profiles
- Handle peak loads of 100k events per second
- Ensure data quality and handle missing/invalid events
- Provide monitoring and alerting

**Tasks:**
1. Sketch the high-level architecture
2. Choose technologies for each component (ingestion, processing, storage, serving)
3. Discuss trade-offs between latency, consistency, and cost
4. Identify potential failure points and mitigation strategies
5. How would you test this pipeline?

### Exercise 4: Product Sense Problem (25 min)
**Scenario:** A music streaming app wants to increase user retention.

**Tasks:**
1. Clarify the problem: what does "increase retention" mean? Which retention metric?
2. Understand the users: who are we trying to retain? New users, power users, etc.
3. Brainstorm potential reasons for churn
4. Propose 3-4 product interventions to address retention
5. For each intervention, define how you would measure success
6. Prioritize the interventions using a framework (e.g., RICE)
7. Describe how you would test the top intervention

### Exercise 5: Ethics & Bias Case Study (20 min)
**Scenario:** A bank uses a machine learning model to approve loan applications.

**Tasks:**
1. Identify potential sources of bias in the data and model
2. How could this bias lead to unfair outcomes for certain groups?
3. What fairness metrics would you evaluate?
4. How would you mitigate bias in the model?
5. What transparency and explainability measures would you implement?
6. How would you monitor the model post-deployment for fairness?

### Exercise 6: System Design Trade-offs (15 min)
**Scenario:** Choose between a relational database and a NoSQL database for a new feature.

**Tasks:**
1. List the characteristics of your data (structure, size, query patterns)
2. Compare relational vs NoSQL for your use case
3. Discuss consistency, availability, and partition tolerance (CAP theorem)
4. Consider development speed, operational complexity, and cost
5. Make a recommendation and justify it

## 💻 Coding Practice (Optional - 15 min)
Create a Python script that:
- Simulates an A/B test and calculates p-value
- Demonstrates sample size calculation
- Or designs a simple data pipeline using functions

## 📝 Reflection Questions
1. How do you choose between different types of metrics for a product?
2. What are the key considerations when designing a data pipeline?
3. How do you explain the concept of statistical power to a non-technical stakeholder?
4. When would you decide not to run an A/B test?
5. How do you balance user privacy with data utility?
6. What questions would you ask to understand a product's goals and users?
7. How do you approach an open-ended system design question?

## 🔗 Today's Resources
- [TryExponent System Design Section](https://www.tryexponent.com/blog/data-science-interview-questions#system-design)
- [Edureka System Design Section](https://www.edureka.co/blog/interview-questions/data-science-interview-questions#system-design)
- [Designing Data-Intensive Applications](https://dataintensive.net/)
- [A/B Testing Guide by Google](https://developers.google.com/optimization)
- [Metrics for Product Managers](https://www.amplitude.com/blog/metrics-for-product-managers)
- [Fairness and Machine Learning](https://fairmlbook.org/)
- [Product Sense Interview Guide](https://www.productexercises.com/)
- [Case in Point: Data Science Product Sense](https://www.caseinterview.com/data-science/product-sense)

## ✅ Daily Checklist
- [ ] Studied data pipeline design concepts
- [ ] Learned about metrics and measurement frameworks
- [ ] Understood A/B testing and experimentation
- [ ] Covered data privacy, ethics, and bias
- [ ] Practiced product sense framework
- [ ] Worked through system design case studies
- [ ] Completed all 6 practice exercises
- [ ] Spent 2-3 hours total study time
- [ ] Reviewed and understood solutions
- [ ] Created flashcards for key concepts and frameworks

## 📈 Progress Tracking
**Concepts Mastered:** ⬜ Data Pipelines ⬜ Metrics ⬜ A/B Testing ⬜ Ethics & Bias ⬜ Product Sense ⬜ System Design

**Time Spent:** ______ hours  
**Difficulty Rating (1-5):** ______  
**Areas to Review Tomorrow:** ___________________________

---
*Prepare for Day 7: Mock Interview & Review*