# 📝 Changelog – Pharmacy Locator

All notable changes to this project are documented here.

---
## [v1.6.0] – 2025-07-09

### ✨ Added
- 🎚️ **Theme Toggle**: Users can now switch between **Light Mode** and **Dark Mode** for improved accessibility and preference.
- 🧪 **Formulation Filter**: Introduced a dropdown to filter results by **Pure**, **Mixed**, or **All** formulation types.
- ✍️ **Improved Typography**: Side effects are now shown in a **smaller font** compared to uses, for better visual hierarchy and readability.
- 🩺 **Ailment-Based Search**: Users can now enter a health condition (e.g., diabetes, fever) and see relevant medicines associated with it.

## [v1.5.0] – 2025-07-08

### ✨ Added
- 🏠 **New Home Page**: Redesigned landing page for a better first-time user experience.
- 📊 **Medical Insights (Infographics)**: Added a new section with dynamic visualizations and insights for selected medicines.
- 💵 **Price Comparison Graph**: Clicking on a medicine now shows a **bar chart** comparing prices across brands and generics.
- 🥧 **Savings Pie Chart**: A **pie chart** displays the percentage savings when choosing generic over branded.
- 🧪 **Top Formulations Display**: Shows the top formulations related to the selected medicine category, helping users understand popular options.

---

## [v1.4.0] – 2025-06-28

### ✨ Added
- 🧭 **Directions to Pharmacy**: Clicking a pharmacy name now opens **Google Maps** directions from the **user's current location** to the selected pharmacy.
- 🧾 **Prescription Search**: Users can now enter a **prescription or list of drugs**, and the app intelligently extracts and matches branded and generic medicines from the dataset.

### 🛠 Changed
- 🖱️ **Interactive Pharmacy Names**: Pharmacy results are now clickable, improving UX and enabling direct navigation.
- ⚙️ **Search Optimization**: Enhanced backend logic to handle multi-drug queries and match prescription entries with improved speed and accuracy.

---

## [v1.3.0] – 2025-06-27

### ✨ Added
- 🔍 **Search Button**: Users must now click **Search** to run the query, preventing accidental auto-refresh and improving control.
- 🧼 **Clear Filters Button**: Quickly resets all entered filters including PIN, area, city, and geolocation.

### 🛠 Changed
- 🧭 **Location Marker**: A **distinct red pin** now marks the user's **current location** on the map for better clarity.
- 🧮 **Database Update**: Cleaned to include **only generic medicine stores**, improving result accuracy.
- 🧹 **UI Simplification**: Removed the *Local / Chain* filter as it’s no longer relevant with a purely generic store database.
- 🎯 **Search Logic**: Modified to use `st.session_state` for search trigger persistence. Replaced deprecated `st.experimental_rerun()` with `st.rerun()` for compatibility with Streamlit 1.32+.
- 💥 **Safety Patch**: Fixed crash when `user_location` was `None` by validating before using on map.

---

## [v1.2.0] – 2025-06-25

### ✨ Added
- 📍 Real-time location capture using `streamlit_geolocation`.
- 🗺️ Interactive map display with Folium markers for nearby pharmacies.
- 📄 Export buttons to download search results in PDF and CSV formats.

---

## [v1.1.0] – 2025-06-22

### ✨ Added
- 💊 Pharmacy locator feature with filtering by PIN, city, or area.
- 🌐 Base map integration using Google Tiles via Folium.
- 📋 Search radius adjustment for dynamic nearby pharmacy results.
