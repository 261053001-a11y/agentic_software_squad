# 📊 Dashboard Analisis Operasional Penjualan

> **Bedah Kasus 1: Visualisasi & Data Analytics (1.000 Transaksi)**  
> **Nama:** Hudzaifah Aini  
> **NIM:** 261053001  

Aplikasi *Dashboard* interaktif berbasis web yang dibangun menggunakan **Streamlit**, **Pandas**, dan **Plotly** untuk menganalisis data operasional penjualan dari 1.000 data transaksi sintetis.

---

## 🚀 Fitur Utama Dashboard
1. **Filter Data Interaktif (Sidebar):**
   - Rentang Tanggal (Date Range Picker)
   - Kategori Produk (Elektronik & Pendidikan)
   - Produk Spesifik
2. **Metrik KPI Utama:**
   - Total Pendapatan (Rp)
   - Total Unit Terjual
   - Rata-Rata Pendapatan per Transaksi
   - Jumlah Total Transaksi
3. **Visualisasi Data Interaktif (Plotly):**
   - 📈 **Tren Pendapatan Harian** (*Line Chart*)
   - 🍰 **Proporsi Pendapatan per Kategori** (*Donut Chart*)
   - 📊 **Performance Produk Terjual** (*Horizontal Bar Chart*)
   - 🔔 **Distribusi Harga Produk** (*Histogram*)
4. **Tabel Data Mentah (*Raw Data Table*):** Menampilkan detail transaksi yang dapat difilter secara dinamis.

---

## 📁 Struktur File Repository
- `app.py`: File utama untuk menjalankan aplikasi antarmuka *dashboard* Streamlit.
- `data.py`: Skrip Python untuk menghasilkan data sintetis (*dataset_penjualan_1000.csv*) secara otomatis dan reproduksibel.
- `dataset_penjualan_1000.csv`: Berkas data transaksi penjualan (1.000 baris).
- `requirements.txt`: Daftar pustaka/dependencies yang dibutuhkan untuk menjalankan project.

---

## 🛠️ Cara Menjalankan Project

1. **Clone repository ini atau unduh file project.**
2. **Install semua *dependencies* yang diperlukan:**
   ```bash
   pip install -r requirements.txt
