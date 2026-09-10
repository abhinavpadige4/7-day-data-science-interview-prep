# 📊 Day 5: Data Visualization

**Date:** 2026-09-15 | **Time:** 2-3 hours | **Focus:** Creating effective visualizations and communicating insights

## 🎯 Learning Objectives
By the end of today, you should be able to:
- Choose the right visualization for different data types and insights
- Create publication-quality plots using Matplotlib and Seaborn
- Build interactive visualizations with Plotly/Bokeh (conceptual)
- Tell compelling data stories through visualization
- Design effective dashboards
- Avoid common visualization pitfalls

## 📚 Key Topics to Cover

### 1. Visualization Principles (30 min)
- Data-ink ratio and chartjunk (Tufte principles)
- Choosing appropriate chart types based on data and message
- Color theory and usage in visualization
- Typography and labeling best practices
- Accessibility considerations (color blindness, etc.)
- Honesty in visualization: avoiding misleading representations

### 2. Matplotlib Fundamentals (40 min)
- Figure and axes objects
- Basic plot types: line, scatter, bar, histogram
- Customizing plots: labels, titles, legends, grids
- Subplots and complex layouts
- Saving figures in different formats
- Styles and themes

### 3. Seaborn for Statistical Visualization (40 min)
- Seaborn vs Matplotlib: when to use each
- Distribution plots: histograms, KDE, box plots, violin plots
- Categorical plots: bar plots, count plots, point plots, box plots
- Regression plots: lmplot, residplot
- Matrix plots: heatmaps, clustermaps
- Grids: FacetGrid, PairGrid
- Color palettes and styling

### 4. Interactive Visualization Concepts (25 min)
- Introduction to Plotly and Bokeh
- Basic interactivity: hover, zoom, pan
- Linked brushing and filtering
- Dashboards and web deployment
- When to use interactive vs static visualizations

### 5. Specialized Visualizations (20 min)
- Time series visualization
- Geospatial visualization (basics)
- Network graphs
- Text visualization (word clouds, etc.)
- High-dimensional data visualization (parallel coordinates, etc.)

### 6. Data Storytelling & Dashboard Design (25 min)
- Structure of a data story: setup, conflict, resolution
- Storyboarding and narrative flow
- Dashboard design principles: KPIs, layout, interactivity
- Tools for dashboarding: Tableau, Power BI, Dash, Streamlit (conceptual)
- Case studies of effective data stories

## 🔧 Practice Exercises

### Exercise 1: Matplotlib Basics (30 min)
**Scenario:** Visualize the relationship between advertising spend and sales.

**Tasks:**
1. Create a line plot showing sales over time
2. Create a scatter plot of advertising spend vs sales with regression line
3. Create a bar chart comparing sales across different regions
4. Create a histogram of sales distribution
5. Customize all plots with proper labels, titles, legends, and colors
6. Save plots in PNG and PDF formats
7. Create a figure with subplots showing all four plot types together

### Exercise 2: Seaborn Statistical Plots (35 min)
**Scenario:** Analyze the Iris dataset to understand flower characteristics.

**Tasks:**
1. Load the Iris dataset (built into Seaborn or from sklearn)
2. Create a pair plot to show relationships between all variables
3. Create a violin plot showing petal length distribution by species
4. Create a box plot showing sepal width by species with outliers highlighted
5. Create a heatmap of the correlation matrix
6. Create a FacetGrid showing histograms of each variable split by species
7. Apply a custom color palette and style to all plots

### Exercise 3: Time Series Visualization (25 min)
**Scenario:** Analyze website traffic data over a year.

**Tasks:**
1. Load timestamped website traffic data (synthetic or real)
2. Create a line plot showing daily traffic over time
3. Add moving averages (7-day and 30-day) to the plot
4. Highlight weekends and holidays differently
5. Create a calendar heatmap showing traffic patterns
6. Create a decomposition plot showing trend, seasonality, and residuals
7. Create an interactive version with Plotly (conceptual - describe how you would make it interactive)

### Exercise 4: Categorical & Geospatial Visualization (20 min)
**Scenario:** Visualize customer demographics and geographic distribution.

**Tasks:**
1. Create a count plot showing distribution of customers by age group
2. Create a bar chart showing average purchase amount by membership tier
3. Create a pie chart (or better, a waffle chart) showing market share by region
4. Create a basic scatter plot of customer locations (latitude vs longitude)
5. Create a choropleth map showing customer density by state (conceptual - describe tools)
6. Create a visualization showing customer journey stages

### Exercise 5: Dashboard Design (20 min)
**Scenario:** Design an executive dashboard for a retail company.

**Tasks:**
1. Identify 4-5 key metrics for the dashboard (sales, profit, customer count, etc.)
2. Sketch a layout for the dashboard (where each chart goes)
3. Choose appropriate visualization types for each metric
4. Describe how interactivity would work (filters, drill-downs)
5. Identify potential pitfalls to avoid
6. Describe how you would tell a story with this dashboard

## 💻 Coding Practice (Optional - 15 min)
Create a Python script that:
- Generates sample data for at least two different scenarios
- Creates at least three different types of visualizations
- Applies proper styling and labeling
- Saves the visualizations to files

## 📝 Reflection Questions
1. When would you use a box plot vs a violin plot?
2. How do you choose between a bar chart and a histogram?
3. What are the advantages and disadvantages of using pie charts?
4. How do you handle overplotting in scatter plots?
5. When would you choose a logarithmic scale?
6. How do you ensure your visualizations are accessible to color-blind viewers?
7. What makes a visualization "telling a story" vs just showing data?

## 🔗 Today's Resources
- [Edureka Visualization Section](https://www.edureka.co/blog/interview-questions/data-science-interview-questions#visualization)
- [TryExponent Visualization Guide](https://www.tryexponent.com/blog/data-science-interview-questions#visualization)
- [Matplotlib Tutorial](https://matplotlib.org/stable/tutorials/index.html)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Python Graph Gallery](https://www.python-graph-gallery.com/)
- [Data to Viz](https://www.data-to-viz.com/)
- [Storytelling with Data](https://www.storytellingwithdata.com/)
- [Plotly Documentation](https://plotly.com/python/)
- [Alberto Cairo's The Functional Art](https://www.thefunctionalart.com/)

## ✅ Daily Checklist
- [ ] Studied visualization principles
- [ ] Mastered Matplotlib basics
- [ ] Learned Seaborn for statistical visualization
- [ ] Understood interactive visualization concepts
- [ ] Covered specialized visualizations
- [ ] Practiced data storytelling and dashboard design
- [ ] Completed all 5 practice exercises
- [ ] Spent 2-3 hours total study time
- [ ] Reviewed and understood solutions
- [ ] Created flashcards for key visualization concepts and functions

## 📈 Progress Tracking
**Concepts Mastered:** ⬜ Visualization Principles ⬜ Matplotlib ⬜ Seaborn ⬜ Interactive Viz ⬜ Specialized Viz ⬜ Data Storytelling

**Time Spent:** ______ hours  
**Difficulty Rating (1-5):** ______  
**Areas to Review Tomorrow:** ___________________________

---
*Prepare for Day 6: System Design & Product Sense*