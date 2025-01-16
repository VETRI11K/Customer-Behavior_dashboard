import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data from the CSV file
data = pd.read_csv("C:/Users/Lenovo/Documents/CSV_EXCEL/Cleaned_Amazon_Customer_Behavior.csv")

# Check for numerical columns for the correlation heatmap
numerical_cols = data.select_dtypes(include=['float64', 'int64']).columns

# Q2: Gender Breakdown
fig, ax = plt.subplots(figsize=(6, 4))
sns.countplot(x='Gender', data=data, palette='viridis', hue='Gender', dodge=False, legend=False, ax=ax)
ax.set_title('Gender Breakdown')
ax.set_xlabel('Gender')
ax.set_ylabel('Count')
st.pyplot(fig)

# Q3: Age vs. Shopping Satisfaction
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(x='age', y='Shopping_Satisfaction', hue='Gender', data=data, palette='pastel', ax=ax)
ax.set_title('Age vs. Shopping Satisfaction')
ax.set_xlabel('Age')
ax.set_ylabel('Shopping Satisfaction')
st.pyplot(fig)

# Q5: Product Search Methods
search_counts = data['Product_Search_Method'].value_counts()
fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(search_counts, labels=search_counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
ax.set_title('Product Search Methods')
st.pyplot(fig)

# Q6: Add to Cart Behavior
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(x='Add_to_Cart_Browsing', data=data, hue='Add_to_Cart_Browsing', palette='Set2', legend=False, ax=ax)
ax.set_title('Frequency of Adding Items to Cart Without Purchase')
ax.set_xlabel('Add to Cart Behavior')
ax.set_ylabel('Count')
st.pyplot(fig)

# Q7: Shopping Satisfaction Distribution
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(x='Shopping_Satisfaction', data=data, palette='viridis', ax=ax)
ax.set_title('Shopping Satisfaction Levels')
ax.set_xlabel('Shopping Satisfaction (1-5)')
ax.set_ylabel('Count')
st.pyplot(fig)

# Q8: Correlation Between Satisfaction and Other Factors
fig, ax = plt.subplots(figsize=(8, 6))
corr = data[numerical_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
ax.set_title('Correlation Heatmap of Numerical Features')
st.pyplot(fig)

# Q10: Personalized Recommendations and Satisfaction
fig, ax = plt.subplots(figsize=(8, 5))
sns.boxplot(x='Personalized_Recommendation_Frequency', y='Shopping_Satisfaction', data=data, palette='coolwarm', ax=ax)
ax.set_title('Personalized Recommendations vs. Shopping Satisfaction')
ax.set_xlabel('Personalized Recommendations')
ax.set_ylabel('Shopping Satisfaction')
st.pyplot(fig)
