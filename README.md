# Amazon Customer Behavior Analysis

## Project Overview
The **Amazon Customer Behavior Analysis** project aims to understand and analyze the shopping behaviors, preferences, and satisfaction levels of Amazon customers using survey data. This analysis focuses on exploring key metrics, identifying patterns, and visualizing insights through charts and dashboards.

The project is divided into three main steps:
1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Visualizations and Insights

This README serves as a comprehensive guide to the project's objectives, methods, and outcomes.

---

## Objectives
- Clean and preprocess the survey data to ensure it is ready for analysis.
- Analyze customer demographics, shopping preferences, and satisfaction levels.
- Create meaningful visualizations to identify trends and relationships within the data.
- Provide actionable insights for improving customer satisfaction and business strategies.

---

## Dataset
**Dataset Name:** Amazon Customer Behavior Survey

**Key Features:**
- `Timestamp`: Date and time of the survey.
- `age`: Age of the customer.
- `Gender`: Gender of the customer.
- `Product_Search_Method`: Method used by the customer to search for products (e.g., search engine, website, app).
- `Personalized_Recommendation_Frequency`: Frequency of receiving personalized recommendations.
- `Add_to_Cart_Browsing`: Behavior of adding items to the cart without purchasing.
- `Review_Left`: Whether the customer left a review.
- `Review_Helpfulness`: Helpfulness of the review.
- `Shopping_Satisfaction`: Customer's satisfaction level (scale 1-5).
- `Purchase_Categories`: Categories of products purchased by the customer.

---

## Step 1: Data Cleaning
### Tasks Performed:
1. **Handling Missing Values:**
   - Replaced missing values in `Product_Search_Method` with "Unknown."
   - Converted `Timestamp` to a proper datetime format.

2. **Standardizing Data Formats:**
   - Ensured consistent formatting for Yes/No columns like `Personalized_Recommendation_Frequency` and `Add_to_Cart_Browsing`.

3. **Splitting Multi-Category Data:**
   - Processed `Purchase_Categories` column to handle multiple categories.

4. **Saving Cleaned Data:**
   - Saved the cleaned dataset for further analysis.

---

## Step 2: Exploratory Data Analysis (EDA)
### Key Questions Answered:
1. **What is the age distribution of respondents?**
   - Analyzed the age distribution to understand the target audience demographics.

2. **What is the gender breakdown of respondents?**
   - Visualized gender proportions to ensure representative insights.

3. **How does age relate to shopping satisfaction?**
   - Investigated the relationship between customer age and satisfaction levels.

4. **What are the most popular product categories?**
   - Identified frequently purchased product categories.

5. **What methods do customers use to search for products?**
   - Explored search preferences like apps, search engines, and websites.

6. **How frequently do customers add items to the cart without purchasing?**
   - Analyzed cart abandonment behaviors.

7. **What is the correlation between various numerical features?**
   - Created a correlation heatmap to uncover relationships between age, review importance, and satisfaction.

---

## Step 3: Visualizations and Dashboards
### Sample Visualizations:
1. **Age Distribution:**
   - Used a histogram with a KDE (Kernel Density Estimate) overlay.

2. **Gender Breakdown:**
   - Created a pie chart to show the proportion of male and female respondents.

3. **Age vs. Shopping Satisfaction:**
   - Used a scatter plot to show trends between age and satisfaction levels.

4. **Popular Purchase Categories:**
   - Displayed a horizontal bar chart to rank product categories.

5. **Product Search Methods:**
   - Visualized search preferences with a horizontal count plot.

6. **Correlation Heatmap:**
   - Highlighted relationships between key numerical features in the dataset.

---

## Insights
- **Age Distribution:** The majority of respondents were between 25-40 years old, indicating that this is the primary customer demographic.
- **Gender Breakdown:** The gender distribution showed near-equal representation, ensuring balanced insights.
- **Product Categories:** Electronics and Fashion were the most popular categories among respondents.
- **Shopping Satisfaction:** Customers aged 30-45 showed higher satisfaction levels, suggesting targeted campaigns for this age group.
- **Search Methods:** Most customers used mobile apps to search for products, indicating the importance of app optimization.

---

## Tools and Technologies Used
- **Programming Language:** Python
- **Libraries:**
  - `pandas`: For data manipulation and cleaning.
  - `matplotlib` and `seaborn`: For creating visualizations.
  - `collections.Counter`: For processing categorical data.

---

## How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/username/amazon-customer-analysis.git
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Place the dataset in the `data/` directory.

4. Run the Python scripts:
   ```bash
   python analysis.py
   ```

5. View the visualizations and dashboards generated in the `output/` folder.

---

## Future Work
- Integrate machine learning models to predict customer satisfaction.
- Develop interactive dashboards using tools like Tableau or Plotly.
- Explore additional datasets for a broader analysis.

---

## License
The dataset used in this project was sourced from Kaggle ([Amazon consumer Behaviour Dataset]). Please refer to the licensing terms on the Kaggle dataset page for any restrictions or conditions related to its use.

---

Thank you for exploring the Amazon Customer Behavior Analysis project!

