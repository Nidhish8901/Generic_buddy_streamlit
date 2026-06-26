# 📘 Project Documentation: GenericBuddy – Medicine Finder & Pharmacy Locator

## 📌 Project Title
**GenericBuddy – Medicine Finder & Pharmacy Locator**

## 🧠 Objective
To create a user-friendly and cost-efficient digital platform that helps patients, pharmacists, and healthcare stakeholders to:
- Compare branded medicines with affordable generic alternatives.
- Explore formulation, dosage, and savings.
- Discover pharmacy stores using location-based tools.

---

## 🔍 Problem Statement

In India, branded medicines are often sold at significantly higher prices than their generic counterparts, creating a barrier to affordable healthcare. Lack of awareness and accessibility to generic substitutes hinders cost-effective treatment. Our platform addresses this issue by:
- Identifying equivalent generics for expensive branded medicines.
- Providing a smart, searchable interface.
- Including geolocation tools to guide users to nearby generic medicine stores.

---

## 🧩 Key Components and Implementation Stages

### 1️⃣ **Data Collection**
- We created an Excel-based **medicine database** containing:
  - **Branded name**
  - **Generic name**
  - **Formulation**
  - **Price of branded & generic medicine**
  - **Saving percentage**
- Prices were manually fetched from trusted online sources like **Tata 1mg**, **PharmEasy**, and **NetMeds**.

### 2️⃣ **Medicine Alternatives Matching**
- We used an **AI assistant and pharmacy tools** to find alternative medicines based on:
  - **Exact generic name matches**
  - **Same formulation but different brands**
- This involved scraping, mapping, and validating each alternative for accuracy and relevance.

### 3️⃣ **Development of Web App (MVP Stage)**
- Built a **Streamlit** web application with:
  - User interface for medicine search
  - Smart filters for comparison
  - Tabulated and visually enriched results
- A **raw prototype** was created to present to faculty for early feedback and improvement.

### 4️⃣ **Feature Set and Functionality**

#### 💊 Generic Medicine Finder
- **Smart Search:** By brand name or formulation.
- **Exact + Formulation Matches:** Display both exact and partial matches.
- **Price-Based Filters:** Sort by price (High → Low, Low → High), or percentage savings.
- **Dosage and Therapeutic Filters:** Narrow down options for better match.
- **Comparison Table:** Side-by-side data showing:
  - Brand price
  - Generic price
  - % savings
- **Medicine Info Card:** Includes basic use cases and potential side effects.

#### 🗺️ Pharmacy Locator
- Search by:
  - **PIN code**
  - **City / Area**
  - **Live GPS**
- Filter by pharmacy type (e.g., Jan Aushadhi, chain stores).
- Adjustable **distance slider** to control radius.
- Results exportable as **CSV or PDF**.
- **Map view:** Satellite or street mode toggle.

---

## 🧪 Tech Stack

| Component               | Purpose                              |
|------------------------|--------------------------------------|
| **Streamlit**          | Front-end web framework              |
| **Pandas**             | Data cleaning and manipulation       |
| **streamlit-geolocation** | Integrate real-time location      |
| **ReportLab**          | Exporting reports in PDF format      |
| **HTML/CSS**           | Styling and custom layout design     |

---

## 📁 Data Insights and Usage

- Each medicine entry in our dataset includes:
  - Dosage strength
  - Cost per unit
  - Saving calculations (Brand – Generic)
  - Alternate branded options
- The data helps users identify more **affordable treatment options** and empowers pharmacists to guide patients better.

---

## 🧠 Learnings & Future Improvements

### 🧪 Challenges Faced:
- Variability in online medicine prices across platforms.
- Lack of uniformity in medicine naming and formulation formats.
- Manual effort in matching generic-branded pairs.
- UI performance with large datasets.

### 🚀 Future Plans:
- Connect with live APIs from pharmacy chains (e.g., 1mg, PharmEasy).
- Add multi-language support to reach rural users.
- Expand locator to include **Jan Aushadhi**, **PHC**, and **NGO clinics**.
- Build AI-powered **recommendation system** for users based on common symptoms or prescriptions.

---

## 🧾 Team Contribution Summary

- **Data Research & Entry:** Price scraping, formulation comparison, dataset cleanup.
- **UI/UX Design:** Streamlit web interface and responsive layout.
- **Feature Integration:** Search filters, map integration, AI-based suggestions.
- **Documentation & Testing:** User feedback collection and documentation creation.

---

## 🔗 Live Demos

- 🌐 [GenericBro](https://genericmedicinefinder143.streamlit.app)

---

## 📸 Screenshots

> *Screenshots of the prototype interface, search results page, and pharmacy map view can be inserted here.*

---

## 📚 References

- Tata 1mg Medicine Pricing
- PharmEasy Pricing and Data Sheets
- Government Generic Medicines List
- Jan Aushadhi Scheme Resources
- WHO Guidelines on Generic Drugs

---

## ✅ Conclusion

**GenericBro** is a smart step toward **accessible, affordable, and informed medication choices** for the Indian public. With continuous iterations and AI enhancements, it can serve as a reliable digital companion for everyday medicine comparison and discovery.