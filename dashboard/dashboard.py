import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul dashboard
st.title("✨ Bike Sharing Dashboard")

# Memuat data dengan cache untuk efisiensi
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

# Memuat dataset gabungan
main_data = load_data('main_data.csv')

# Sidebar untuk filter
st.sidebar.header('🔍 Filter Options')

# Filter berdasarkan musim dan bulan
season_filter = st.sidebar.multiselect('Select Season Day', main_data['season_day'].unique(), main_data['season_day'].unique())
month_filter = st.sidebar.multiselect('Select Month Hour', main_data['mnth_hour'].unique(), main_data['mnth_hour'].unique())

# Tombol untuk mereset filter
if st.sidebar.button("Reset Filters"):
    season_filter = main_data['season_day'].unique()
    month_filter = main_data['mnth_hour'].unique()

# Filter data sesuai pilihan pengguna
filtered_data = main_data[(main_data['season_day'].isin(season_filter)) & (main_data['mnth_hour'].isin(month_filter))]

# Cek ketersediaan data setelah memfilter
if filtered_data.empty:
    st.warning("❌ No data available for the selected filters. Please select different options.")
else:
    # Analisis Dampak Suhu dan Kelembapan pada Penyewaan Sepeda di Musim Panas
    st.header("🌞 Impact of Temperature and Humidity on Bike Rentals During Summer")
    summer_data = filtered_data[(filtered_data['mnth_hour'] == 7) | (filtered_data['mnth_hour'] == 8)]

    # Menampilkan penyewaan maksimum di musim panas
    max_rentals_summer = summer_data['cnt_hour'].max()
    st.markdown(f"<h3 style='font-size: 24px;'>Max Rentals in Summer: {max_rentals_summer}</h3>", unsafe_allow_html=True)

    # Grafik scatter plot suhu terhadap penyewaan sepeda
    fig, ax = plt.subplots()
    sns.scatterplot(data=summer_data, x='temp_hour', y='cnt_hour', ax=ax, color='orange', s=100, edgecolor='black')
    ax.set_title("Temperature vs Bike Rentals (Summer)", fontsize=14)
    ax.set_xlabel("Temperature (Normalized)", fontsize=12)
    ax.set_ylabel("Number of Bike Rentals", fontsize=12)
    st.pyplot(fig)

    # Analisis Tren Penyewaan Sepeda Bulanan
    st.header("📈 Monthly Bike Rental Trend (January to December)")
    monthly_rentals = filtered_data.groupby('mnth_hour')['cnt_hour'].mean()

    # Menampilkan rata-rata penyewaan untuk bulan yang dipilih
    avg_rentals_current_month = monthly_rentals.mean()
    st.markdown(f"<h3 style='font-size: 24px;'>Average Rentals for Selected Months: {avg_rentals_current_month:.2f}</h3>", unsafe_allow_html=True)

    # Line chart tren bulanan
    fig2, ax2 = plt.subplots()
    monthly_rentals.plot(kind='line', ax=ax2, marker='o', color='blue', linewidth=2)
    ax2.set_title("Average Monthly Bike Rentals", fontsize=14)
    ax2.set_xlabel("Month", fontsize=12)
    ax2.set_ylabel("Average Bike Rentals", fontsize=12)
    st.pyplot(fig2)

    # Analisis Penyewaan Berdasarkan Hari Kerja dan Cuaca
    st.header("☀️ Bike Rentals by Weather and Working Days")

    # Total penyewaan untuk akhir pekan dan hari kerja
    total_weekend_rentals = filtered_data[filtered_data['workingday_hour'] == 0]['cnt_hour'].sum()
    total_weekday_rentals = filtered_data[filtered_data['workingday_hour'] == 1]['cnt_hour'].sum()
    st.markdown(f"<h3 style='font-size: 24px;'>Total Rentals on Weekends: {total_weekend_rentals}</h3>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='font-size: 24px;'>Total Rentals on Working Days: {total_weekday_rentals}</h3>", unsafe_allow_html=True)

    # Bar plot untuk penyewaan hari kerja vs akhir pekan
    fig3, ax3 = plt.subplots()
    sns.barplot(x=['Weekend', 'Working Day'], y=[total_weekend_rentals, total_weekday_rentals], ax=ax3, palette="pastel")
    ax3.set_title("Bike Rentals on Working Days vs Weekends", fontsize=14)
    ax3.set_xlabel("Day Type", fontsize=12)
    ax3.set_ylabel("Number of Rentals", fontsize=12)
    st.pyplot(fig3)

    # Heatmap untuk penyewaan rata-rata berdasarkan suhu dan kelembapan
    st.header("🌧️ Average Bike Rentals by Temperature and Humidity")
    filtered_data['temp_group'] = pd.cut(filtered_data['temp_hour'], bins=3, labels=['Low', 'Medium', 'High'])
    filtered_data['hum_group'] = pd.cut(filtered_data['hum_hour'], bins=3, labels=['Low', 'Medium', 'High'])
    avg_rental_by_temp_hum = filtered_data.groupby(['temp_group', 'hum_group'], observed=True)['cnt_hour'].mean().unstack()

    # Menampilkan rata-rata penyewaan maksimum berdasarkan kategori suhu dan kelembapan
    avg_rentals_temp_hum = avg_rental_by_temp_hum.stack().max()
    st.markdown(f"<h3 style='font-size: 24px;'>Max Average Rentals by Temperature and Humidity: {avg_rentals_temp_hum:.2f}</h3>", unsafe_allow_html=True)

    # Membuat heatmap
    fig4, ax4 = plt.subplots(figsize=(10, 6))
    sns.heatmap(avg_rental_by_temp_hum, annot=True, cmap='coolwarm', fmt=".2f", ax=ax4)
    ax4.set_title('Average Bike Rentals Based on Temperature and Humidity', fontsize=14)
    ax4.set_xlabel('Humidity Group', fontsize=12)
    ax4.set_ylabel('Temperature Group', fontsize=12)
    st.pyplot(fig4)
