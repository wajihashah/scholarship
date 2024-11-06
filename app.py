import streamlit as st
import pandas as pd

# Load data
data = pd.read_csv('scholarships.csv')  # Load your scholarship data

st.title("Postgraduate Scholarship Finder")

# Search bar
query = st.text_input("Enter keywords (e.g., 'AI', 'USA', 'full funding'):")

# Filters
country = st.selectbox("Country", data['Country'].unique())
funding_type = st.selectbox("Funding Type", data['Funding Type'].unique())

# Filtered data
filtered_data = data[(data['Country'] == country) & (data['Funding Type'] == funding_type)]

# Display results
st.write(filtered_data)
