import streamlit as st
import pandas as pd
import re
from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes
from difflib import get_close_matches
from pathlib import Path

# ─────────────────────────────────────────────────────────────
# 1. CONSTANTS
# ─────────────────────────────────────────────────────────────
COL_NAME, COL_FORMULATION, COL_DOSAGE = "Name", "Formulation", "Dosage"
COL_TYPE, COL_PRICE_GENERIC = "Type", "Cost of generic"
COL_PRICE_BRAND, COL_SAVE_PCT = "Cost of branded", "Savings"
COL_USES, COL_SIDE_EFF = "Uses", "Side effects"

# ─────────────────────────────────────────────────────────────
# 2. SESSION DEFAULTS
# ─────────────────────────────────────────────────────────────
st.session_state.setdefault("search_mode", "Medicine name")
st.session_state.setdefault("run_search", False)
st.session_state.setdefault("detail_row", None)

# ─────────────────────────────────────────────────────────────
# 3. PAGE CONFIG & CSS
# ─────────────────────────────────────────────────────────────
st.set_page_config(page_title="GENERIC MEDICINE FINDER", layout="wide")
st.markdown("""
<style>
section.main > div > div > div > div{
  border:1px solid #ddd;
  border-radius:18px;
  padding:24px;
  background: #ffffff;
  box-shadow: 0 4px 12px rgba(2, 137, 157, 0.1);
  max-width:900px; margin-left:auto; margin-right:auto;
}
h1, h2 { text-align:center !important; }
div.stButton > button{
  white-space:nowrap;
  padding:12px 20px;
  border:2px solid #02899d;
  border-radius:12px;
  background: #ffffff;
  font-size:15px;
  font-weight: 600;
  transition:.3s;
  height:54px;
}
div.stButton > button:hover{
  background: #02899d;
  color: white;
  box-shadow: 0 0 12px #02899d;
  transform:scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────
# 4. LOAD DATA
# ─────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    BASE_DIR = Path(__file__).resolve().parent.parent
    csv_path = BASE_DIR / "Final.csv"

    if not csv_path.exists():
        st.error(f"Final.csv not found.\nExpected location:\n{csv_path}")
        st.stop()

    df = pd.read_csv(csv_path)

    df.columns = df.columns.str.strip()

    df = df[df["Name"].str.lower() != "name"]

    rename = {
        "uses": "Uses",
        "indications": "Uses",
        "side effects": "Side effects",
        "adverse effects": "Side effects"
    }

    df.rename(
        columns={c: rename[c.lower()] for c in df.columns if c.lower() in rename},
        inplace=True
    )

    df["_form_clean"] = df[COL_FORMULATION].astype(str).str.strip().str.lower()
    df["_dosage_clean"] = df[COL_DOSAGE].astype(str).str.strip().str.lower()
    df["_type_clean"] = df[COL_TYPE].astype(str).str.strip().str.lower()

    for col in (COL_PRICE_GENERIC, COL_PRICE_BRAND, COL_SAVE_PCT):
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    if (
        COL_SAVE_PCT not in df.columns
        and COL_PRICE_GENERIC in df.columns
        and COL_PRICE_BRAND in df.columns
    ):
        df[COL_SAVE_PCT] = (
            100
            * (df[COL_PRICE_BRAND] - df[COL_PRICE_GENERIC])
            / df[COL_PRICE_BRAND]
        )

    return df

df = load_data()

# ─────────────────────────────────────────────────────────────
# 5. UPLOAD PRESCRIPTION & SMART MATCHING
# ─────────────────────────────────────────────────────────────
st.markdown("### 📎 Upload Prescription (PDF or PNG)")
file = st.file_uploader("Upload a prescription file", type=["pdf", "png"])

if file is not None:
    text = ""
    try:
        if file.type == "application/pdf":
            pages = convert_from_bytes(file.read())
            text = "\n".join([pytesseract.image_to_string(page) for page in pages])
        elif file.type.startswith("image/"):
            image = Image.open(file)
            text = pytesseract.image_to_string(image)
    except Exception as e:
        st.error(f"❌ Error extracting text: {e}")

    if text:
        st.markdown("#### 📝 Extracted Text from File")
        st.text(text)

        # Clean text: remove numbers and punctuation
        cleaned_lines = []
        for line in text.splitlines():
            line = re.sub(r"[0-9]+", "", line)
            line = re.sub(r"[^\w\s]", "", line)
            line = line.strip().lower()
            if line:
                cleaned_lines.append(line)

        all_meds = df[COL_NAME].dropna().str.lower().tolist()
        matches = set()

        for line in cleaned_lines:
            for word in line.split():
                if not word.isalpha():
                    continue
                if word in all_meds:
                    matches.add(word)
                else:
                    close = get_close_matches(word, all_meds, n=1, cutoff=0.85)
                    if close:
                        matches.add(close[0])

        matched = df[df[COL_NAME].str.lower().isin(matches)]

        if not matched.empty:
            st.markdown("### ✅ Matched Generic Medicines")

            for idx, row in matched.iterrows():
                with st.expander(f"💊 {row[COL_NAME]} ({row[COL_DOSAGE]}) – {row[COL_FORMULATION]}"):
                    st.markdown(f"**Type:** {row[COL_TYPE]}")
                    if pd.notna(row.get(COL_PRICE_GENERIC)):
                        st.markdown(f"💸 **Generic Cost:** ₹{row[COL_PRICE_GENERIC]:.2f}")
                    if pd.notna(row.get(COL_PRICE_BRAND)):
                        st.markdown(f"🏷️ **Branded Cost:** ₹{row[COL_PRICE_BRAND]:.2f}")
                    if pd.notna(row.get(COL_SAVE_PCT)):
                        st.markdown(f"💰 **Savings:** {row[COL_SAVE_PCT]:.2f}%")
                    if pd.notna(row.get(COL_USES)):
                        st.markdown(f"🩺 **Uses:** {row[COL_USES]}")
                    if pd.notna(row.get(COL_SIDE_EFF)):
                        st.markdown(f"⚠️ **Side Effects:** {row[COL_SIDE_EFF]}")

                # Show alternative brands with same formulation (outside expander)
                same_form_df = df[
                    (df[COL_FORMULATION].astype(str).str.lower().str.strip() == str(row[COL_FORMULATION]).lower().strip())
                    & (df[COL_NAME] != row[COL_NAME])
                ]
                if not same_form_df.empty:
                    show_alt = st.checkbox(f"🔁 Show other medicines with same formulation for {row[COL_NAME]}", key=f"alt_{idx}")
                    if show_alt:
                        for _, alt in same_form_df.iterrows():
                            st.markdown(f"- **{alt[COL_NAME]}** ({alt[COL_DOSAGE]})")
        else:
            st.warning("No medicines matched from extracted names.")

