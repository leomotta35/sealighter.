import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Sea Lighter | Gardening & Handyman",
    page_icon="🌿",
    layout="wide"
)

# =============================
# CAMINHO SIMPLES (IMPORTANTE)
# =============================
ASSETS = Path("assets")
LOGO = ASSETS / "logo.jpg"

# =============================
# CSS
# =============================
st.markdown("""
<style>
header {visibility: hidden;}

.hero {
    background: linear-gradient(90deg,#0f766e,#22c55e);
    padding: 60px 20px;
    border-radius: 15px;
    text-align: center;
    color: white;
}

.footer {
    text-align:center;
    padding:20px;
    font-size:0.9rem;
    color:gray;
}
</style>
""", unsafe_allow_html=True)

# =============================
# HEADER
# =============================
col1, col2 = st.columns([1,4])

with col1:
    if LOGO.exists():
        st.image(str(LOGO), width=150)

with col2:
    st.markdown("## Sea Lighter")
    st.markdown("Gardening & Handyman Services in London")

st.divider()

# =============================
# HERO
# =============================
st.markdown("""
<div class="hero">
    <h1>Professional Gardening & Repairs</h1>
    <p>Reliable services across London</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# =============================
# SERVIÇOS
# =============================
st.markdown("## Our Services")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🌿 Gardening")
    st.write("Lawn mowing, hedge trimming, full garden care.")

with col2:
    st.subheader("🛠 Repairs")
    st.write("Home maintenance and handyman services.")

with col3:
    st.subheader("🏡 Property Care")
    st.write("Odd jobs and improvements.")

st.link_button("📞 Request a Free Quote", "https://wa.me/447480145752")

# =============================
# GALERIA AUTOMÁTICA
# =============================
st.markdown("## 🌿 Recent Work")

if ASSETS.exists():
    images = list(ASSETS.glob("*.jpg"))
    cols = st.columns(4)

    for i, img_path in enumerate(images):
        cols[i % 4].image(str(img_path), use_container_width=True)
else:
    st.warning("Assets folder not found.")

st.write("")

# =============================
# FOOTER
# =============================
st.markdown("""
<div class="footer">
Sea Lighter – Serving London and surrounding areas.<br>
Transforming London gardens, one lawn at a time.
</div>
""", unsafe_allow_html=True)
