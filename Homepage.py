import streamlit as st

st.set_page_config(
    page_title="Datmin - Deployment",
    page_icon="📊",
)

st.sidebar.success("Pilih page di atas.")

st.title("Prediksi Minat Mahasiswa Dalam Menentukan Karir Berwirausaha Untuk Mendorong Transformasi Ekonomi")
st.image("Images/homepage.png", use_column_width=True)

st.write("""
         
    Saat ini, kesadaran akan penting kewirausahaan terutama dalam menciptakan lapangan pekerjaan dan menggerakkan roda ekonomi 
    semakin meningkat dan diperlukan upaya lebih terfokus untuk mendukung calon wirausahawan, terutama di kalangan mahasiswa, 
    guna mencapai pertumbuhan ekonomi yang berkelanjutan. Dengan tingkat pengangguran tinggi dan tantangan ekonomi yang terus 
    berkembang, penting untuk memperkuat ekosistem kewirausahaan. 

         
    Hal ini membutuhkan pemahaman yang mendalam tentang faktor-faktor yang memengaruhi mahasiswa untuk memilih jalur kewirausahaan 
    dan identifikasi potensi wirausahawan di antara mereka. Sehingga perlu dilakukan analisis prediksi apakah mahasiswa tersebut berpotensi 
    menjadi wirausahawan atau tidak berdasarkan pola atau faktor yang mempengaruhinya dengan tujuan utama untuk untuk menciptakan 
    peluang kerja dan mendorong pertumbuhan ekonomi yang berkelanjutan demi transformasi ekonomi di masa depan.
         
    ## Tentang Dashboard 🤔
    Dashboard ini dirancang agar dapat memungkinkan semua orang untuk melihat informasi dan analisis prediksi terkait dengan
    minat mahasiswa dalam menentukan karir berwirausaha untuk mendorong transformasi ekonomi. Dengan dibuatnya dashboard ini,
    akan mendapatkan informasi sebagai berikut.
    - Melihat visualisasi yang insighful terkait faktor-faktor yang mempengaruhi prediksi minat mahasiswa dalam menentukan karir berwirausaha.
    - Melihat hasil analisis prediksi apakah mahasiswa tersebut berpotensi menjadi wirausahawan atau tidak berdasarkan faktor yang mempengaruhinya.

    ## Daftar Menu Dashboard 📋
    1. 🏠 Homepage
    2. 📊 Visualisasi Data
    3. 📝 Analisis Prediksi

    """)
