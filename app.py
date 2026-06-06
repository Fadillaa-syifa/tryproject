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
    st.write("ChemBuddy adalah platform pembelajaran yang dirancang untuk membantu mahasiswa, khususnya tingkat pertama, dalam memahami dan menyelesaikan perhitungan dasar pada mata kuliah *Kimia Dasar* dan *Fisika Dasar*.Melalui ChemBuddy, pengguna dapat dengan mudah melakukan berbagai konversi dan perhitungan, seperti:
        * Konversi suhu
        * Berat Molekul (BM)
        * Berat Ekivalen (BE)
        * Normalitas (N)
        * Molaritas (M)
        * Parts Per Million (PPM)
        Mata kuliah Kimia Dasar,Titrimetri,dan Fisika Dasar sering menjadi tantangan bagi mahasiswa baru karena banyaknya konsep dan perhitungan yang harus dipahami. Tidak sedikit mahasiswa yang harus mengulang mata kuliah tersebut akibat kesulitan dalam memahami materi dasar. Oleh karena itu, ChemBuddy hadir sebagai solusi praktis untuk membantu proses belajar menjadi lebih mudah, cepat, dan efisien.Dengan fitur yang sederhana mudah digunakan, ChemBuddy diharapkan dapat menjadi teman belajar yang membantu mahasiswa meningkatkan pemahaman konsep serta mengurangi kesalahan dalam perhitungan.
*Belajar lebih mudah, hitung lebih cepat, bersama ChemBuddy 🧪✨")

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
    Kami adalah tim pengembang ChemBuddy, sebuah platform edukasi yang dibuat untuk membantu mahasiswa dalam memahami dan menyelesaikan berbagai perhitungan dasar pada mata kuliah Kimia Dasar, Titimetri dan Fisika Dasar.ChemBuddy hadir sebagai solusi praktis bagi mahasiswa, khususnya tingkat pertama, yang sering menghadapi kesulitan dalam melakukan konversi dan perhitungan kimia. Dengan menyediakan fitur konversi suhu, Berat Molekul (BM), Berat Ekivalen (BE), Molaritas, Normalitas, dan PPM, kami berharap dapat membantu proses belajar menjadi lebih efektif dan efisien.Website ini dikembangkan sebagai bentuk kontribusi kami dalam memanfaatkan teknologi untuk mendukung pembelajaran sains yang lebih mudah diakses dan dipahami """)

    st.write("Tim Pengembang ChemBuddy:")
    st.write("""
    1. *Asyifa Fadilla* (2460335)
    2. *Muhamad Daffa Alfath* (2460425)
    3. *Muhammad Al Fariz* (2460425)
    4. *Nadifah Adya Anggita* (2460449)
    5. *Ramdan Abdul Azis* (2460490)

    Kami percaya bahwa pembelajaran akan menjadi lebih menyenangkan ketika didukung oleh alat yang tepat. Oleh karena itu, melalui ChemBuddy kami berkomitmen untuk menghadirkan platform yang sederhana, bermanfaat, dan mudah digunakan oleh seluruh mahasiswa.

    *ChemBuddy — Your Smart Chemistry Learning Companion.* 🧪✨
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


