import streamlit as st
import base64
import pandas as pd
import os

def get_base64(file):
    with open(file, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg = get_base64("background.jpg")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


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

st.sidebar.title("🧪 ChemBuddy")
st.sidebar.markdown("## Pilih Menu")

if st.sidebar.button("🏠 Beranda"):
    st.session_state.menu = "Beranda"

if st.sidebar.button("🧪 Normalitas"):
    st.session_state.menu = "Normalitas"

if st.sidebar.button("⚗️ Molaritas"):
    st.session_state.menu = "Molaritas"

if st.sidebar.button("📐 BE"):
    st.session_state.menu = "BE"

if st.sidebar.button("📏 BM"):
    st.session_state.menu = "BM"

if st.sidebar.button("⚛️ Ar"):
    st.session_state.menu = "Ar"

if st.sidebar.button("🌡️ Konversi Suhu"):
    st.session_state.menu = "Konversi Suhu"

if st.sidebar.button("📊 PPM"):
    st.session_state.menu = "PPM"

if st.sidebar.button("ℹ️ About Us"):
    st.session_state.menu = "About Us"

menu = st.session_state.get("menu", "Beranda")

if menu == " Beranda":
    st.write("Selamat datang di ChemBuddy")

elif menu == "Normalitas":
    gram = st.number_input("Massa zat (gram)", min_value=0.0)
    be = st.number_input("Berat Ekivalen (BE)", min_value=0.0)
    volume = st.number_input("Volume larutan (mL)", min_value=0.0)

    if st.button("Hitung Normalitas"):
        hasil = (gram / be) / (volume / 1000)
        st.success(f"Normalitas = {hasil:.4f} grek/L")

elif menu == "Molaritas":
    gram = st.number_input("Massa zat (gram)", min_value=0.0)
    bm = st.number_input("Berat Molekul (BM)", min_value=0.0)
    volume = st.number_input("Volume larutan (mL)", min_value=0.0)

    if st.button("Hitung Molaritas"):
        hasil = (gram / bm) / (volume / 1000)
        st.success(f"Molaritas = {hasil:.4f} mol/L")

elif menu == "BE":
    bm = st.number_input("BM Senyawa", min_value=0.0)
    valensi = st.number_input("Valensi", min_value=1.0)

    if st.button("Hitung BE"):
        hasil = bm / valensi
        st.success(f"BE = {hasil:.4f} g/grek")

elif menu == "BM":
    unsur = st.selectbox("Pilih unsur", list(data_ar.keys()))
    jumlah = st.number_input("Jumlah atom", min_value=1, step=1)

    if st.button("Hitung BM"):
        hasil = data_ar[unsur] * jumlah
        st.success(f"BM = {hasil} g/mol")

elif menu == "Ar":
    unsur = st.selectbox("Pilih unsur", list(data_ar.keys()))
    st.info(f"Ar {unsur} = {data_ar[unsur]}")

elif menu == "Konversi Suhu":

    jenis = st.selectbox(
        "Konversi",
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

elif menu == "PPM":
    massa = st.number_input("Massa zat terlarut (mg)", min_value=0.0)
    volume = st.number_input("Volume larutan (L)", min_value=0.0)

    if st.button("Hitung PPM"):
        hasil = massa / volume
        st.success(f"PPM = {hasil:.4f} mg/L")

elif menu == "About Us":
    st.header("Tentang ChemBuddy")
    st.write("""
    ChemBuddy adalah kalkulator kimia digital yang membantu
    mahasiswa dan praktikan melakukan perhitungan kimia dengan cepat.
    """)
    
    if os.path.exists("feedback.csv"):
        
        df = pd.read_csv("feedback.csv")
        rata_rata = df["Rating"].mean()

    st.metric(
    "⭐ Rata-rata Rating",
    f"{rata_rata:.1f}/5"
    )
    
    st.write(df.columns)
        
   

st.caption("Bagaimana pengalaman Anda menggunakan ChemBuddy?")

rating = st.feedback("stars")

if rating is not None:

    rating_bintang = rating + 1

    st.success(f"Rating yang diberikan: {rating_bintang} ⭐")

    data = pd.DataFrame({
        "Rating": [rating_bintang]
    })

    if os.path.exists("feedback.csv"):
        data.to_csv(
            "feedback.csv",
            mode="a",
            header=False,
            index=False
        )
    else:
        data.to_csv(
            "feedback.csv",
            index=False
        )

st.markdown("""
<style>

/* Warna tombol menu sidebar */
[data-testid="stSidebar"] .stButton button {
    background-color: #4A90C2;   /* warna tombol */
    color: white;                /* warna tulisan */
    border-radius: 10px;
}

/* Saat kursor diarahkan */
[data-testid="stSidebar"] .stButton button:hover {
    background-color: #2E86C1;
    color: white;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: #003152;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
div[data-baseweb="input"] > div {
    background-color: #588BAE;
    border-radius: 10px;
}

div[data-baseweb="input"] input {
    color: #36454F;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

/* Kotak selectbox */
div[data-baseweb="select"] > div {
    background-color: #588BAE;
    color: white;
    border-radius: 10px;
}

/* Teks di dalam selectbox */
div[data-baseweb="select"] span {
    color: white;
}

</style>
""", unsafe_allow_html=True)


