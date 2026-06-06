import streamlit as st

# Data Ar unsur
data_ar = {
"H": 1,
"C": 12,
"N": 14,
"O": 16,
"Na": 23,
"Mg": 24,
"Al": 27,
"Si": 28,
"P": 31,
"S": 32,
"Cl": 35.5,
"K": 39,
"Ca": 40,
"Fe": 56,
"Cu": 63.5,
"Zn": 65
}

st.set_page_config(page_title="ChemBuddy", page_icon="🧪")

st.title("🧪 ChemBuddy")
st.subheader("Kalkulator Kimia Digital")

menu = st.sidebar.selectbox(
"Pilih Menu",
["Normalitas", "Molaritas", "BE", "BM", "Ar", "Konversi Suhu", "PPM"]
)

# NORMALITAS

if menu == "Normalitas":
    gram = st.number_input("Massa zat (gram)", min_value=0.0)
    be = st.number_input("Berat Ekivalen (BE)", min_value=0.0)
    volume = st.number_input("Volume larutan (mL)", min_value=0.0)

if st.button("Hitung Normalitas"):
    hasil = (gram / be) / (volume / 1000)
    st.success(f"Normalitas = {hasil:.4f} N")

# MOLARITAS

elif menu == "Molaritas":
    gram = st.number_input("Massa zat (gram)", min_value=0.0)
    bm = st.number_input("Berat Molekul (BM)", min_value=0.0)
    volume = st.number_input("Volume larutan (mL)", min_value=0.0)

if st.button("Hitung Molaritas"):
    hasil = (gram / bm) / (volume / 1000)
    st.success(f"Molaritas = {hasil:.4f} M")

# BM

elif menu == "BM":
    unsur = st.selectbox("Pilih unsur", list(data_ar.keys()))
    jumlah = st.number_input("Jumlah atom", min_value=1, step=1)

if st.button("Hitung BM"):
    hasil = data_ar[unsur] * jumlah
    st.success(f"BM = {hasil}")

# AR

elif menu == "Ar":
    unsur = st.selectbox("Pilih unsur", list(data_ar.keys()))
    st.info(f"Ar {unsur} = {data_ar[unsur]}")

# PPM

elif menu == "PPM":
    massa = st.number_input("Massa zat terlarut (mg)", min_value=0.0)
    volume = st.number_input("Volume larutan (L)", min_value=0.0)

if st.button("Hitung PPM"):
    hasil = massa / volume
    st.success(f"PPM = {hasil:.4f}")

# BE

elif menu == "BE":
    bm = st.number_input("BM Senyawa", min_value=0.0)
    valensi = st.number_input("Valensi", min_value=1.0)

if st.button("Hitung BE"):
    hasil = bm / valensi
    st.success(f"BE = {hasil:.4f}")

# KONVERSI SUHU

elif menu == "Konversi Suhu":
    jenis = st.selectbox("Konversi",
    [
        "Celcius ke Fahrenheit",
        "Celcius ke Kelvin",
        "Fahrenheit ke Celcius",
        "Kelvin ke Celcius"
    ]
)

suhu = st.number_input("Masukkan suhu")

if st.button("Konversi"):

    if jenis == "Celcius ke Fahrenheit":
        hasil = (suhu * 9/5) + 32
        satuan = "°F"

    elif jenis == "Celcius ke Kelvin":
        hasil = suhu + 273.15
        satuan = "K"

    elif jenis == "Fahrenheit ke Celcius":
        hasil = (suhu - 32) * 5/9
        satuan = "°C"

    else:
        hasil = suhu - 273.15
        satuan = "°C"

    st.success(f"Hasil = {hasil:.2f} {satuan}")
