import pandas as pd
import numpy as np

# Set seed agar hasil data reproduksibel
np.random.seed(42)

# Definisi Produk, Kategori, Harga Standar, dan Rentang Jumlah Terjual per Transaksi
katalog_produk = {
    'Elektronik': [
        ('Laptop', 8500000, (1, 10)),
        ('Smartphone', 4500000, (1, 15)),
        ('Monitor', 2500000, (1, 8)),
        ('Headset', 350000, (2, 25)),
        ('Mouse', 150000, (5, 40))
    ],
    'Pendidikan': [
        ('Buku', 75000, (10, 120)),
        ('Novel', 85000, (5, 80)),
        ('Modul Ajar', 120000, (5, 50)),
        ('Alat Tulis Set', 45000, (15, 150)),
        ('Kamus Bahasa', 150000, (2, 30))
    ]
}

# Generate 1.000 baris transaksi
data = []
rentang_tanggal = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')

for i in range(1000):
    kategori = np.random.choice(['Elektronik', 'Pendidikan'], p=[0.45, 0.55])
    daftar_prod = katalog_produk[kategori]
    prod_selected = daftar_prod[np.random.randint(0, len(daftar_prod))]
    
    nama_produk, harga_dasar, (min_qty, max_qty) = prod_selected
    jumlah_terjual = np.random.randint(min_qty, max_qty + 1)
    tanggal = np.random.choice(rentang_tanggal)
    
    data.append({
        'Tanggal': tanggal,
        'Produk': nama_produk,
        'Kategori': kategori,
        'Harga (Rp)': harga_dasar,
        'Jumlah Terjual': jumlah_terjual
    })

# Buat DataFrame
df = pd.DataFrame(data)
df['Total Pendapatan (Rp)'] = df['Harga (Rp)'] * df['Jumlah Terjual']
df = df.sort_values('Tanggal').reset_index(drop=True)

# Simpan ke CSV
df.to_csv('dataset_penjualan_1000.csv', index=False)
print("Data sintesis 1.000 baris berhasil dibuat dan disimpan ke 'dataset_penjualan_1000.csv'!")