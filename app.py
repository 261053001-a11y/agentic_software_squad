import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="Dashboard Operasional Penjualan",
    page_icon="📊",
    layout="wide"
)

# 2. Load Data
@st.cache_data
def load_data():
    df = pd.read_csv('dataset_penjualan_1000.csv')
    df['Tanggal'] = pd.to_datetime(df['Tanggal'])
    return df

df = load_data()

# 3. Sidebar Filter
st.sidebar.title("🔍 Filter Data Penjualan")

min_date = df['Tanggal'].min().date()
max_date = df['Tanggal'].max().date()

start_date, end_date = st.sidebar.date_input(
    "Rentang Tanggal",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

kategori_list = ["Semua"] + list(df['Kategori'].unique())
selected_kategori = st.sidebar.selectbox("Pilih Kategori", kategori_list)

if selected_kategori != "Semua":
    produk_list = ["Semua"] + list(df[df['Kategori'] == selected_kategori]['Produk'].unique())
else:
    produk_list = ["Semua"] + list(df['Produk'].unique())

selected_produk = st.sidebar.selectbox("Pilih Produk", produk_list)

# Filtering Data
filtered_df = df[(df['Tanggal'].dt.date >= start_date) & (df['Tanggal'].dt.date <= end_date)]

if selected_kategori != "Semua":
    filtered_df = filtered_df[filtered_df['Kategori'] == selected_kategori]

if selected_produk != "Semua":
    filtered_df = filtered_df[filtered_df['Produk'] == selected_produk]

# 4. Header & KPI Metrics
st.title("📊 Dashboard Analisis Operasional Penjualan")
st.caption("Bedah Kasus 1: Visualisasi & Data Analytics (1.000 Transaksi) Nama: HUDZAIFAH AINI, NIM : 261053001")
st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

total_revenue = filtered_df['Total Pendapatan (Rp)'].sum()
total_units = filtered_df['Jumlah Terjual'].sum()
avg_transaction = filtered_df['Total Pendapatan (Rp)'].mean() if len(filtered_df) > 0 else 0
total_transactions = len(filtered_df)

col1.metric("Total Pendapatan", f"Rp {total_revenue:,.0f}")
col2.metric("Total Unit Terjual", f"{total_units:,} unit")
col3.metric("Rata-Rata Transaksi", f"Rp {avg_transaction:,.0f}")
col4.metric("Jumlah Transaksi", f"{total_transactions:,}")

st.markdown("---")

# 5. Visualisasi Data Utama
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("📈 Tren Pendapatan Harian")
    st.caption("Waktu - Interval/Rasio: Line Chart")
    df_trend = filtered_df.groupby('Tanggal')['Total Pendapatan (Rp)'].sum().reset_index()
    fig_line = px.line(
        df_trend, 
        x='Tanggal', 
        y='Total Pendapatan (Rp)',
        title='Pergerakan Pendapatan Penjualan',
        markers=True,
        color_discrete_sequence=['#1f77b4']
    )
    fig_line.update_layout(template='plotly_white')
    st.plotly_chart(fig_line, use_container_width=True)

with row1_col2:
    st.subheader("🍰 Proporsi Pendapatan per Kategori")
    st.caption("Kategorik (Nominal): Pie Chart")
    df_cat = filtered_df.groupby('Kategori')['Total Pendapatan (Rp)'].sum().reset_index()
    fig_pie = px.pie(
        df_cat, 
        names='Kategori', 
        values='Total Pendapatan (Rp)',
        hole=0.4,
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig_pie.update_layout(template='plotly_white')
    st.plotly_chart(fig_pie, use_container_width=True)

row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("📊 Performance Produk Terjual (Unit)")
    st.caption("Kategorik (Nominal) vs Numerik Diskrit: Bar Chart")
    df_prod = filtered_df.groupby(['Produk', 'Kategori'])['Jumlah Terjual'].sum().reset_index()
    df_prod = df_prod.sort_values(by='Jumlah Terjual', ascending=True)
    fig_bar = px.bar(
        df_prod, 
        x='Jumlah Terjual', 
        y='Produk', 
        color='Kategori',
        orientation='h',
        title='Total Unit Terjual per Produk',
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig_bar.update_layout(template='plotly_white')
    st.plotly_chart(fig_bar, use_container_width=True)

with row2_col2:
    st.subheader("🔔 Distribusi Harga Produk")
    st.caption("Numerik Kontinu (Rasio): Histogram")
    fig_hist = px.histogram(
        filtered_df, 
        x='Harga (Rp)', 
        nbins=20,
        title='Distribusi Frekuensi Harga Barang',
        color_discrete_sequence=['#2ca02c']
    )
    fig_hist.update_layout(template='plotly_white')
    st.plotly_chart(fig_hist, use_container_width=True)

# 6. Tabel Data Transaksi
st.markdown("---")
st.subheader("📄 Raw Data Transaksi")
st.dataframe(filtered_df, use_container_width=True)