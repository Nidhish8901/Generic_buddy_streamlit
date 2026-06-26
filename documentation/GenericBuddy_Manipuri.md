# 📘 প্ৰ’জেক্ট নাম: GenericBuddy – ওষুধ খুঁজিব ও ফার্মাচি খুঁজিব

## 📌 প্ৰজেক্ট টাইটেল
**GenericBuddy – ওষুধ খুঁজিব ও ফার্মাচি খুঁজিব**

## 🧠 লক্ষ্য
সুবিধাজনক আৰু খৰচ-কটকটি ডিজিটাল প্লাটফর্ম বানাবা যি–
- বিপণিত ওষুধৰ সস্তা জেনেরিক বিকল্প দেখুৱায়।
- ফর্মুলেশন, ডোজ আৰু সঞ্চয় তুলনা কৰিব পাৰে।
- লোকেশন-ভিত্তিক ফার্মাচি খুঁজিবলৈ সহায় কৰে।

---

## 🔍 সমস্যাৰ বৰ্ণনা

ভাৰতত বিপণিত ওষুধ বহু সময়ত বহুত দামী হয়, যাৰ ফলে স্বাস্থ্যসেবা সকলোৰে বাবে সহজ নহয়। অধিকাংশ মানুহে সস্তা জেনেরিক বিকল্প বিষয়ে জানি নথাকিব। এই প্লাটফর্মে এই সমস্যা সমাধান কৰে:
- দামি ব্র্যান্ডেড ওষুধৰ বিকল্প চিনাক্ত কৰি।
- সহজ, স্মার্ট খুঁজিব ইন্টারফেস দিয়া।
- জিপিএস-ভিত্তিক টুলে নিকটতম ফার্মাচি চিনাক্ত কৰা।

---

## 🧩 মূল উপাদান আৰু প্ৰয়োগ ধাপসমূহ

### 1️⃣ **ডাটা সংগ্রহ**
- Excel-based ডাটাবেস তৈয়ার কৰা:
  - ব্র্যান্ড নাম, জেনেরিক নাম, ফর্মুলেশন
  - বিপণিত ও জেনেরিক দাম
  - সঞ্চয়ের শতাংশ
- Tata 1mg, PharmEasy, NetMeds পৰিসৰৰ পৰা ম্যানুৱেল তথ্য সংগ্ৰহ কৰা।

### 2️⃣ **ঔষধ বিকল্প মিলানো**
- AI সহায় আৰু ফার্মাচি টুল ব্যৱহাৰ কৰা:
  - একে জেনেরিক নাম আৰু ফর্মুলেশন
  - স্ক্ৰ্যাপিং, ম্যাপিং, ভেৰিফিকেশ্যন

### 3️⃣ **Web App Development (MVP)**
- Streamlit দিয়ে Web UI ডেভেলপ কৰা:
  - Medicine খুঁজিব অপশন
  - ফিল্টার আৰু তুলনামূলক ফলাফল
  - Faculty ৰ বাবে raw প্ৰটোটাইপ পেশ কৰা

### 4️⃣ **Feature Set**

#### 💊 Generic Medicine Finder
- স্মার্ট খুঁজিব (Brand নাম বা Formulation)
- Exact + Similar match দেখুৱায়
- দাম অনুসৰি Filter (High→Low, Low→High)
- Dosage আৰু থেৰাপিউটিক ফিল্টার
- তুলনামূলক টেবুল: Brand price, Generic price, % saving
- Medicine Info Card: Use cases, side effects

#### 🗺️ Pharmacy Locator
- PIN, শহর, এলাকা বা লাইভ GPS অনুসন্ধান
- Jan Aushadhi বা chain store অনুসৰি Filter
- Distance slider
- CSV/PDF ৰিপোর্ট এক্সপোর্ট
- Map view: Satellite বা Street toggle

---

## 🧪 Tech Stack

| কম্পোনেন্ট             | উদ্দেশ্য                             |
|------------------------|--------------------------------------|
| **Streamlit**          | Front-end web framework              |
| **Pandas**             | Data cleaning & manipulation         |
| **streamlit-geolocation** | Real-time location integration   |
| **ReportLab**          | PDF রিপোর্ট এক্সপোর্ট                |
| **HTML/CSS**           | Styling এবং layout customization     |

---

## 📁 Data Insights

- Medicine dataset অন্তর্ভুক্ত:
  - Dosage strength, Cost per unit
  - Savings calculation
  - Alternate branded options
- স্বাস্থ্যসচেতন সিদ্ধান্ত ল’বলৈ সহায় কৰে

---

## 🧠 শিকনি আৰু উন্নয়ন

### 🧪 চ্যালেঞ্জ:
- অনলাইন medicine দামৰ variability
- Formulation format ৰ অমিল
- Generic-brand pair মিলাবলৈ ম্যানুয়েল কাম
- বড় dataset ৰ UI performance

### 🚀 Future Plans:
- 1mg বা PharmEasy ৰ live API ইন্টিগ্ৰেট কৰা
- Multi-language support rural ইউজাৰ ৰ বাবে
- Jan Aushadhi, PHC, NGO Clinic locator ৰ অন্তর্ভুক্তি
- AI-based recommendation system

---

## 🧾 Team Contribution Summary

- ডাটা Research, Entry, Formulation Matching
- UI/UX ডিজাইন
- Feature Integration: search, maps, AI
- Documentation আৰু ইউজাৰ Feedback

---

## 🔗 লাইভ ডেমো

- 🌐 [Generic Medicine Finder](https://generic-bro-b9bjg6yserxjjpczyaegab.streamlit.app)  
- 📍 [Pharmacy Locator](https://generic-bro-f4rmkft8huxzzuj52cnfyy.streamlit.app)

---

## 📸 Screenshots

> *Interface, Results, Map view screenshots insert কৰক*

---

## 📚 References

- Tata 1mg
- PharmEasy Data
- Jan Aushadhi Resources
- WHO Guidelines on Generics

---

## ✅ উপসংহার

**GenericBro** হৈছে এক বুদ্ধিমান পদক্ষেপ সাশ্রয়ী আৰু সুবিদামূলক স্বাস্থ্যসেবাৰ বাবে। AI সংহতিৰে এইটো এক digital সহচৰ হ’ব।

