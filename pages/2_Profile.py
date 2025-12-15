import streamlit as st
from PIL import Image

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Developer Profile", layout="centered")

# =========================
# CSS DESIGN (SINKRONISASI TEMA PAGE 1 & PAGE 2)
# =========================
st.markdown("""
<style>
/* Background utama (Tema Hangat Page 2) */
.main {
    background-color: #fff7ed;
    color: black;
}

/* Sidebar (Warna Hangat Page 2) */
section[data-testid="stSidebar"] {
    background-color: #fef3c7;
}

/* Judul (Warna Ungu Page 2) */
h1 {
    color: #7c3aed;
    text-align: center;
    font-weight: 800;
    margin-bottom: 30px;
}

/* Card Umum */
.profile-card {
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

/* Card Anggota yang BEKERJA (Warna Biru Muda, dari Page 1) */
.working-card {
    background: #e0f2fe; 
}

/* Card Anggota yang TIDAK BEKERJA (Warna Pink Muda, dari Page 1) */
.not-working-card {
    background: #fce7f3; 
}

/* Role yang BEKERJA (Warna Biru Kuat dari Page 2) */
.role {
    font-weight: bold;
    color: #2563eb; 
}

/* Status TIDAK BEKERJA */
.not-working {
    color: #dc2626; 
    font-weight: bold;
}

/* Styling Gambar Profil (Bulat dan Border Biru dari Page 2) */
img {
    border-radius: 50%;
    border: 3px solid #93c5fd; 
    object-fit: cover;
}

/* Style untuk teks informasi profil */
.profile-info {
    line-height: 1.8;
}

/* Style untuk bullet point di penjelasan */
.explanation-content {
    padding-left: 20px;
    padding-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# =========================
# LANGUAGE SYSTEM (MENGGUNAKAN SINTAKS MARKDOWN STABIL)
# =========================
LANG = {
    "INDONESIA": {
        "title": "👥 Profil Pengembang",
        "name": "Nama",
        "sid": "NIM",
        "role": "Peran",
        "status": "Status",
        "active_role_1": "Ketua Kelompok Aljabar Linear",
        "active_role_2": "Ketua Kelompok Statistik 1",
        "not_working": "Tidak Bekerja",
        
        # --- PENJELASAN APLIKASI (STRING MARKDOWN) ---
        "how_app_works_title": "💡 Cara Kerja Aplikasi",
        "matrix_title": "1. Transformasi Matriks (Aljabar Linear)",
        "matrix_explanation": 
            "* Matriks 3x3 Homogen: Digunakan untuk mempresentasikan transformasi 2D (seperti translasi, rotasi, dan skala) sebagai perkalian matriks.\n"
            "* Transformasi Piksel: Setiap koordinat piksel (x, y) diubah menjadi vektor homogen (x, y, 1). Vektor ini dikalikan dengan matriks transformasi untuk mendapatkan koordinat baru (x', y', 1).\n"
            "* Interpolasi: Karena koordinat baru seringkali bukan bilangan bulat, teknik interpolasi (seperti remap OpenCV) digunakan untuk menentukan nilai warna piksel dari koordinat sekitarnya.",
        
        "convolution_title": "2. Filter Gambar (Konvolusi)",
        "convolution_explanation": 
            "* Kernel (Matriks Filter): Sebuah matriks kecil (misalnya 3x3 atau 5x5) yang berisi bobot (weights) tertentu. Contohnya: Kernel rata-rata untuk Blur, Kernel Laplacian untuk Sharpen.\n"
            "* Operasi Konvolusi: Kernel digeser di atas gambar. Untuk setiap piksel, nilai warna baru dihitung sebagai jumlah dari perkalian elemen Kernel dengan nilai piksel di bawah Kernel tersebut.\n"
            "* Filter Gambar: Proses ini secara efektif memodifikasi frekuensi gambar (Smoothing untuk Blur, Edge Detection/Peningkatan detail untuk Sharpen).",
        # -----------------------------------
    },
    "ENGLISH": {
        "title": "👥 Developer Profile",
        "name": "Name",
        "sid": "SID",
        "role": "Role",
        "status": "Status",
        "active_role_1": "Lead Group of Linear Algebra",
        "active_role_2": "Lead Group of Statistics 1",
        "not_working": "Not Working",
        
        # --- APP EXPLANATION (MARKDOWN STRING) ---
        "how_app_works_title": "💡 How the App Works",
        "matrix_title": "1. Matrix Transformations (Linear Algebra)",
        "matrix_explanation": 
            "* Homogeneous 3x3 Matrix: Used to represent 2D transformations (like translation, rotation, and scaling) as a single matrix multiplication.\n"
            "* Pixel Transformation: Each pixel coordinate (x, y) is converted to a homogeneous vector (x, y, 1). This vector is multiplied by the transformation matrix to yield the new coordinate (x', y', 1).\n"
            "* Interpolation: Since the new coordinates are often non-integers, interpolation techniques (like OpenCV's remap) are used to determine the pixel's color value from the surrounding coordinates.",
        
        "convolution_title": "2. Image Filtering (Convolution)",
        "convolution_explanation": 
            "* Kernel (Filter Matrix): A small matrix (e.g., 3x3 or 5x5) containing specific weights. Examples: Averaging kernel for Blur, Laplacian kernel for Sharpen.\n"
            "* Convolution Operation: The kernel is slid over the image. For each pixel, the new color value is computed as the sum of the products between the kernel elements and the pixel values underneath the kernel.\n"
            "* Image Filtering: This process effectively modifies the image's frequency (Smoothing for Blur, Edge Detection/Detail enhancement for Sharpen).",
        # -----------------------------
    }
}

language = st.sidebar.selectbox("Language", ["INDONESIA", "ENGLISH"])
TXT = LANG[language]

# =========================
# TITLE
# =========================
st.title(TXT["title"])

# =========================
# MEMBER 1 (BEKERJA)
# =========================
col1, col2 = st.columns([1,3])

with col1:
    st.image("assets/kenrick.jpg", width=140) 

with col2:
    st.markdown(f"""
    <div class="profile-card working-card">
        <div class="profile-info">
            <b>{TXT["name"]}:</b> Kenrick Sierra Kisworo<br>
            <b>{TXT["sid"]}:</b> 004202400070<br>
            <span class="role">{TXT["role"]}: {TXT["active_role_1"]}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# MEMBER 2 (BEKERJA)
# =========================
col1, col2 = st.columns([1,3])

with col1:
    st.image("assets/dicky.jpg", width=140)

with col2:
    st.markdown(f"""
    <div class="profile-card working-card">
        <div class="profile-info">
            <b>{TXT["name"]}:</b> Muhammad Dicky Ramadhan<br>
            <b>{TXT["sid"]}:</b> 00420240011<br>
            <span class="role">{TXT["role"]}: {TXT["active_role_2"]}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================
# PENJELASAN CARA KERJA APLIKASI (PERBAIKAN FINAL & STABIL)
# =========================
st.subheader(TXT['how_app_works_title'])

# --- MENGGUNAKAN METODE PEMISAHAN STABIL ---

# 1. Mulai Card (Tag <div> pembuka) dan Judul Matriks
st.markdown(f"""
<div class="profile-card working-card"> 
    <h3>{TXT['matrix_title']}</h3>
""", unsafe_allow_html=True)

# 2. Render Poin-Poin Matriks (Markdown murni)
st.markdown(TXT['matrix_explanation']) 

# 3. Lanjutkan dengan Judul Konvolusi
st.markdown(f"""
    <h3>{TXT['convolution_title']}</h3>
""", unsafe_allow_html=True)

# 4. Render Poin-Poin Konvolusi (Markdown murni)
st.markdown(TXT['convolution_explanation'])

# 5. Tutup Div Card
st.markdown("</div>", unsafe_allow_html=True)