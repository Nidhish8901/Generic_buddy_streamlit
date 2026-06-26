import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re

# Read the theme from session
theme = st.session_state.get("theme", "Light Mode")

# Inject additional dark theme styling for widgets
if theme == "Dark Mode":
    st.markdown("""
        <style>
        /* Input boxes and text fields */
        input, textarea, .stTextInput > div > div > input {
            background-color: #1e1e1e !important;
            color: #f5f5f5 !important;
            border: 1px solid #555 !important;
        }

        /* Dropdowns */
        .stSelectbox > div > div {
            background-color: #1e1e1e !important;
            color: #f5f5f5 !important;
            border: 1px solid #555 !important;
        }

        /* Buttons */
        button[kind="secondary"], .stButton > button {
            background-color: #333333 !important;
            color: white !important;
            border: 1px solid #666666 !important;
        }

        /* Radio buttons */
        .stRadio > div {
            color: #f5f5f5 !important;
        }

        /* Labels */
        label, .css-1cpxqw2 {
            color: #ddd !important;
        }
        </style>
    """, unsafe_allow_html=True)

# ──────────── 1. CONSTANTS ────────────
COL_NAME, COL_FORMULATION, COL_DOSAGE = "Name", "Formulation", "Dosage"
COL_TYPE, COL_PRICE_GENERIC = "Type", "Cost of generic"
COL_PRICE_BRAND, COL_SAVE_PCT = "Cost of branded", "Savings"
COL_USES, COL_SIDE_EFF = "Uses", "Side effects"

st.session_state.setdefault("search_mode", "Medicine name")
st.session_state.setdefault("run_search", False)
st.session_state.setdefault("detail_row", None)
st.session_state.setdefault("show_insights", False)

# ──────────── 2. PAGE SETUP + STYLES ────────────
st.set_page_config(page_title="GENERIC MEDICINE FINDER", layout="wide")
st.markdown("""
<style>
:root {
  --primary-color: #02899d;
  --primary-dark-color: #015c68;
}
section.main > div > div > div > div{
  border:1px solid #ddd; border-radius:18px; padding:24px;
  background: white; box-shadow: 0 4px 12px rgba(2,137,157,0.1);
  max-width:900px; margin:auto;
}
h1, h2 { text-align:center; }
h1 { color: var(--primary-dark-color); }
h2 { color: var(--primary-color); }
div.stButton > button{
  padding:12px 20px; border:2px solid var(--primary-color); border-radius:12px;
  background:white; font-size:15px; font-weight:600; height:54px;
}
div.stButton > button:hover{
  background: var(--primary-color); color: white;
  box-shadow: 0 0 12px var(--primary-color); transform:scale(1.05);
}
th,td{padding:6px 4px;font-size:.9rem;}
</style>
""", unsafe_allow_html=True)

# ──────────── 3. LOAD DATA ────────────
def is_mixed(formulation):
    if pd.isna(formulation): return "Pure"
    return "Mixed" if re.search(r"\+|/|,|&", formulation) else "Pure"

@st.cache_data
def load_data(path="Final.csv"):
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()

    rename = {
        "uses": "Uses",
        "indications": "Uses",
        "side effects": "Side effects",
        "adverse effects": "Side effects"
    }
    df.rename(columns={c: rename[c.lower()] for c in df if c.lower() in rename}, inplace=True)

    df["_form_clean"] = df[COL_FORMULATION].str.strip().str.lower()
    df["Formulation Type"] = df[COL_FORMULATION].apply(is_mixed)
    df["_dosage_clean"] = df[COL_DOSAGE].astype(str).str.strip().str.lower()
    df["_type_clean"] = df[COL_TYPE].str.strip().str.lower()

    for col in (COL_PRICE_GENERIC, COL_PRICE_BRAND, COL_SAVE_PCT):
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    if COL_SAVE_PCT not in df.columns and {COL_PRICE_GENERIC, COL_PRICE_BRAND}.issubset(df.columns):
        df[COL_SAVE_PCT] = 100 * (df[COL_PRICE_BRAND] - df[COL_PRICE_GENERIC]) / df[COL_PRICE_BRAND]

    return df

# Call the function after definition
df = load_data()


# ──────────── 4. HELPERS ────────────
def bulletify(txt):
    if pd.isna(txt) or str(txt).strip() == "":
        return ""
    parts = re.split(r"[;,/\n]+", str(txt))
    return "\n".join(f"- {p.strip().capitalize()}" for p in parts if p.strip())

def tidy(d):
    d = d.drop(columns=[c for c in d.columns if c.startswith("_")], errors="ignore").copy()
    if COL_SAVE_PCT in d.columns:
        d[COL_SAVE_PCT] = d[COL_SAVE_PCT].round(1)
    return d.reset_index(drop=True)

def safe_sort(d, col, asc):
    if col not in d: return d
    return d.assign(_k=pd.to_numeric(d[col], errors="coerce")).sort_values("_k", ascending=asc).drop(columns="_k")

def show_clickable_table(df_: pd.DataFrame, header=None, key_prefix="tbl"):
    if df_.empty: return
    if header: st.subheader(header)
    page_size = 10
    total_pages = (len(df_) - 1) // page_size + 1
    current_page = st.number_input("Page", min_value=1, max_value=total_pages, value=1, step=1, key=f"{key_prefix}_page")
    start_idx = (current_page - 1) * page_size
    end_idx = start_idx + page_size
    df_page = df_.iloc[start_idx:end_idx]

    hdr = st.columns([2.5, 2, 2, 2, 2, 2])
    for col, text in zip(hdr, ["Name", "Formulation", "Dosage", "Generic ₹", "Branded ₹", "Savings %"]):
        col.markdown(f"{text}")

    for i, row in df_page.iterrows():
        c = st.columns([2.5, 2, 2, 2, 2, 2])
        if c[0].button(row[COL_NAME], key=f"{key_prefix}_{i}"):
            st.session_state.detail_row = row.to_dict()
        c[1].write(row.get(COL_FORMULATION, "—"))
        c[2].write(row.get(COL_DOSAGE, "—"))
        c[3].write(row.get(COL_PRICE_GENERIC, "—"))
        c[4].write(row.get(COL_PRICE_BRAND, "—"))
        savings = row.get(COL_SAVE_PCT, "—")
        if isinstance(savings, (int, float)) and not pd.isna(savings):
            if savings < 0:
                c[5].markdown(f"<span style='color:red;font-weight:600'>{savings:.1f}%</span>", unsafe_allow_html=True)
            else:
                c[5].write(f"{savings:.1f}%")
        else:
            c[5].write("—")

    st.caption(f"Showing {start_idx+1} – {min(end_idx, len(df_))} of {len(df_)} results")

def plot_infographics(df):
    st.markdown("## 💡 Medical Insights")
    st.markdown("Trends and savings analysis for generic medicines:")

    fig1, ax1 = plt.subplots()
    fig1.set_size_inches(1.5, 1.2)
    ax1.bar(["Branded", "Generic"], [df[COL_PRICE_BRAND].mean(), df[COL_PRICE_GENERIC].mean()],
            color=["#ff6666", "#66cc99"])
    ax1.set_title("Avg. Price", fontsize=8)
    ax1.set_ylabel("₹", fontsize=7)
    ax1.tick_params(labelsize=6)
    st.pyplot(fig1)

    fig2, ax2 = plt.subplots()
    fig2.set_size_inches(1.5, 1.2)
    df[COL_SAVE_PCT].dropna().clip(0, 100).hist(bins=20, ax=ax2, color="#4db6ac")
    ax2.set_title("Savings Distribution", fontsize=8)
    ax2.set_xlabel("Savings (%)", fontsize=7)
    ax2.set_ylabel("Count", fontsize=7)
    ax2.tick_params(labelsize=6)
    st.pyplot(fig2)

    fig3, ax3 = plt.subplots()
    fig3.set_size_inches(1.5, 1.2)
    top_forms = df[COL_FORMULATION].value_counts().nlargest(5)
    top_forms.plot(kind="bar", ax=ax3, color="#02899d")
    ax3.set_title("Top 5 Formulations", fontsize=8)
    ax3.set_ylabel("No. of Medicines", fontsize=7)
    ax3.tick_params(labelsize=6)
    st.pyplot(fig3)

# ──────────── 5. UI + FILTERS ────────────
st.markdown("# GENERIC MEDICINE FINDER")
st.markdown("## Search & Filters")

b1, b2 = st.columns([0.4, 0.6])
with b1:
    if st.button("📊 Show Medical Insights"):
        st.session_state.show_insights = True
with b2:
    if st.session_state.show_insights and st.button("🔙 Back to Results"):
        st.session_state.show_insights = False

st.markdown("---")

if st.session_state.show_insights:
    plot_infographics(df)
    st.stop()

mode_cols = st.columns([0.3, 0.3, 0.4])
with mode_cols[0]:
    if st.button("Name", key="mode_name"):
        st.session_state.search_mode = "Medicine name"
with mode_cols[1]:
    if st.button("Formulation", key="mode_form"):
        st.session_state.search_mode = "Formulation"
with mode_cols[2]:
    if st.button("Ailment", key="mode_ailment"):
        st.session_state.search_mode = "Ailment"

mode = st.session_state.search_mode
if mode == "Ailment":
    ailment_input = st.text_input("Enter ailment name (e.g., pain, fever, diabetes)")


r1 = st.columns([1.2, 1, 1])
types = sorted(df[COL_TYPE].dropna().unique())
typ = r1[0].selectbox("Therapeutic Type", ["All"] + types)
base_df = df if typ == "All" else df[df["_type_clean"] == typ.lower()]
dosages = sorted(base_df["_dosage_clean"].dropna().unique())
dose = r1[1].selectbox("Dosage Filter", ["All"] + dosages)
sort_map = {"Generic price": COL_PRICE_GENERIC, "Branded price": COL_PRICE_BRAND, "Savings %": COL_SAVE_PCT}
sort_by = r1[2].selectbox("Sort by", list(sort_map))
# Add Formulation Type Filter
form_type = st.selectbox("Formulation Type", ["All", "Pure Formulation", "Mixed Formulation"])


r2 = st.columns([1.2, 1, 1])
mode = st.session_state.search_mode
if mode == "Medicine name":
    names = sorted(base_df[COL_NAME].dropna().unique())
    picked = r2[0].selectbox("Branded Medicine", ["— All in Type —"] + names)
    name_sel = picked != "— All in Type —"
else:
    forms_base = base_df if typ == "All" else base_df[base_df["_type_clean"] == typ.lower()]
    forms = sorted(forms_base[COL_FORMULATION].dropna().unique())
    picked = r2[0].selectbox("Choose Formulation", ["— select —"] + forms)

ascending = r2[1].radio("Order", ["Low → High", "High → Low"], horizontal=True) == "Low → High"
if r2[2].button("Search", key="search_btn"):
    st.session_state.run_search = True
    st.session_state.detail_row = None

# ──────────── 6. FILTER + DISPLAY ────────────
if not st.session_state.run_search:
    st.info("Adjust filters, then click Search to view results.")
    st.stop()

if mode == "Medicine name":
    hits = base_df if not name_sel else base_df[base_df[COL_NAME] == picked]
elif mode == "Formulation":
    if picked == "— select —":
        st.warning("Please select a formulation.")
        st.stop()
    hits = base_df[base_df[COL_FORMULATION].str.lower().str.strip() == picked.strip().lower()]
elif mode == "Ailment":
    if not ailment_input.strip():
        st.warning("Please enter an ailment name.")
        st.stop()
    hits = base_df[base_df[COL_USES].str.contains(ailment_input.strip(), case=False, na=False)]
else:
    st.warning("Invalid mode.")
    st.stop()


if dose != "All":
    hits = hits[hits["_dosage_clean"] == dose]
# Apply Formulation Type Filter
if form_type == "Pure Formulation":
    hits = hits[hits["Formulation Type"] == "Pure"]
elif form_type == "Mixed Formulation":
    hits = hits[hits["Formulation Type"] == "Mixed"]


if hits.empty:
    st.warning("No entries match your filters.")
    st.stop()

same = pd.DataFrame()
if mode == "Medicine name" and "name_sel" in locals() and name_sel:
    same = base_df[base_df["_form_clean"].isin(hits["_form_clean"].unique())]
    if dose != "All":
        same = same[same["_dosage_clean"] == dose]
    if form_type == "Pure Formulation":
       same = same[same["Formulation Type"] == "Pure"]
    elif form_type == "Mixed Formulation":
       same = same[same["Formulation Type"] == "Mixed"]


hits_sorted = tidy(safe_sort(hits, sort_map[sort_by], ascending))
same_sorted = tidy(safe_sort(same, sort_map[sort_by], ascending))

if mode == "Medicine name":
    if not name_sel:
        show_clickable_table(hits_sorted, "Medicines", "generic")
    else:
        st.subheader("Exact Match")
        st.markdown(f"Formulation – {hits_sorted.at[0, COL_FORMULATION]}")
        show_clickable_table(hits_sorted, key_prefix="exact")
        st.subheader("All Medicines with the Same Formulation")
        show_clickable_table(same_sorted, key_prefix="same")
else:
    show_clickable_table(hits_sorted, f"Medicines with Formulation: {picked}", key_prefix="form")

det = st.session_state.detail_row
if det:
    uses = bulletify(det.get(COL_USES, ""))
    side = bulletify(det.get(COL_SIDE_EFF, ""))
    if uses or side:
        st.markdown("---")
    if uses:
        st.markdown(f"#### Uses of {det[COL_NAME]}")
        st.markdown(uses)
    
    if side:
        st.markdown("<div style='font-size:15px; font-weight:600; color:#444;'>Possible Side Effects</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='font-size:13px; line-height:1.6'>{side}</div>", unsafe_allow_html=True)



    # ────── NEW: MEDICINE-SPECIFIC INFOGRAPHIC ──────
    st.markdown("#### 📈 Medicine Infographic")

    # Bar chart – Branded vs Generic (smaller)
    fig1, ax1 = plt.subplots(figsize=(2.5, 2))  # smaller figure
    ax1.bar(["Branded", "Generic"],
            [det.get(COL_PRICE_BRAND, 0), det.get(COL_PRICE_GENERIC, 0)],
            color=["#ff6f61", "#66bb6a"])
    ax1.set_title("Price Comparison", fontsize=10)
    ax1.set_ylabel("₹", fontsize=9)
    ax1.tick_params(labelsize=8)
    fig1.tight_layout()
    st.pyplot(fig1, use_container_width=False)

    # Pie chart – Savings %
    if pd.notna(det.get(COL_SAVE_PCT)):
        savings = det[COL_SAVE_PCT]
        fig2, ax2 = plt.subplots(figsize=(2.3, 2.3))  # smaller figure
        ax2.pie([savings, 100 - savings],
                labels=["Saved", "Paid"],
                colors=["#4db6ac", "#ddd"],
                autopct="%.1f%%",
                startangle=90)
        ax2.set_title("Savings Share", fontsize=10)
        fig2.tight_layout()
        st.pyplot(fig2, use_container_width=False)

    # Top formulations bar – Same therapeutic type
    if COL_FORMULATION in det and COL_TYPE in det:
        form_name = det[COL_FORMULATION]
        type_clean = det[COL_TYPE].strip().lower()
        form_count_df = df[df[COL_TYPE].str.strip().str.lower() == type_clean]
        top_forms = form_count_df[COL_FORMULATION].value_counts().nlargest(5)

        fig3, ax3 = plt.subplots(figsize=(2.5, 2))  # smaller figure
        top_forms.plot(kind="bar", ax=ax3, color="#02899d")
        ax3.set_title("Top Formulations in Category", fontsize=10)
        ax3.set_ylabel("No. of Medicines", fontsize=9)
        ax3.tick_params(labelsize=8)
        fig3.tight_layout()
        st.pyplot(fig3, use_container_width=False)
