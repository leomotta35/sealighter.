import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Sea Lighter | Gardening & Handyman London",
    page_icon="🌿",
    layout="wide"
)

ASSETS = Path("assets")
LOGO = ASSETS / "logo.jpg"

# =============================
# CSS PROFISSIONAL
# =============================
st.markdown("""
<style>

header {visibility: hidden;}

html, body, [class*="css"]  {
    font-family: 'Segoe UI', sans-serif;
}

.hero {
    background: linear-gradient(135deg,#0f766e,#22c55e);
    padding: 80px 20px;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 40px;
}

.section {
    padding: 60px 0px;
}

.card {
    background: #f9fafb;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-5px);
}

.footer {
    text-align:center;
    padding:30px;
    font-size:0.9rem;
    color:gray;
    border-top:1px solid #eee;
    margin-top:50px;
}

/* WhatsApp Floating Button */
.whatsapp-float {
    position: fixed;
    width: 60px;
    height: 60px;
    bottom: 25px;
    right: 25px;
    background-color: #25D366;
    color: white;
    border-radius: 50px;
    text-align: center;
    font-size: 30px;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
    z-index: 100;
    display:flex;
    align-items:center;
    justify-content:center;
    text-decoration:none;
}

.whatsapp-float:hover {
    background-color: #1ebe5d;
}

</style>
""", unsafe_allow_html=True)

# =============================
# HEADER
# =============================
col1, col2 = st.columns([1,5])

with col1:
    if LOGO.exists():
        st.image(str(LOGO), width=120)

with col2:
    st.markdown("## Sea Lighter")
    st.markdown("### Professional Gardening & Handyman Services in London")

st.divider()

# =============================
# HERO
# =============================
st.markdown("""
<div class="hero">
    <h1>Transforming Gardens & Homes Across London</h1>
    <p>Reliable • Professional • Affordable</p>
    <br>
    <a href="https://wa.me/447480145752" style="background:white;color:#0f766e;padding:15px 30px;border-radius:10px;text-decoration:none;font-weight:bold;">
    Request a Free Quote
    </a>
</div>
""", unsafe_allow_html=True)

# =============================
# ABOUT SECTION
# =============================
st.markdown("## 🌿 About Sea Lighter")

st.write("""
Sea Lighter provides high-quality gardening and handyman services across London.
We pride ourselves on reliability, attention to detail, and delivering outstanding
results for residential and commercial properties.

Whether you need regular garden maintenance, landscaping improvements, or small home repairs,
we are ready to help.
""")

# =============================
# SERVICES
# =============================
st.markdown("## 🛠 Our Services")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🌿 Gardening")
    st.write("""
    • Lawn mowing  
    • Hedge trimming  
    • Weed removal  
    • Garden clearance  
    • Seasonal maintenance  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🪴 Landscaping")
    st.write("""
    • Turf installation  
    • Fence repairs  
    • Decking  
    • Patio cleaning  
    • Pressure washing  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔧 Handyman")
    st.write("""
    • General repairs  
    • Painting  
    • Furniture assembly  
    • Minor plumbing  
    • Property maintenance  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# =============================
# GALLERY
# =============================
st.markdown("## 📸 Recent Projects")

if ASSETS.exists():
    images = list(ASSETS.glob("*.jpg"))
    cols = st.columns(4)
    for i, img in enumerate(images):
        cols[i % 4].image(str(img), use_container_width=True)

# =============================
# WHY CHOOSE US
# =============================
st.markdown("## ⭐ Why Choose Sea Lighter?")

st.write("""
✔ Fully insured  
✔ Competitive pricing  
✔ Fast response time  
✔ Trusted by local London clients  
✔ 5-star service attitude  
""")

# =============================
# SERVICE AREA
# =============================
st.markdown("## 📍 Areas We Cover")

st.write("""
We proudly serve London and surrounding areas including:
Central London, South London, West London and nearby boroughs.
""")

# =============================
# FOOTER
# =============================
st.markdown("""
<div class="footer">
Sea Lighter – Gardening & Handyman Services in London<br>
© 2026 Sea Lighter. All rights reserved.
</div>
""", unsafe_allow_html=True)

# =============================
# WHATSAPP FLOAT BUTTON
# =============================
st.markdown("""
<a href="https://wa.me/447480145752" class="whatsapp-float" target="_blank">
💬
</a>
""", unsafe_allow_html=True)

