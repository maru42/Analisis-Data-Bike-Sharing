import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data_path = 'dashboard/main_data.csv'
data = pd.read_csv(data_path)

# Display the title
st.title('Bike Sharing Data Analysis Dashboard')

# Show data overview
st.header('1. Data Overview')
st.write(data.head())
st.write('Total records:', len(data))

# Convert 'dteday' to datetime
data['dteday'] = pd.to_datetime(data['dteday'])

# Plotting the trend of bike rentals over time (by day)
st.header('2. Bike Rentals Trend Over Time')
daily_data = data.groupby('dteday')['cnt_day'].sum()
daily_data.plot()
plt.title('Daily Bike Rentals')
plt.xlabel('Date')
plt.ylabel('Number of Rentals')
plt.grid()
st.pyplot(plt)

# Plotting bike rentals by hour
st.header('3. Bike Rentals by Hour')
hourly_data = data.groupby('hr')['cnt_hour'].sum()
hourly_data.plot(kind='bar')
plt.title('Total Bike Rentals by Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Rentals')
plt.xticks(rotation=0)
plt.grid()
st.pyplot(plt)

# Factors influencing bike rentals
st.header('4. Factors Influencing Bike Rentals')

# Select only numeric columns for correlation
numeric_data = data.select_dtypes(include=['float64', 'int64'])

# Create correlation heatmap
correlation = numeric_data.corr()
fig4, ax4 = plt.subplots()
sns.heatmap(correlation, annot=True, cmap='coolwarm', ax=ax4)
ax4.set_title('Correlation Heatmap of Factors Influencing Bike Rentals')
st.pyplot(fig4)

# Add a section for user input to analyze bike rentals by temperature
st.header('5. Analyze Bike Rentals by Temperature')
temp_filter = st.slider('Select Temperature Range:', float(data['temp_day'].min()), float(data['temp_day'].max()), (0.0, 1.0))
filtered_data = data[(data['temp_day'] >= temp_filter[0]) & (data['temp_day'] <= temp_filter[1])]

# Plot bike rentals in the selected temperature range
st.subheader('Filtered Bike Rentals by Temperature')
filtered_data.groupby('temp_day')['cnt_day'].sum().plot()
plt.title('Total Bike Rentals by Temperature')
plt.xlabel('Temperature')
plt.ylabel('Number of Rentals')
plt.grid()
st.pyplot(plt)

# Conclusion
st.header('6. Conclusion')
st.write("This dashboard provides insights into bike rental patterns and how different factors influence rentals.")
