import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the title of the dashboard
st.title("Bike Rentals Data Analysis Dashboard")

# Load the dataset
data_path = "dashboard/main_data.csv"
data = pd.read_csv(data_path)

# Display the first few rows of the dataset
st.subheader("Dataset Overview")
st.write(data.head())

# Data Preprocessing
# Convert date columns to datetime
data['dteday'] = pd.to_datetime(data['dteday'])
data['instant_hour'] = data['instant_hour'].astype(int)

# Display statistics
st.subheader("Data Statistics")
st.write(data.describe())

# Business Question 1: Impact of temperature and humidity on bike rentals during summer
st.subheader("Impact of Temperature and Humidity on Bike Rentals in Summer")

# Filter data for summer months (July and August)
summer_data = data[data['mnth_hour'].isin([7, 8])]

# Create scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=summer_data, x='temp_hour', y='cnt_hour', hue='hum_hour', palette='viridis', alpha=0.6)
plt.title("Bike Rentals vs Temperature and Humidity (July and August)")
plt.xlabel("Temperature")
plt.ylabel("Number of Rentals")
plt.colorbar(label='Humidity')
st.pyplot(plt)

# Business Question 2: Monthly bike rental trend
st.subheader("Monthly Bike Rental Trend")

# Group data by month and sum the counts
monthly_trend = data.groupby('mnth_day')['cnt_day'].sum().reset_index()

# Create line plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_trend, x='mnth_day', y='cnt_day', marker='o')
plt.title("Monthly Bike Rental Trend (January to December)")
plt.xlabel("Month")
plt.ylabel("Total Rentals")
plt.xticks(ticks=monthly_trend['mnth_day'], labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], rotation=45)
st.pyplot(plt)

# Show additional insights or visualizations as needed
# For example: Rental trends by weekday
st.subheader("Bike Rentals by Weekday")

# Group data by weekday
weekday_trend = data.groupby('weekday_day')['cnt_day'].sum().reset_index()

# Create bar plot
plt.figure(figsize=(10, 6))
sns.barplot(data=weekday_trend, x='weekday_day', y='cnt_day', palette='coolwarm')
plt.title("Total Bike Rentals by Weekday")
plt.xlabel("Weekday")
plt.ylabel("Total Rentals")
st.pyplot(plt)

# Show the dashboard
if __name__ == "__main__":
    st.run()
