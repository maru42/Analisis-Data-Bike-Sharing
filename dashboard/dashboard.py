import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the path for the dataset
DATA_PATH = 'dashboard/main_data.csv'

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv(DATA_PATH)
    return data

data = load_data()

# Title of the dashboard
st.title('Bike Rentals Analysis Dashboard')

# Display the dataset
st.write('### Dataset Preview')
st.dataframe(data.head())

# Analyzing the impact of temperature and humidity on bike rentals during the summer
st.header('1. Impact of Temperature and Humidity on Bike Rentals During Summer')

# Filter data for summer months
summer_data = data[(data['season_day'] == 'summer')]

# Create a scatter plot for temperature vs. bike rentals
fig1, ax1 = plt.subplots()
sns.scatterplot(data=summer_data, x='temp_day', y='cnt_day', hue='hum_day', ax=ax1)
ax1.set_title('Temperature vs. Bike Rentals (Summer)')
ax1.set_xlabel('Temperature (°C)')
ax1.set_ylabel('Bike Rentals')
st.pyplot(fig1)

# Analyzing bike rentals comparison between weekends and weekdays
st.header('2. Bike Rentals Comparison Between Weekends and Weekdays')

# Create a column for days
data['day_of_week'] = pd.to_datetime(data['dteday']).dt.day_name()
weekend_data = data[data['day_of_week'].isin(['Saturday', 'Sunday'])]
weekday_data = data[data['day_of_week'].isin(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])]

# Group by day type
weekend_rentals = weekend_data.groupby('day_of_week')['cnt_day'].sum().reset_index()
weekday_rentals = weekday_data.groupby('day_of_week')['cnt_day'].sum().reset_index()

# Plot comparison
fig2, ax2 = plt.subplots()
sns.barplot(data=weekend_rentals, x='day_of_week', y='cnt_day', ax=ax2, color='blue', label='Weekend')
sns.barplot(data=weekday_rentals, x='day_of_week', y='cnt_day', ax=ax2, color='orange', label='Weekday')
ax2.set_title('Bike Rentals: Weekend vs. Weekday')
ax2.set_xlabel('Day of Week')
ax2.set_ylabel('Total Bike Rentals')
ax2.legend()
st.pyplot(fig2)

# Monthly bike rental trend from January to December
st.header('3. Monthly Bike Rental Trend')

# Extract month from date
data['month'] = pd.to_datetime(data['dteday']).dt.month_name()
monthly_rentals = data.groupby('month')['cnt_day'].sum().reindex(['January', 'February', 'March', 'April', 'May', 'June',
                                                                     'July', 'August', 'September', 'October', 'November', 'December'])

# Plot the trend
fig3, ax3 = plt.subplots()
monthly_rentals.plot(kind='line', ax=ax3)
ax3.set_title('Monthly Bike Rental Trend')
ax3.set_xlabel('Month')
ax3.set_ylabel('Total Bike Rentals')
st.pyplot(fig3)

# Factors influencing bike rentals
st.header('4. Factors Influencing Bike Rentals')

# Create correlation heatmap
correlation = data.corr()
fig4, ax4 = plt.subplots()
sns.heatmap(correlation, annot=True, cmap='coolwarm', ax=ax4)
ax4.set_title('Correlation Heatmap of Factors Influencing Bike Rentals')
st.pyplot(fig4)

# Footer
st.write('### Dashboard created for bike rental analysis using Streamlit.')
