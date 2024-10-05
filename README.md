# Analisis Data Bike Sharing

## Deskripsi Proyek

Proyek ini merupakan analisis data penyewaan sepeda menggunakan dataset yang mencakup informasi harian dan per jam penyewaan sepeda. Dashboard ini dibuat menggunakan Streamlit dan ditujukan untuk memberikan wawasan mengenai pola penyewaan sepeda berdasarkan suhu, kelembapan, dan hari kerja.

## Struktur Direktori

Berikut adalah struktur direktori nya

```
submission
├───dashboard
| ├───main_data.csv
| └───dashboard.py
├───data
| ├───day.csv
| └───hour.csv
├───notebook.ipynb
├───README.md
└───requirements.txt
└───url.txt
```

## Dataset

Dataset yang digunakan dalam proyek ini adalah:
- `day.csv`: Dataset ini berisi informasi harian mengenai penyewaan sepeda, termasuk suhu, kelembapan, dan jumlah penyewaan.
- `hour.csv`: Dataset ini berisi informasi penyewaan sepeda per jam.
- `main_data.csv`: Dataset ini adalah kombinasi dari `day.csv` dan `hour.csv`, yang menyimpan informasi yang lebih terintegrasi untuk analisis dan visualisasi dalam dashboard.

## Instalasi

### 1. Setup Lingkungan di Google Colab

Pastikan untuk menginstal semua library yang diperlukan. Jalankan kode berikut di sel Colab:

```
!pip install -r requirements.txt
```

### 2. Menjalankan Dashboard
Setelah semua library terinstal, jalankan aplikasi Streamlit dengan perintah berikut:

```
!streamlit run dashboard.py & npx localtunnel --port 8501
```

### 3. Link Dashboard
Dashboard juga dapat di akses melalui [url.txt](https://github.com/maru42/Analisis-Data-Bike-Sharing/blob/main/url.txt)

## Fitur Dashboard

- Filter Berdasarkan Musim dan Bulan: Pengguna dapat memfilter data berdasarkan musim (season_day) dan bulan (mnth_hour).
- Analisis Suhu dan Kelembapan di Musim Panas: Analisis scatter plot mengenai dampak suhu terhadap penyewaan sepeda di musim panas.
- Tren Penyewaan Sepeda Bulanan: Analisis tren rata-rata penyewaan sepeda dari Januari hingga Desember.
- Penyewaan Berdasarkan Hari Kerja dan Cuaca: Analisis bar plot mengenai penyewaan di hari kerja dan akhir pekan.
- Heatmap Penyewaan Berdasarkan Suhu dan Kelembapan: Visualisasi heatmap rata-rata penyewaan sepeda berdasarkan kategori suhu dan kelembapan.
- Clustering: Penerapan teknik clustering untuk mengelompokkan data berdasarkan fitur tertentu.
