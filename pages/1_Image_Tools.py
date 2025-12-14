import streamlit as st
import numpy as np
from PIL import Image
import cv2
import io
import time
from rembg import remove

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Image Tools", layout="centered")

# =========================
# CSS CERAH (N A M B A H  S A J A)
# =========================
st.markdown("""
<style>
.main {
    background-color: #fff7ed;
    color: black;
}

section[data-testid="stSidebar"] {
    background-color: #fef3c7;
}

h1 {
    color: #7c3aed;
}

h2, h3 {
    color: #2563eb;
}

.stButton > button,
.stDownloadButton > button {
    background: linear-gradient(90deg, #fb7185, #60a5fa, #a78bfa);
    color: black;
    font-weight: bold;
    border-radius: 12px;
}

img {
    border-radius: 16px;
    border: 2px solid #93c5fd;
}
</style>
""", unsafe_allow_html=True)

# =========================
# LANGUAGE SYSTEM (ASLI)
# =========================
LANGUAGES = {
    "INDONESIA": {
        "title": "Aplikasi Transformasi Matriks",
        "upload": "Unggah Gambar",
        "feature": "Pilih Fitur",
        "translation": "Translasi",
        "scaling": "Skala",
        "rotation": "Rotasi",
        "shearing": "Shearing",
        "reflection": "Refleksi",
        "blur": "Blur",
        "sharpen": "Sharpen",
        "bgremove": "Hapus Background",
        "processed": "Hasil",
        "original": "Gambar Asli",
        "download": "Unduh Gambar Hasil (.PNG)"
    },
    "ENGLISH": {
        "title": "Matrix Transformation App",
        "upload": "Upload Image",
        "feature": "Choose Feature",
        "translation": "Translation",
        "scaling": "Scaling",
        "rotation": "Rotation",
        "shearing": "Shearing",
        "reflection": "Reflection",
        "blur": "Blur",
        "sharpen": "Sharpen",
        "bgremove": "Background Removal",
        "processed": "Processed Image",
        "original": "Original Image",
        "download": "Download Processed Image (.PNG)"
    }
}

choice = st.sidebar.selectbox("LANGUAGE", list(LANGUAGES.keys()))
TXT = LANGUAGES[choice]

# =========================
# IMAGE HELPERS (ASLI)
# =========================
def to_numpy(img):
    return np.array(img.convert("RGB"))

def to_pil(arr):
    return Image.fromarray(np.clip(arr, 0, 255).astype("uint8"))

def download_image(img):
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

def auto_resize_for_bg_removal(pil_img, max_size=512):
    w, h = pil_img.size
    if max(w, h) <= max_size:
        return pil_img
    scale = max_size / max(w, h)
    return pil_img.resize((int(w*scale), int(h*scale)))

# =========================
# MATRIX FUNCTIONS (ASLI)
# =========================
def translation_matrix(tx, ty):
    return np.array([[1,0,tx],[0,1,ty],[0,0,1]])

def scaling_matrix(sx, sy):
    return np.array([[sx,0,0],[0,sy,0],[0,0,1]])

def rotation_matrix(angle):
    rad = np.deg2rad(angle)
    c, s = np.cos(rad), np.sin(rad)
    return np.array([[c,-s,0],[s,c,0],[0,0,1]])

def shearing_matrix(shx, shy):
    return np.array([[1,shx,0],[shy,1,0],[0,0,1]])

def reflection_matrix(axis):
    if axis == "x": return np.array([[1,0,0],[0,-1,0],[0,0,1]])
    if axis == "y": return np.array([[-1,0,0],[0,1,0],[0,0,1]])
    return np.array([[-1,0,0],[0,-1,0],[0,0,1]])

def apply_transform(img, M):
    h, w = img.shape[:2]
    ys, xs = np.indices((h,w))
    ones = np.ones_like(xs)
    coords = np.stack([xs.ravel(), ys.ravel(), ones.ravel()])
    mapped = np.linalg.inv(M) @ coords
    xmap = mapped[0].reshape(h,w).astype("float32")
    ymap = mapped[1].reshape(h,w).astype("float32")
    return cv2.remap(img, xmap, ymap, cv2.INTER_LINEAR)

# =========================
# UI (ASLI)
# =========================
st.title(TXT["title"])

uploaded = st.file_uploader(TXT["upload"], ["png","jpg","jpeg"])
if uploaded is None:
    st.stop()

image = Image.open(uploaded)
img_arr = to_numpy(image)

feature = st.sidebar.selectbox(
    TXT["feature"],
    [
        TXT["translation"], TXT["scaling"], TXT["rotation"],
        TXT["shearing"], TXT["reflection"],
        TXT["blur"], TXT["sharpen"], TXT["bgremove"]
    ]
)

processed = img_arr.copy()

# =========================
# FEATURE LOGIC (ASLI)
# =========================
if feature == TXT["translation"]:
    tx = st.sidebar.slider("tx", -200,200,0)
    ty = st.sidebar.slider("ty", -200,200,0)
    processed = apply_transform(img_arr, translation_matrix(tx,ty))

elif feature == TXT["scaling"]:
    sx = st.sidebar.slider("sx", 0.5,2.0,1.0)
    sy = st.sidebar.slider("sy", 0.5,2.0,1.0)
    cx, cy = img_arr.shape[1]/2, img_arr.shape[0]/2
    M = translation_matrix(cx,cy) @ scaling_matrix(sx,sy) @ translation_matrix(-cx,-cy)
    processed = apply_transform(img_arr, M)

elif feature == TXT["rotation"]:
    angle = st.sidebar.slider("angle", -180,180,0)
    cx, cy = img_arr.shape[1]/2, img_arr.shape[0]/2
    M = translation_matrix(cx,cy) @ rotation_matrix(angle) @ translation_matrix(-cx,-cy)
    processed = apply_transform(img_arr, M)

elif feature == TXT["shearing"]:
    shx = st.sidebar.slider("shx", -1.0,1.0,0.0)
    shy = st.sidebar.slider("shy", -1.0,1.0,0.0)
    processed = apply_transform(img_arr, shearing_matrix(shx,shy))

elif feature == TXT["reflection"]:
    axis = st.sidebar.selectbox("Axis", ["x","y","both"])
    
    cx, cy = img_arr.shape[1]/2, img_arr.shape[0]/2
    
    T_neg = translation_matrix(-cx, -cy)
    
    R = reflection_matrix(axis)
    
    T_pos = translation_matrix(cx, cy)
    
    M = T_pos @ R @ T_neg
    
    processed = apply_transform(img_arr, M)
    # ----------------------------------

elif feature == TXT["blur"]:
    kernel_size = 5
    kernel_blur = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size * kernel_size)
    
    processed = cv2.filter2D(img_arr, -1, kernel_blur)
    
elif feature == TXT["sharpen"]:
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    processed = cv2.filter2D(img_arr,-1,kernel)

elif feature == TXT["bgremove"]:
    image_proc = auto_resize_for_bg_removal(image)
    with st.spinner("Processing..."):
        processed = np.array(remove(image_proc))

# =========================
# DISPLAY
# =========================
col1, col2 = st.columns(2)
with col1:
    st.image(image, caption=TXT["original"], use_container_width=True)
with col2:
    processed_pil = to_pil(processed)
    st.image(processed_pil, caption=TXT["processed"], use_container_width=True)

st.download_button(
    TXT["download"],
    data=download_image(processed_pil),
    file_name="result.png",
    mime="image/png"
)
