import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set the page title
st.title("Bike Rental Data Analysis Dashboard")

# Load the data
data_file = 'dashboard/main_data.csv'

# Check if the file exists and is not empty
if os.path.exists(data_file) and os.path.getsize(data_file) > 0:
    try:
        data = pd.read_csv(data_file)

        # Display the first few rows of the dataframe
        st.subheader("Data Overview")
        st.write(data.head())

        # Data Preprocessing
        data['dteday'] = pd.to_datetime(data['dteday'], errors='coerce')
        data['hour'] = pd.to_datetime(data['hr'], format='%H', errors='coerce').dt.hour
        
        # Sidebar for user inputs
        st.sidebar.header("User Inputs")

        # Select the month
        month = st.sidebar.selectbox('Select Month:', data['mnth_hour'].unique())

        # Filter data based on the selected month
        filtered_data = data[data['mnth_hour'] == month]

        # Business Question 1: Impact of temperature and humidity on bike rentals during the summer
        st.subheader("Impact of Temperature and Humidity on Bike Rentals During Summer")
        
        # Filter for summer months (June, July, August)
        summer_data = data[data['mnth_hour'].isin([6, 7, 8])]

        # Create a scatter plot for summer data
        fig1, ax1 = plt.subplots(figsize=(10, 5))
        sns.scatterplot(data=summer_data, x='temp_hour', y='cnt_hour', hue='hum_hour', palette='viridis', ax=ax1, alpha=0.6)
        ax1.set_title('Summer: Temperature vs. Bike Rentals')
        ax1.set_xlabel('Temperature (°C)')
        ax1.set_ylabel('Number of Rentals')
        st.pyplot(fig1)

        # Business Question 2: Monthly bike rental trend
        st.subheader("Monthly Bike Rental Trend")
        monthly_rentals = data.groupby('mnth_hour')['cnt_hour'].sum().reset_index()
        fig2, ax2 = plt.subplots(figsize=(10, 5))
        sns.lineplot(data=monthly_rentals, x='mnth_hour', y='cnt_hour', marker='o', ax=ax2)
        ax2.set_title('Monthly Bike Rental Trend')
        ax2.set_xlabel('Month')
        ax2.set_ylabel('Total Rentals')
        st.pyplot(fig2)

        # Display statistics
        st.subheader("Statistics")
        st.write(filtered_data.describe())

    except pd.errors.EmptyDataError:
        st.error("No columns to parse from the file. Please check the file format.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.error("Data file is missing or empty. Please check the file path and content.")

# Show a message at the end
st.sidebar.text("Analyze your bike rental data effectively!")
