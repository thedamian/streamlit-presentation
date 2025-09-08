import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Tech Stack Explorer", layout="wide")

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv("survey_results_public.csv", low_memory=False)
    df["WorkExp"] = pd.to_numeric(df["WorkExp"], errors="coerce")
    df["YearsCode"] = pd.to_numeric(df["YearsCode"], errors="coerce")
    return df.dropna(subset=["Country", "WorkExp", "Employment"])

df = load_data()

st.title("🧠 Stack Overflow Tech Stack Explorer")

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filter Responses")
countries = st.sidebar.multiselect("Country", sorted(df["Country"].unique()))
employment_types = st.sidebar.multiselect("Employment Type", sorted(df["Employment"].unique()))
exp_range = st.sidebar.slider("Years of Experience", 0, 50, (0, 50))

# --- Apply Filters ---
filtered_df = df.copy()
if countries:
    filtered_df = filtered_df[filtered_df["Country"].isin(countries)]
if employment_types:
    filtered_df = filtered_df[filtered_df["Employment"].isin(employment_types)]
filtered_df = filtered_df[
    (filtered_df["WorkExp"] >= exp_range[0]) & (filtered_df["WorkExp"] <= exp_range[1])
]

st.markdown(f"### Showing {len(filtered_df)} responses")

# --- Helper: Extract Top Keywords ---
def extract_top(series, top_n=10):
    return (
        series.dropna()
        .str.split(";")
        .explode()
        .str.strip()
        .value_counts()
        .head(top_n)
    )

# --- Top Technologies ---
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("💻 Top Languages")
    lang_counts = extract_top(filtered_df["LanguageHaveWorkedWith"])
    st.bar_chart(lang_counts)

with col2:
    st.subheader("🧱 Top Frameworks")
    fw_counts = extract_top(filtered_df["WebframeHaveWorkedWith"])
    st.bar_chart(fw_counts)

with col3:
    st.subheader("🗄️ Top Databases")
    db_counts = extract_top(filtered_df["DatabaseHaveWorkedWith"])
    st.bar_chart(db_counts)

# --- Trends Over Time ---# --- Trends Over Time ---
# st.subheader("📈 Language Trends Over Time")

# trend_df = df.dropna(subset=["YearsCode", "LanguageHaveWorkedWith"]).copy()
# trend_df["YearsCode"] = pd.to_numeric(trend_df["YearsCode"], errors="coerce")
# trend_df = trend_df.dropna(subset=["YearsCode"])
# trend_df["YearsCode"] = trend_df["YearsCode"].astype(int)

# # Explode languages
# trend_df["Language"] = trend_df["LanguageHaveWorkedWith"].str.split(";")
# trend_df = trend_df.explode("Language")
# trend_df["Language"] = trend_df["Language"].str.strip()

# # Reset index to avoid duplicate axis errors
# trend_df = trend_df.reset_index(drop=True)

# # Optional: Drop duplicate rows if needed
# trend_df = trend_df.drop_duplicates(subset=["YearsCode", "Language"])

# # Filter selected languages
# trend_langs = st.multiselect(
#     "Select Languages to Compare",
#     options=trend_df["Language"].value_counts().index.tolist(),
#     default=["TypeScript", "PHP"]
# )

# trend_filtered = trend_df[trend_df["Language"].isin(trend_langs)]
# lang_trend = trend_filtered.groupby(["YearsCode", "Language"]).size().reset_index(name="Count")

# fig = px.line(lang_trend, x="YearsCode", y="Count", color="Language", markers=True)
# st.plotly_chart(fig, use_container_width=True)

# --- Footer ---
st.markdown("---")