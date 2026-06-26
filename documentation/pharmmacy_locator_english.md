# 💊 GenericBuddy – Medicine Finder & Pharmacy Locator

## 📘 Project Documentation

---

## 🧠 Objective

**GenericBro** is a user-focused web platform developed to:
- Provide affordable alternatives to costly branded medicines.
- Help users locate nearby **generic medicine stores** such as **Jan Aushadhi Kendras**.
- Enable cost-saving comparisons based on medicine formulations, pricing, and dosage.
- Promote awareness of generic drug use in India, improving access to healthcare.

---

## 🧩 Project Modules

### 1️⃣ Generic Medicine Finder

#### 🔍 Overview

The **Generic Medicine Finder** helps users search for branded medicines and find their cost-effective **generic equivalents**. Users can compare medicine formulation, strength, cost, and savings percentage in an intuitive interface.

#### 🧪 Development Process

**Step 1: Data Collection**
- We built a **medicine dataset** from various pharmacy websites like **Tata 1mg**, **PharmEasy**, and **NetMeds**.
- Each entry contains:
  - Branded name
  - Generic name
  - Dosage strength
  - Formulation (tablet, syrup, etc.)
  - Price of both branded and generic versions
  - Calculated savings in rupees and percentage

**Step 2: Alternative Matching**
- Using **AI assistants** and pharmacy databases, we matched branded medicines with:
  - Exact generic counterparts
  - Other brands with the same formulation
- This involved text standardization and data cleaning (e.g., formulation type unification).

**Step 3: Front-End Design**
- The UI was built using **Streamlit** for rapid prototyping.
- Users can:
  - Search medicines by brand or formulation
  - Sort by price (High to Low, Low to High)
  - View savings per medicine
  - Filter by therapeutic class or dosage
- The interface also shows:
  - Use cases
  - Side effects
  - Strength and formulation details

#### ⚙️ Tools Used

| Tool         | Use Case                               |
|--------------|-----------------------------------------|
| Streamlit    | UI/UX and dashboard rendering           |
| Pandas       | Data handling and filtering             |
| Excel/CSV    | Raw dataset compilation and editing     |
| Python       | Backend scripting and logic             |

---

### 2️⃣ Pharmacy Locator

#### 📍 Overview

The **Pharmacy Locator** lets users search for **nearby generic medicine stores**, especially **Jan Aushadhi Kendras**. It includes filtering, map view, and export functionality.

#### 🧪 Development Process

**Step 1: Sourcing Pharmacy Store Data**
- We collected Jan Aushadhi Kendra (JAK) information from government sources and public listings.
- Data included store name, city, address, and pincode.
- However, most entries lacked **latitude and longitude**.

**Step 2: Geo-Coding Process**
- To convert addresses to GPS coordinates:
  - We manually verified store locations using **Google Maps**.
  - Used a custom **Streamlit-based Geolocation App**:
    👉 [https://geolocator-564564.streamlit.app/](https://geolocator-564564.streamlit.app/)
  - The app takes in an address and outputs:
    - Latitude
    - Longitude
    - Full resolved address
- We cleaned and validated geolocation data to remove duplicates and inaccurate mappings.

**Step 3: Integration into App**
- A map-based pharmacy locator was built in Streamlit.
- Users can:
  - Search by pincode, city, area
  - Use **live GPS** (via `streamlit-geolocation`) to find nearest stores
  - Adjust **radius** using a slider
  - View results in **table** or **interactive map** format
  - Export store list as **PDF** or **CSV**
- Each map marker shows:
  - Store name
  - Address
  - Contact details (if available)

#### ⚙️ Tools & APIs Used

| Tool/Library           | Purpose                                        |
|------------------------|------------------------------------------------|
| Google Maps            | Manual geolocation validation                  |
| Streamlit              | Front-end UI and geolocation module            |
| streamlit-geolocation  | User GPS location capture                      |
| Custom Streamlit Geolocator App | Batch geocoding for JAK addresses     |
| Pandas                 | Address data cleaning and structuring          |
| Leaflet / Folium       | Interactive map rendering and marker display   |

---

## ✨ Features Summary

### 💊 Generic Medicine Finder
| Feature                     | Description                                        |
|-----------------------------|----------------------------------------------------|
| Search                      | By brand name or formulation                       |
| Comparison Table            | Brand vs. Generic pricing and % savings            |
| Filters                     | By price, dosage, and formulation type             |
| Detailed View               | Uses, side effects, strength, and alternatives     |
| AI-Powered Suggestions      | Matched based on formulation and ingredients       |

### 🗺️ Pharmacy Locator
| Feature                     | Description                                        |
|-----------------------------|----------------------------------------------------|
| Search Options              | Pincode, area, city, GPS-based                     |
| Distance Filter             | Adjustable radius for store discovery              |
| Store Type Filter           | Filter Jan Aushadhi or other types                 |
| Export Options              | Download pharmacy list as PDF or CSV               |
| Map View                    | Satellite/Street toggle, marker popups             |

---

## 📊 Dataset Fields

### Medicines Dataset
- Medicine Name (Brand)
- Generic Name
- Formulation
- Strength
- Branded Price
- Generic Price
- Savings ₹
- Savings %

### Pharmacy Store Dataset
- Store Name
- Address
- City
- State
- Pincode
- Latitude
- Longitude

---

## 💡 Learnings & Improvements

### 🧪 Challenges
- Inconsistent medicine naming across platforms.
- Manual entry of GPS coordinates was time-consuming.
- Streamlit limitations with large datasets and dynamic map performance.

### 🚀 Future Scope
- Add **multi-language support** for rural users.
- Automate medicine matching with **NLP models**.
- Integrate **live APIs** from Tata 1mg and PharmEasy.
- Build an **AI symptom checker** that suggests generic medicines.
- Include **PHC and NGO clinics** in pharmacy locator module.

---

## 📁 Project Structure

```bash
📦genericbro
 ┣ 📂data
 ┃ ┣ medicines.csv
 ┃ ┗ pharmacy_stores_with_coords.csv
 ┣ 📂pages
 ┃ ┣ home.py
 ┃ ┣ medicine_finder.py
 ┃ ┗ pharmacy_locator.py
 ┣ app.py
 ┣ README.md
 ┗ requirements.txt