import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Sea Lighter | Premium Gardening & Handyman London",
    page_icon="🌿",
    layout="wide"
)

# =============================
# CONFIGURAÇÕES
# =============================
ASSETS = Path("assets")
LOGO = ASSETS / "logo.jpg"

WHATSAPP_LINK = "https://wa.me/447480145752?text=Hello%2C%20I%20would%20like%20to%20request%20a%20quotation%20for%20your%20gardening%20and%20handyman%20services.%20Could%20you%20please%20provide%20more%20details%20about%20availability%20and%20pricing%3F"

INSTAGRAM_LINK = "https://www.instagram.com/sea_lighter?igsh=MTgxMGt5ZmRteW5hYg=="

# =============================
# CSS PREMIUM
# =============================
st.markdown("""
<style>

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

.hero {
    background: linear-gradient(135deg,#0f172a,#0f766e);
    padding: 100px 20px;
    border-radius: 25px;
    text-align: center;
    color: white;
    margin-bottom: 40px;
}

.hero h1 {
    font-size: 48px;
    font-weight: 700;
}

.hero p {
    font-size: 20px;
    opacity: 0.9;
}

.hero .cta {
    margin-top: 25px;
    font-size: 18px;
    font-weight: 500;
}

.card {
    background: white;
    padding: 35px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    transition: 0.3s ease;
    height: 100%;
}

.card:hover {
    transform: translateY(-8px);
}

.footer {
    text-align:center;
    padding:40px;
    font-size:0.9rem;
    color:#888;
    margin-top:80px;
    border-top:1px solid #eee;
}

/* WhatsApp Float */
.whatsapp-float {
    position: fixed;
    width: 65px;
    height: 65px;
    bottom: 25px;
    right: 25px;
    background-color: #25D366;
    color: white;
    border-radius: 50px;
    font-size: 28px;
    display:flex;
    align-items:center;
    justify-content:center;
    box-shadow: 0 5px 20px rgba(0,0,0,0.2);
    z-index: 100;
    text-decoration:none;
}

/* Instagram Button */
.instagram-btn {
    display:inline-block;
    padding:14px 30px;
    border-radius:12px;
    background: linear-gradient(45deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888);
    color:white;
    text-decoration:none;
    font-weight:600;
    margin-top:20px;
}

</style>
""", unsafe_allow_html=True)

# =============================
# HEADER
# =============================
col1, col2 = st.columns([1,6])

with col1:
    if LOGO.exists():
        st.image(str(LOGO), width=110)

with col2:
    st.markdown("## Sea Lighter")
    st.markdown("Premium Gardening & Property Maintenance in London")

st.divider()

# =============================
# HERO SECTION
# =============================
st.markdown(f"""
<div class="hero">
    <h1>Exceptional Gardens. Flawless Maintenance.</h1>
    <p>Professional Gardening & Handyman Services Across London</p>
    <div class="cta">
        Contact us today – <a href="{WHATSAPP_LINK}" style="color:white;font-weight:bold;text-decoration:underline;">click here</a> to request your professional quotation.
    </div>
</div>
""", unsafe_allow_html=True)

# =============================
# ABOUT
# =============================
st.markdown("## About Sea Lighter")
st.write("""
Sea Lighter delivers high-end gardening and handyman services tailored for
London homeowners and property managers. Our approach combines reliability,
attention to detail, and premium finishing standards.
""")

# =============================
# SERVICES
# =============================
st.markdown("## Our Services")

services = {
    "Gardening": [
        "Lawn maintenance",
        "Hedge trimming",
        "Garden clearance",
        "Seasonal garden care"
    ],
    "Landscaping": [
        "Turf installation",
        "Decking & fencing",
        "Patio restoration",
        "Pressure washing"
    ],
    "Handyman": [
        "General repairs",
        "Interior & exterior painting",
        "Furniture assembly",
        "Property maintenance"
    ]
}

cols = st.columns(3)
for col, (title, items) in zip(cols, services.items()):
    with col:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader(title)
        for item in items:
            st.write(f"• {item}")
        st.markdown('</div>', unsafe_allow_html=True)

# =============================
# ORGANIZED GALLERY
# =============================
st.markdown("## Recent Projects")

if ASSETS.exists():
    images = sorted(ASSETS.glob("work*.jpg"))
    rows = [images[i:i+4] for i in range(0, len(images), 4)]
    for row in rows:
        cols = st.columns(len(row))
        for col, img in zip(cols, row):
            col.image(str(img), use_container_width=True)

# =============================
# INSTAGRAM SECTION
# =============================
st.markdown("## Follow Our Work")
st.markdown(f"""
<a href="{INSTAGRAM_LINK}" 
class="instagram-btn" target="_blank">
Follow Sea Lighter on Instagram
</a>
""", unsafe_allow_html=True)

# =============================
# FOOTER
# =============================
st.markdown("""
<div class="footer">
Sea Lighter – Premium Gardening & Handyman Services in London<br>
© 2026 Sea Lighter. All rights reserved.
</div>
""", unsafe_allow_html=True)

# =============================
# WHATSAPP FLOAT BUTTON COM LOGO
# =============================
st.markdown(f"""
<a href="{WHATSAPP_LINK}" class="whatsapp-float" target="_blank">
<img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" style="width:32px;height:32px;">
</a>
""", unsafe_allow_html=True)
