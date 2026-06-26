<!-- Project Logo -->
<p align="center">
  <img src="logo.png" width="180" alt="GenericBuddy Logo"/>
</p>

<h1 align="center">💊 GenericBuddy – Medicine Finder & Pharmacy Locator</h1>

<p align="center"><b>A Streamlit-powered platform to find affordable generic alternatives to branded medicines and locate nearby pharmacies.</b></p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Streamlit-ff4b4b?style=for-the-badge&logo=streamlit" />
  <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/UI-Mobile%20Friendly-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=1000&center=true&vCenter=true&width=850&lines=Discover+affordable+alternatives+to+branded+medicines...;Compare+prices%2C+dosage%2C+and+formulation+in+seconds.;Find+pharmacies+around+you+using+geolocation!+📍" />
</p>

---

## 🚀 Live Preview

- [GenericBuddy](https://genericbuddy.streamlit.app)  

---

## 💡 Overview

GenericBuddy helps users:  
- 🔍 Search branded medicines and discover *generic substitutes*  
- 📊 Compare formulation, cost, dosage, and savings  
- 📍 Locate pharmacies via *PIN, city, area, or GPS*  
- 🧭 Get *directions* to pharmacies from your location  
- 🧾 Detect medicines from a *full prescription* text  
- 📈 View *price comparisons as bar graphs* and *savings shares as pie charts*  
- 🖼 Explore *top formulations* and *medical insights* through interactive infographics  
- 🏠 Enjoy a *new home page* with a clean, modern interface and quick links to key features  
- 🎚 Toggle between *Dark Mode* and *Light Mode*  
- 🧪 Filter medicines by *formulation type*: Pure, Mixed, or All  
- 🩺 Search by *ailment name* (e.g., "fever", "diabetes")  
- 🔡 Improved visual layout with *smaller font for side effects*  

---

## 🎯 Who’s It For?

| Target            | Benefit                                   |
|-------------------|-------------------------------------------|
| 🧑‍⚕ Patients     | Lower medication costs & better access    |
| 💊 Pharmacists    | Recommend effective generic substitutions |
| 🏥 NGOs           | Budget-friendly public-health outreach    |
| 📚 Students       | Study drug equivalence & pharmacology     |

---

## ✨ Feature Highlights

### 💊 Generic Medicine Finder

| Feature                                  | Description                                                                 |
|------------------------------------------|-----------------------------------------------------------------------------|
| 🔍 Smart Search                          | Search by *brand name* or *formulation name*                                |
| 🧬 Exact + Formulation Matches           | Lists both *exact brand matches* and *same formulation* alternatives        |
| 💸 Price-Based Filtering                 | Filter by *branded price, generic price, or % savings*                      |
| 🧪 Therapeutic & Dosage Filters          | Narrow results by *therapeutic type* or *dosage strength*                   |
| 📊 Rich Comparison Data                  | View *brand price, generic price, and savings %* for each entry             |
| 📉 Bar Graph Price Comparison            | Compare prices visually as a *bar graph*                                    |
| 🥧 Savings Pie Chart                     | Visualize savings share as a *pie chart*                                    |
| 🔝 Top Formulations Insights             | View *top formulations* in the same category                                |
| 🧠 Deep Medicine Details                 | Get *uses, side effects, and medical insights*                              |
| 🎚 Theme Toggle                         | Switch between *light* and *dark* mode                                      |
| 🧪 Formulation Filter                    | Filter results by *Pure, Mixed, or All* formulations                        |
| 🩺 Ailment-Based Search                  | Search by *condition or disease name*                                       |
| 🔡 Visual Layout Improvements            | *Side effects* now displayed in smaller font for better readability         |

---

### 🏠 New Home Page

- ✨ Modern, intuitive layout  
- 🚀 Quick links to popular features  
- 🖼 Featured medical infographics for instant health insights  

---

### 📊 Medical Insights (Infographics)

- 🖼 Interactive visuals showing health trends, drug usage statistics, and cost comparisons  
- 📌 Integrated within the app for quick exploration  

---

### 🗺 Pharmacy Locator

| Feature                                  | Description                                                                 |
|------------------------------------------|-----------------------------------------------------------------------------|
| 📍 Multi-mode Search                     | Search by *pincode, area, city, or live GPS*                                |
| 🧭 Google Maps Directions                | Click a pharmacy name to get directions                                     |
| 📏 Distance Slider                       | Adjust search radius with an interactive slider                             |
| 📤 Export Results                        | Download results as *CSV* or *PDF*                                          |
| 🗺 Map View Options                      | Switch between *satellite* and *street* map views                           |

---

### 📄 Prescription Reader

| Feature                                | Description                                                                 |
|----------------------------------------|-----------------------------------------------------------------------------|
| 🧾 Prescription Input                  | Paste a prescription or drug list directly                                  |
| 🧠 Intelligent Matching                | Detects and matches *branded & generic medicines*                           |
| 📊 Multi-drug Results                  | Compares each medicine with available alternatives and pricing              |

---

## 🧪 Tech Stack

| Technology                  | Purpose                          |
|-----------------------------|------------------------------------|
| *Streamlit*               | UI rendering and dashboard logic |
| *Pandas*                  | Data handling and processing     |
| *Plotly / Matplotlib*     | Interactive bar & pie charts     |
| *ReportLab*               | PDF generation for exports       |
| *streamlit-geolocation*   | GPS-based location features      |
| *HTML / CSS*              | Custom styling and layout        |

---

## ⚙️ How to Use GenericBuddy on Your System

✅ **1. Install Python & Streamlit**  
Ensure **Python 3.9+** is installed. Then run:

```bash
pip install streamlit pandas plotly matplotlib reportlab streamlit-geolocation

git clone https://github.com/your-username/GenericBuddy.git
cd GenericBuddy

streamlit run <filename>.py

