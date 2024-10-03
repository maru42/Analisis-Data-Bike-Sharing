# Analisis Data Bike Sharing

## Deskripsi Proyek

Proyek ini merupakan analisis data penyewaan sepeda menggunakan dataset yang mencakup informasi harian dan per jam penyewaan sepeda. Dashboard ini dibuat menggunakan Streamlit dan ditujukan untuk memberikan wawasan mengenai pola penyewaan sepeda berdasarkan suhu, kelembapan, dan hari kerja.

## Struktur Direktori

Berikut adalah struktur direktori nya

```
submission
├───dashboard
| ├───data.csv
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

Setelah blok kode diatas dijalankan, copy Exterbak URL lalu klik link "your url is"
