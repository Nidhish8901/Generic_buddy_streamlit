import streamlit as st
import base64

# === DARK/LIGHT MODE TOGGLE (stored globally) ===
if "theme" not in st.session_state:
    st.session_state["theme"] = "Light Mode"

st.session_state["theme"] = st.sidebar.radio(
    "Choose Theme",
    ("Light Mode", "Dark Mode"),
    index=0 if st.session_state["theme"] == "Light Mode" else 1,
    key="theme_radio"
)

theme = st.session_state["theme"]

# === COLOR SETUP BASED ON THEME ===
if theme == "Dark Mode":
    background = "#111111"
    text_color = "#f5f5f5"
    subtitle_color = "#cccccc"
    card_bg = "#1e1e1e"
    card_border = "#444444"
    hover_bg = "#333333"
    hover_text = "#ffffff"
else:
    background = "#f9fafa"
    text_color = "#000000"
    subtitle_color = "#444444"
    card_bg = "#ffffff"
    card_border = "#02899d"
    hover_bg = "#02899d"
    hover_text = "#ffffff"

# === Load and Encode Logo ===
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

logo_base64 = get_base64_image("logo.jpeg")

# === DYNAMIC CSS BASED ON THEME ===
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
    background-color: {background};
    color: {text_color};
}}

.moving-text-container {{
    overflow: hidden;
    white-space: nowrap;
    background: linear-gradient(90deg, #02899d, #4db6ac);
    color: white;
    padding: 12px 0;
    margin-bottom: 2rem;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}}

.moving-text {{
    display: inline-block;
    animation: scroll-left 25s linear infinite;
    font-size: 1.1rem;
    font-weight: 500;
    padding-left: 100%;
}}

@keyframes scroll-left {{
    0% {{ transform: translateX(0); }}
    100% {{ transform: translateX(-100%); }}
}}

.container {{
    max-width: 900px;
    margin: auto;
    padding: 3rem 2rem;
    text-align: center;
}}

.logo {{
    width: 160px;
    margin-bottom: 1rem;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
    border-radius: 12px;
}}

.main-title {{
    font-size: 2.5rem;
    font-weight: 700;
    color: #02899d;
    margin: 0.5rem 0;
}}

.subtitle {{
    font-size: 1.1rem;
    color: {subtitle_color};
    margin-bottom: 2.5rem;
}}

.features-title {{
    font-size: 1.4rem;
    font-weight: 600;
    margin-top: 2rem;
    margin-bottom: 1.5rem;
    color: {text_color};
}}

.feature-card {{
    background-color: {card_bg};
    border: 2px solid {card_border};
    color: {card_border};
    padding: 1.2rem 1rem;
    font-size: 1rem;
    font-weight: 600;
    border-radius: 12px;
    transition: all 0.3s ease;
    text-align: center;
    box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    text-decoration: none;
    display: block;
    cursor: pointer;
}}

.feature-card:hover {{
    background-color: {hover_bg};
    color: {hover_text};
    transform: scale(1.03);
    text-decoration: none;
}}

.feature-card:active {{
    transform: scale(0.98);
}}

.get-started {{
    text-align: left;
    margin-top: 2.5rem;
}}

.get-started h3 {{
    font-size: 1.3rem;
    color: #02899d;
}}

.get-started ul {{
    font-size: 1rem;
    color: {subtitle_color};
    margin-top: 0.5rem;
}}

.footer {{
    margin-top: 3rem;
    font-size: 0.9rem;
    color: #999;
    text-align: center;
}}

.navigation-buttons {{
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin: 2rem 0;
    flex-wrap: wrap;
}}

.nav-button, .nav-button:visited, .nav-button:link {{
    background: linear-gradient(135deg, #02899d, #4db6ac);
    color: white !important;
    padding: 12px 24px;
    border: none;
    border-radius: 25px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    text-decoration: none !important;
    display: inline-block;
    min-width: 180px;
    box-shadow: 0 4px 15px rgba(2, 137, 157, 0.3);
}}

.nav-button:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(2, 137, 157, 0.4);
    text-decoration: none;
    color: white;
}}

.nav-button:active {{
    transform: translateY(0);
}}

@media (max-width: 768px) {{
    .navigation-buttons {{
        flex-direction: column;
        align-items: center;
    }}

    .nav-button {{
        width: 100%;
        max-width: 300px;
    }}
}}
</style>

<!-- Moving text banner -->
<div class="moving-text-container">
    <div class="moving-text">
        💊 Find Generic Medicines at Affordable Prices | 📍 Locate Nearby Pharmacies | 📝 Upload Prescriptions for Easy Medicine Extraction | 🏥 Your Health, Our Priority | 💰 Save Money on Healthcare
    </div>
</div>

<div class="container">
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{logo_base64}" class="logo" />
        <div class="main-title">GenericBuddy</div>
        <div class="subtitle">
            Affordable Healthcare at Your Fingertips.<br>
            Find <b>generic alternatives</b> and <b>locate pharmacies</b> instantly.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# === NAVIGATION BUTTONS ===
st.markdown("""
<div class="navigation-buttons">
    <a href="/Generic_Medicine_Finder" target="_self" class="nav-button">
        💊 Generic Medicine Finder
    </a>
    <a href="/Pharmacy_Locator" target="_self" class="nav-button">
        📍 Pharmacy Locator
    </a>
    <a href="/Prescription_Reader" target="_self" class="nav-button">
        📝 Prescription Reader
    </a>
</div>
""", unsafe_allow_html=True)

# === GET STARTED ===
st.markdown("""
<div class="get-started">
    <h3>🚀 Get Started</h3>
    <ul>
        <li><b>Generic Medicine Finder</b>: Discover affordable alternatives to branded medicines with detailed price comparisons and savings information.</li>
        <li><b>Pharmacy Locator</b>: Find nearby pharmacies using GPS location, PIN code, or city search with interactive maps and navigation.</li>
        <li><b>Prescription Reader</b>: Upload prescription images or PDFs to automatically extract medicine names and find generic alternatives.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# === QUICK STATS ===
st.markdown(f"""
<div style="background: linear-gradient(135deg, #02899d, #4db6ac); color: white; padding: 2rem; border-radius: 15px; margin: 2rem 0; text-align: center;">
    <h3 style="color: white; margin-bottom: 1rem;">📊 Platform Statistics</h3>
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 1rem;">
        <div style="text-align: center;">
            <div style="font-size: 2rem; font-weight: 700;">1000+</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">Generic Medicines</div>
        </div>
        <div style="text-align: center;">
            <div style="font-size: 2rem; font-weight: 700;">500+</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">Pharmacies Listed</div>
        </div>
        <div style="text-align: center;">
            <div style="font-size: 2rem; font-weight: 700;">60%</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">Average Savings</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# === FOOTER ===
st.markdown("""
<div class="footer">
    Built with ❤️ by Team GenericBuddy. <br>
    <div style="margin-top: 1rem; display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 15px;">
        <span style="background: linear-gradient(135deg, #02899d, #4db6ac); color: white; padding: 5px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">👨‍💻 Nidhish</span>
        <span style="background: linear-gradient(135deg, #ff6b6b, #ff8e8e); color: white; padding: 5px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">💻 Gursidak</span>
        <span style="background: linear-gradient(135deg, #a8e6cf, #7fcdcd); color: white; padding: 5px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">👩‍💻 Varshini</span>
        <span style="background: linear-gradient(135deg, #ffd93d, #ffb347); color: white; padding: 5px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">🧑‍💻 Oindrila</span>
        <span style="background: linear-gradient(135deg, #c7a8ff, #b18cff); color: white; padding: 5px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">💻 Atharva</span>
        <span style="background: linear-gradient(135deg, #ff9a9e, #fecfef); color: white; padding: 5px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 500;">👩‍💻 Poorvi</span>
    </div>
</div>
""", unsafe_allow_html=True)
