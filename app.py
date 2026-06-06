import streamlit as st

# Python biasa
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# Streamlit (tampilan website)
st.title("Kalkulator Luas")

p = st.number_input("Panjang")
l = st.number_input("Lebar")

if st.button("Hitung"):
    hasil = luas_persegi_panjang(p, l)  # fungsi Python biasa
    st.write("Luas =", hasil)

