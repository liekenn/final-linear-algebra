import streamlit as st

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Matrix Transformation Project",
    layout="centered"
)

# =========================
# CSS DESIGN (BRIGHT THEME)
# =========================
st.markdown("""
<style>
/* Background utama */
.main {
    background-color: #ffffff;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #fff7cc;
}

/* Judul utama */
.hero-title {
    font-size: 42px;
    font-weight: 800;
    color: #6b21a8;
    text-align: center;
    margin-top: 20px;
}

/* Subjudul */
.hero-subtitle {
    font-size: 18px;
    text-align: center;
    color: #374151;
    margin-bottom: 40px;
}

/* Card */
.card {
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.blue { background: #e0f2fe; }
.pink { background: #fce7f3; }
.yellow { background: #fef9c3; }
.purple { background: #ede9fe; }

.card h3 {
    margin-top: 0;
    color: #111827;
}

.card ul {
    padding-left: 20px;
    color: #374151;
}

/* CTA */
.cta {
    margin-top: 30px;
    padding: 16px;
    background: #dbeafe;
    border-radius: 12px;
    font-weight: 600;
    text-align: center;
    color: #1e3a8a;
}
</style>
""", unsafe_allow_html=True)

# =========================
# LANGUAGE SYSTEM
# =========================
LANG = {
    "INDONESIA": {
        "title": "Transformasi Matriks dalam Pengolahan Citra",
        "subtitle": "Aplikasi web untuk memahami penerapan Aljabar Linear pada pengolahan citra digital.",
        "features": "Fitur Aplikasi",
        "matrix": "Transformasi Matriks",
        "matrix_points": [
            "Translasi menggunakan matriks homogen 3×3",
            "Skala pada sumbu X dan Y",
            "Rotasi terhadap pusat gambar",
            "Shearing (pergeseran sudut)",
            "Refleksi terhadap sumbu"
        ],
        "image": "Image Processing",
        "image_points": [
            "Blur menggunakan kernel konvolusi",
            "Sharpen menggunakan kernel konvolusi",
            "Background removal sebagai fitur bonus"
        ],
        "profile": "Profil Pengembang",
        "profile_points": [
            "Dikembangkan oleh mahasiswa",
            "Bagian dari proyek akhir Aljabar Linear",
            "Menggunakan Python dan Streamlit"
        ],
        "cta": "Gunakan menu di sidebar untuk membuka Image Processing Tools."
    },
    "ENGLISH": {
        "title": "Matrix Transformations in Image Processing",
        "subtitle": "A web application to understand the application of Linear Algebra in digital image processing.",
        "features": "Application Features",
        "matrix": "Matrix Transformations",
        "matrix_points": [
            "Translation using 3×3 homogeneous matrix",
            "Scaling on X and Y axis",
            "Rotation around image center",
            "Shearing transformation",
            "Reflection across axis"
        ],
        "image": "Image Processing",
        "image_points": [
            "Blur using convolution kernel",
            "Sharpen using convolution kernel",
            "Background removal as bonus feature"
        ],
        "profile": "Developer Profile",
        "profile_points": [
            "Developed by university students",
            "Final project for Linear Algebra course",
            "Built using Python and Streamlit"
        ],
        "cta": "Use the sidebar menu to open Image Processing Tools."
    }
}

language = st.sidebar.selectbox("Language", ["INDONESIA", "ENGLISH"])
TXT = LANG[language]

# =========================
# HERO SECTION
# =========================
st.markdown(f'<div class="hero-title">{TXT["title"]}</div>', unsafe_allow_html=True)
st.markdown(f'<div class="hero-subtitle">{TXT["subtitle"]}</div>', unsafe_allow_html=True)

# =========================
# FEATURE SECTION
# =========================
st.subheader(f"✨ {TXT['features']}")

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="card blue">
        <h3>{TXT["matrix"]}</h3>
        <ul>
            {''.join(f'<li>{p}</li>' for p in TXT["matrix_points"])}
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card pink">
        <h3>{TXT["image"]}</h3>
        <ul>
            {''.join(f'<li>{p}</li>' for p in TXT["image_points"])}
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown(f"""
<div class="card purple">
    <h3>{TXT["profile"]}</h3>
    <ul>
        {''.join(f'<li>{p}</li>' for p in TXT["profile_points"])}
    </ul>
</div>
""", unsafe_allow_html=True)

# =========================
# CTA
# =========================
st.markdown(f"""
<div class="cta">
👉 {TXT["cta"]}
</div>
""", unsafe_allow_html=True)
