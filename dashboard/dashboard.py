import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title for the dashboard
st.title("✨ Bike Sharing Dashboard")

# Load data with caching
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

# Load the combined dataset
main_data = load_data('dashboard/main_data.csv')

# Sidebar for filtering options
st.sidebar.header('🔍 Filter Options')

# Allow users to filter data by season or month
season_filter = st.sidebar.multiselect('Select Season Day', main_data['season_day'].unique(), main_data['season_day'].unique())
month_filter = st.sidebar.multiselect('Select Month Hour', main_data['mnth_hour'].unique(), main_data['mnth_hour'].unique())

# Filter the data based on user selection
filtered_data = main_data[(main_data['season_hour'].isin(season_filter)) & (main_data['mnth_hour'].isin(month_filter))]

# Check if there is data available after filtering
if filtered_data.empty:
    st.warning("❌ No data available for the selected filters. Please select different options.")
else:
    # Business Question 1: Impact of Temperature and Humidity on Bike Rentals (Summer)
    st.header("🌞 Impact of Temperature and Humidity on Bike Rentals During Summer")
    summer_data = filtered_data[(filtered_data['mnth_hour'] == 7) | (filtered_data['mnth_hour'] == 8)]

    # Display maximum rentals for summer data
    max_rentals_summer = summer_data['cnt_hour'].max()
    st.markdown(f"<h3 style='font-size: 24px;'>Max Rentals in Summer: {max_rentals_summer}</h3>", unsafe_allow_html=True)

    # Scatter plot for temperature vs. bike rentals
    fig, ax = plt.subplots()
    sns.scatterplot(data=summer_data, x='temp_hour', y='cnt_hour', ax=ax, color='orange', s=100, edgecolor='black')
    ax.set_title("Temperature vs Bike Rentals (Summer)", fontsize=14)
    ax.set_xlabel("Temperature (Normalized)", fontsize=12)
    ax.set_ylabel("Number of Bike Rentals", fontsize=12)
    st.pyplot(fig)

    # Business Question 2: Monthly Bike Rental Trend (January to December)
    st.header("📈 Monthly Bike Rental Trend (January to December)")
    monthly_rentals = filtered_data.groupby('mnth')['cnt'].mean()

    # Display average rentals for current month filter
    avg_rentals_current_month = monthly_rentals.mean()
    st.markdown(f"<h3 style='font-size: 24px;'>Average Rentals for Selected Months: {avg_rentals_current_month:.2f}</h3>", unsafe_allow_html=True)

    # Line chart for monthly trend
    fig2, ax2 = plt.subplots()
    monthly_rentals.plot(kind='line', ax=ax2, marker='o', color='blue', linewidth=2)
    ax2.set_title("Average Monthly Bike Rentals", fontsize=14)
    ax2.set_xlabel("Month", fontsize=12)
    ax2.set_ylabel("Average Bike Rentals", fontsize=12)
    st.pyplot(fig2)

    # Additional visualizations based on working days and weather
    st.header("☀️ Bike Rentals by Weather and Working Days")

    # Display total rentals for weekdays and weekends
    total_weekend_rentals = filtered_data[filtered_data['workingday'] == 0]['cnt'].sum()
    total_weekday_rentals = filtered_data[filtered_data['workingday'] == 1]['cnt'].sum()
    st.markdown(f"<h3 style='font-size: 24px;'>Total Rentals on Weekends: {total_weekend_rentals}</h3>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='font-size: 24px;'>Total Rentals on Working Days: {total_weekday_rentals}</h3>", unsafe_allow_html=True)

    # Bar plot for bike rentals on weekdays vs weekends
    fig3, ax3 = plt.subplots()
    sns.barplot(x='workingday', y='cnt', data=filtered_data, ax=ax3, palette="pastel")
    ax3.set_title("Bike Rentals on Working Days vs Weekends", fontsize=14)
    ax3.set_xticklabels(['Weekend', 'Working Day'], fontsize=12)
    ax3.set_xlabel("Day Type", fontsize=12)
    ax3.set_ylabel("Number of Rentals", fontsize=12)
    st.pyplot(fig3)

    # Heatmap for average rentals based on temperature and humidity
    st.header("🌧️ Average Bike Rentals by Temperature and Humidity")
    filtered_data['temp_group'] = pd.cut(filtered_data['temp'], bins=3, labels=['Low', 'Medium', 'High'])
    filtered_data['hum_group'] = pd.cut(filtered_data['hum'], bins=3, labels=['Low', 'Medium', 'High'])
    avg_rental_by_temp_hum = filtered_data.groupby(['temp_group', 'hum_group'], observed=True)['cnt'].mean().unstack()

    # Display maximum average rentals by temperature and humidity groups
    avg_rentals_temp_hum = avg_rental_by_temp_hum.stack().max()
    st.markdown(f"<h3 style='font-size: 24px;'>Max Average Rentals by Temperature and Humidity: {avg_rentals_temp_hum:.2f}</h3>", unsafe_allow_html=True)

    # Create heatmap
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    sns.heatmap(avg_rental_by_temp_hum, annot=True, cmap='coolwarm', fmt=".2f", ax=ax4)
    ax4.set_title('Average Bike Rentals Based on Temperature and Humidity', fontsize=14)
    ax4.set_xlabel('Humidity Group', fontsize=12)
    ax4.set_ylabel('Temperature Group', fontsize=12)
    st.pyplot(fig4)
