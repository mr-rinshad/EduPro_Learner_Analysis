import base64
import os
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="EduPro | Learner Analytics Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- ASSET HELPERS ----------------
@st.cache_data
def get_image_base64(path):
    """Load image from disk and return as base64 data string."""
    if os.path.exists(path):
        with open(path, "rb") as f:
            encoded = base64.b64encode(f.read()).decode()
            ext = os.path.splitext(path)[1].lower().replace(".", "")
            if ext == "jpg":
                ext = "jpeg"
            return f"data:image/{ext};base64,{encoded}"
    return None

banner_b64 = get_image_base64("assets/header_banner.jpg")
icon_learners_b64 = get_image_base64("assets/icon_learners.jpg")
icon_courses_b64 = get_image_base64("assets/icon_courses.jpg")
icon_enrollments_b64 = get_image_base64("assets/icon_enrollments.jpg")
icon_revenue_b64 = get_image_base64("assets/icon_revenue.jpg")

# ---------------- CUSTOM CSS: EMERALD & OFF-WHITE LUXURY THEME ----------------
st.markdown("""
<style>
/* Import High-End Google Typography */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

:root {
    --emerald-primary: #059669;
    --emerald-deep: #064E3B;
    --emerald-dark: #022C22;
    --emerald-light: #10B981;
    --emerald-soft: #34D399;
    --emerald-subtle: #ECFDF5;
    --emerald-border: #D1FAE5;
    --offwhite-bg: #F7FAF8;
    --offwhite-surface: #FFFFFF;
    --offwhite-card: #FAFDFB;
    --text-primary: #0F2E23;
    --text-secondary: #3D5A4F;
    --text-muted: #6B877B;
}

/* Base App Styling */
.stApp {
    background-color: var(--offwhite-bg);
    color: var(--text-primary);
    font-family: 'Plus Jakarta Sans', sans-serif;
}

/* Typography Overrides */
html, body, p, span, div, label {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
}

h1, h2, h3, h4, h5, h6 {
    font-family: 'Outfit', sans-serif !important;
    font-weight: 700 !important;
    color: var(--emerald-deep) !important;
    letter-spacing: -0.02em;
}

/* Sidebar Customization */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #F1F7F4 0%, #EBF4F0 100%) !important;
    border-right: 1px solid #D6E8DE !important;
}

[data-testid="stSidebar"] .block-container {
    padding-top: 2rem;
}

/* Multiselect Tags in Emerald Green */
span[data-baseweb="tag"] {
    background-color: var(--emerald-primary) !important;
    color: #FFFFFF !important;
    border-radius: 6px !important;
    font-weight: 600 !important;
    font-size: 0.8rem !important;
    padding: 2px 6px !important;
}
span[data-baseweb="tag"] span {
    color: #FFFFFF !important;
}

/* Hero Banner Card */
.hero-card {
    background: linear-gradient(135deg, #FFFFFF 0%, #F5FAF7 60%, #EBF6F0 100%);
    border: 1px solid #D7EADF;
    border-radius: 20px;
    padding: 1.75rem 2.25rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 20px -2px rgba(6, 78, 59, 0.05), 0 1px 3px rgba(6, 78, 59, 0.03);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 2rem;
}

.hero-content {
    flex: 1.3;
}

.hero-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    background: #ECFDF5;
    border: 1px solid #A7F3D0;
    padding: 0.25rem 0.8rem;
    border-radius: 999px;
    font-size: 0.75rem;
    font-weight: 700;
    color: #047857;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-bottom: 0.75rem;
}

.hero-title {
    font-family: 'Outfit', sans-serif;
    font-size: 2.35rem;
    font-weight: 800;
    line-height: 1.15;
    color: var(--emerald-deep);
    margin: 0 0 0.5rem 0;
    letter-spacing: -0.03em;
}

.hero-title span {
    background: linear-gradient(135deg, #059669 0%, #10B981 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    font-size: 1rem;
    color: #426356;
    line-height: 1.5;
    margin-bottom: 1.1rem;
    max-width: 650px;
}

.hero-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.hero-tag-item {
    font-size: 0.75rem;
    font-weight: 600;
    color: #064E3B;
    background: rgba(255, 255, 255, 0.9);
    border: 1px solid #C7E4D5;
    border-radius: 8px;
    padding: 0.25rem 0.65rem;
}

.hero-image-wrapper {
    flex: 0.9;
    max-width: 360px;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 8px 24px -4px rgba(6, 78, 59, 0.12);
    border: 1px solid #D2E7DC;
    transition: transform 0.3s ease;
}

.hero-image-wrapper:hover {
    transform: scale(1.02);
}

.hero-image-wrapper img {
    width: 100%;
    height: auto;
    display: block;
    object-fit: cover;
}

/* KPI Card Grid */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.25rem;
    margin-bottom: 2rem;
}

@media (max-width: 1024px) {
    .kpi-grid {
        grid-template-columns: repeat(2, 1fr);
    }
    .hero-card {
        flex-direction: column;
        align-items: flex-start;
    }
    .hero-image-wrapper {
        max-width: 100%;
        width: 100%;
    }
}

@media (max-width: 640px) {
    .kpi-grid {
        grid-template-columns: 1fr;
    }
}

.kpi-card {
    background: #FFFFFF;
    border: 1px solid #DDEBE3;
    border-radius: 16px;
    padding: 1.25rem 1.25rem;
    box-shadow: 0 4px 16px -2px rgba(6, 78, 59, 0.04), 0 1px 3px rgba(6, 78, 59, 0.02);
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    position: relative;
    overflow: hidden;
}

.kpi-card:hover {
    transform: translateY(-4px);
    border-color: #10B981;
    box-shadow: 0 12px 28px -6px rgba(16, 185, 129, 0.18);
}

.kpi-top-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 0.85rem;
}

.kpi-icon-box {
    width: 52px;
    height: 52px;
    border-radius: 13px;
    overflow: hidden;
    background: #ECFDF5;
    border: 1.5px solid #D1FAE5;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 2px 10px rgba(16, 185, 129, 0.12);
}

.kpi-icon-box img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.kpi-badge {
    background: #ECFDF5;
    color: #047857;
    font-size: 0.7rem;
    font-weight: 700;
    padding: 0.22rem 0.6rem;
    border-radius: 999px;
    border: 1px solid #A7F3D0;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}

.kpi-label {
    font-size: 0.76rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    color: #557769;
    margin-bottom: 0.25rem;
}

.kpi-number {
    font-family: 'Outfit', sans-serif;
    font-size: 1.95rem;
    font-weight: 800;
    color: #064E3B;
    line-height: 1.1;
    letter-spacing: -0.02em;
}

.kpi-note {
    font-size: 0.75rem;
    color: #6B877B;
    margin-top: 0.4rem;
}

/* Styled Streamlit Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background-color: #EDF5F1;
    padding: 6px;
    border-radius: 14px;
    border: 1px solid #D5E5DC;
    margin-bottom: 1.5rem;
}

.stTabs [data-baseweb="tab"] {
    height: 44px;
    border-radius: 10px;
    color: #2D4F42;
    font-weight: 600;
    font-size: 0.92rem;
    padding: 0 18px;
    transition: all 0.2s ease;
    border: none !important;
}

.stTabs [aria-selected="true"] {
    background-color: #FFFFFF !important;
    color: #064E3B !important;
    font-weight: 700 !important;
    box-shadow: 0 2px 10px rgba(6, 78, 59, 0.08) !important;
}

/* Content Container Card */
.content-box {
    background: #FFFFFF;
    border: 1px solid #DDEBE3;
    border-radius: 18px;
    padding: 1.4rem;
    box-shadow: 0 3px 14px rgba(6, 78, 59, 0.03);
    margin-bottom: 1.5rem;
}

/* Insight Cards */
.insight-card {
    background: #FFFFFF;
    border: 1px solid #D9EBE0;
    border-left: 5px solid #059669;
    border-radius: 14px;
    padding: 1.25rem 1.4rem;
    margin-bottom: 1rem;
    box-shadow: 0 2px 10px rgba(6, 78, 59, 0.03);
    transition: transform 0.2s ease, border-left-color 0.2s ease;
}

.insight-card:hover {
    transform: translateX(4px);
    border-left-color: #10B981;
}

.insight-title-row {
    font-family: 'Outfit', sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: #064E3B;
    margin-bottom: 0.35rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.insight-desc {
    font-size: 0.93rem;
    color: #38564B;
    line-height: 1.5;
}

/* Download CSV Button */
div.stDownloadButton > button {
    background: linear-gradient(135deg, #059669 0%, #047857 100%) !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.75rem 1.75rem !important;
    font-weight: 700 !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 0.95rem !important;
    box-shadow: 0 4px 14px rgba(5, 150, 105, 0.28) !important;
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

div.stDownloadButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 6px 22px rgba(5, 150, 105, 0.4) !important;
    background: linear-gradient(135deg, #10B981 0%, #059669 100%) !important;
}

/* Sidebar Branding Box */
.brand-box {
    background: linear-gradient(135deg, #064E3B 0%, #059669 100%);
    border-radius: 14px;
    padding: 1.25rem 1.15rem;
    color: #FFFFFF;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 16px rgba(6, 78, 59, 0.18);
}

.brand-title {
    font-family: 'Outfit', sans-serif;
    font-size: 1.25rem;
    font-weight: 800;
    color: #FFFFFF !important;
    margin: 0;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.brand-subtitle {
    font-size: 0.78rem;
    color: #D1FAE5;
    margin-top: 0.3rem;
    line-height: 1.35;
}

/* Footer Styling */
.footer-wrap {
    text-align: center;
    color: #6C8A7D;
    font-size: 0.85rem;
    padding: 2rem 0 1rem 0;
    border-top: 1px solid #DFEBE4;
    margin-top: 3rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------- PLOTLY EMERALD THEME HELPER ----------------
EMERALD_SEQUENCE = [
    "#059669",  # Main Emerald
    "#10B981",  # Mint / Vibrant
    "#047857",  # Deep Forest
    "#34D399",  # Soft Jade
    "#064E3B",  # Dark Spruce
    "#0D9488",  # Teal Accent
    "#6EE7B7",  # Pastel Mint
    "#14B8A6"   # Aqua Sage
]

def apply_emerald_theme(fig, title="", height=390):
    fig.update_layout(
        title={
            "text": f"<b>{title}</b>",
            "font": {"family": "Outfit, sans-serif", "size": 17, "color": "#064E3B"},
            "x": 0.02,
            "y": 0.94
        },
        font={"family": "Plus Jakarta Sans, sans-serif", "color": "#2C4A3E"},
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(247,250,248,0.6)",
        height=height,
        margin={"l": 25, "r": 25, "t": 55, "b": 25},
        hoverlabel={
            "bgcolor": "#064E3B",
            "font_size": 12,
            "font_family": "Plus Jakarta Sans, sans-serif",
            "font_color": "#FFFFFF"
        },
        xaxis={
            "gridcolor": "#E6EFEA",
            "zerolinecolor": "#D3E4DB",
            "tickfont": {"size": 11, "color": "#3D5A4F", "family": "Plus Jakarta Sans"}
        },
        yaxis={
            "gridcolor": "#E6EFEA",
            "zerolinecolor": "#D3E4DB",
            "tickfont": {"size": 11, "color": "#3D5A4F", "family": "Plus Jakarta Sans"}
        },
        legend={
            "orientation": "h",
            "yanchor": "bottom",
            "y": 1.02,
            "xanchor": "right",
            "x": 1,
            "font": {"size": 11, "color": "#2C4A3E"}
        }
    )
    return fig

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    return pd.read_csv("edupro_processed_data.csv")

df = load_data()

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.markdown("""
<div class="brand-box">
    <div class="brand-title">🎓 EduPro Analytics</div>
    <div class="brand-subtitle">Smart Learner Demographics & Revenue Intelligence Platform</div>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("### 🔍 Filter Parameters")

age_options = sorted(df["AgeGroup"].dropna().unique().tolist())
gender_options = sorted(df["Gender"].dropna().unique().tolist())
category_options = sorted(df["CourseCategory"].dropna().unique().tolist())
type_options = sorted(df["CourseType"].dropna().unique().tolist())

selected_age = st.sidebar.multiselect(
    "Age Group",
    age_options,
    default=age_options,
    help="Filter by learner age cohorts"
)

selected_gender = st.sidebar.multiselect(
    "Gender",
    gender_options,
    default=gender_options,
    help="Filter by learner gender"
)

selected_category = st.sidebar.multiselect(
    "Course Category",
    category_options,
    default=category_options,
    help="Filter by course subject domain"
)

selected_type = st.sidebar.multiselect(
    "Course Type",
    type_options,
    default=type_options,
    help="Filter between Free and Paid courses"
)

# ---------------- FILTER DATA ----------------
filtered_df = df[
    df["AgeGroup"].isin(selected_age)
    & df["Gender"].isin(selected_gender)
    & df["CourseCategory"].isin(selected_category)
    & df["CourseType"].isin(selected_type)
].copy()

# Sidebar quick filter statistics
filtered_ratio = (len(filtered_df) / len(df)) * 100 if len(df) > 0 else 0
st.sidebar.markdown(f"""
<div style="background:#FFFFFF; border:1px solid #D6E8DE; border-radius:12px; padding:0.9rem; margin-top:1.5rem;">
    <div style="font-size:0.75rem; font-weight:700; color:#064E3B; text-transform:uppercase; letter-spacing:0.05em; margin-bottom:0.25rem;">Active Filter Scope</div>
    <div style="font-family:'Outfit', sans-serif; font-size:1.35rem; font-weight:800; color:#059669;">{len(filtered_df):,} <span style="font-size:0.82rem; font-weight:500; color:#527366;">/ {len(df):,} records</span></div>
    <div style="width:100%; height:6px; background:#E2EFE7; border-radius:999px; margin-top:0.4rem; overflow:hidden;">
        <div style="width:{filtered_ratio}%; height:100%; background:linear-gradient(90deg, #10B981, #059669); border-radius:999px;"></div>
    </div>
    <div style="font-size:0.72rem; color:#6B877B; margin-top:0.35rem;">{filtered_ratio:.1f}% of total enrollment dataset</div>
</div>
""", unsafe_allow_html=True)

# ---------------- HERO HEADER ----------------
banner_img_html = f'<div class="hero-image-wrapper"><img src="{banner_b64}" alt="EduPro Analytics AI Illustration" /></div>' if banner_b64 else ''

st.markdown(f"""
<div class="hero-card">
    <div class="hero-content">
        <div class="hero-pill">
            <span style="font-size:0.9rem;">🟢</span> Live Intelligence Hub • 2025–2026
        </div>
        <h1 class="hero-title">EduPro <span>Learner Analysis</span></h1>
        <div class="hero-subtitle">
            Explore learner demographics, course enrollment behaviors, financial transactions, and automated performance insights with our curated emerald intelligence dashboard.
        </div>
        <div class="hero-tags">
            <div class="hero-tag-item">📊 <b>{len(filtered_df):,}</b> Active Records</div>
            <div class="hero-tag-item">🎓 <b>{df['CourseName'].nunique()}</b> Total Offerings</div>
            <div class="hero-tag-item">⚡ <b>{df['UserID'].nunique():,}</b> Global Learners</div>
            <div class="hero-tag-item">💎 Emerald & Off-White UI</div>
        </div>
    </div>
    {banner_img_html}
</div>
""", unsafe_allow_html=True)

# ---------------- KPI CARDS WITH 3D AI GENERATED ICONS ----------------
total_learners = filtered_df["UserID"].nunique()
total_courses = filtered_df["CourseID"].nunique()
total_enrollments = filtered_df["TransactionID"].nunique()
total_amount = filtered_df["Amount"].sum()

avg_spend_per_learner = (total_amount / total_learners) if total_learners > 0 else 0
enrollment_per_learner = (total_enrollments / total_learners) if total_learners > 0 else 0

learner_icon_tag = f'<img src="{icon_learners_b64}" alt="Learners Icon" />' if icon_learners_b64 else '👥'
courses_icon_tag = f'<img src="{icon_courses_b64}" alt="Courses Icon" />' if icon_courses_b64 else '📚'
enrollments_icon_tag = f'<img src="{icon_enrollments_b64}" alt="Enrollments Icon" />' if icon_enrollments_b64 else '📜'
revenue_icon_tag = f'<img src="{icon_revenue_b64}" alt="Revenue Icon" />' if icon_revenue_b64 else '💳'

st.markdown(f"""
<div class="kpi-grid">
    <div class="kpi-card">
        <div class="kpi-top-row">
            <div class="kpi-icon-box">{learner_icon_tag}</div>
            <div class="kpi-badge">Learners</div>
        </div>
        <div>
            <div class="kpi-label">Unique Learners</div>
            <div class="kpi-number">{total_learners:,}</div>
            <div class="kpi-note">Distinct registered students</div>
        </div>
    </div>
    <div class="kpi-card">
        <div class="kpi-top-row">
            <div class="kpi-icon-box">{courses_icon_tag}</div>
            <div class="kpi-badge">Catalog</div>
        </div>
        <div>
            <div class="kpi-label">Courses Enrolled</div>
            <div class="kpi-number">{total_courses:,}</div>
            <div class="kpi-note">Active courses in selection</div>
        </div>
    </div>
    <div class="kpi-card">
        <div class="kpi-top-row">
            <div class="kpi-icon-box">{enrollments_icon_tag}</div>
            <div class="kpi-badge">Activity</div>
        </div>
        <div>
            <div class="kpi-label">Total Enrollments</div>
            <div class="kpi-number">{total_enrollments:,}</div>
            <div class="kpi-note">~{enrollment_per_learner:.2f} courses per learner</div>
        </div>
    </div>
    <div class="kpi-card">
        <div class="kpi-top-row">
            <div class="kpi-icon-box">{revenue_icon_tag}</div>
            <div class="kpi-badge">Financials</div>
        </div>
        <div>
            <div class="kpi-label">Transaction Amount</div>
            <div class="kpi-number">${total_amount:,.2f}</div>
            <div class="kpi-note">Avg ${avg_spend_per_learner:,.2f} per learner</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

if filtered_df.empty:
    st.warning("⚠️ No records match the current sidebar filter parameters. Please widen your selection in the left sidebar.")
    st.stop()

# ---------------- NAVIGATION TABS ----------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Demographics & Learners",
    "📚 Course Popularity & Ratings",
    "📈 Enrollment & Revenue Trends",
    "💡 Strategic Insights",
    "📋 Data Explorer & CSV Export"
])

# ==================== TAB 1: DEMOGRAPHICS ====================
with tab1:
    col_d1, col_d2 = st.columns([1.1, 0.9])

    with col_d1:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        age_counts = (
            filtered_df.drop_duplicates("UserID")
            ["AgeGroup"].value_counts()
            .reindex(age_options, fill_value=0)
            .rename_axis("Age Group")
            .reset_index(name="Learners")
        )

        fig_age = px.bar(
            age_counts,
            x="Age Group",
            y="Learners",
            text="Learners",
            color="Learners",
            color_continuous_scale=["#6EE7B7", "#10B981", "#059669", "#064E3B"]
        )
        fig_age.update_traces(
            textposition="outside",
            marker_line_width=0,
            hovertemplate="<b>Age Group:</b> %{x}<br><b>Learners:</b> %{y:,}<extra></extra>"
        )
        fig_age.update_coloraxes(showscale=False)
        fig_age = apply_emerald_theme(fig_age, "Learner Distribution by Age Cohort", height=390)
        st.plotly_chart(fig_age, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_d2:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        gender_data = (
            filtered_df.drop_duplicates("UserID")["Gender"]
            .value_counts()
            .rename_axis("Gender")
            .reset_index(name="Learners")
        )

        fig_gender = px.pie(
            gender_data,
            names="Gender",
            values="Learners",
            hole=0.55,
            color="Gender",
            color_discrete_map={
                "Female": "#059669",
                "Male": "#10B981",
                "Other": "#34D399",
                "Prefer not to say": "#6EE7B7"
            } if set(gender_data["Gender"]).issubset({"Female", "Male", "Other", "Prefer not to say"}) else None,
            color_discrete_sequence=EMERALD_SEQUENCE
        )
        fig_gender.update_traces(
            textposition="inside",
            textinfo="percent+label",
            marker=dict(line=dict(color="#FFFFFF", width=3)),
            hovertemplate="<b>%{label}</b><br>Learners: %{value:,} (%{percent})<extra></extra>"
        )
        fig_gender = apply_emerald_theme(fig_gender, "Learners by Gender Identity", height=390)
        st.plotly_chart(fig_gender, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ==================== TAB 2: COURSE PERFORMANCE ====================
with tab2:
    col_c1, col_c2 = st.columns([1.1, 0.9])

    with col_c1:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        top_courses = (
            filtered_df.groupby("CourseName")["TransactionID"]
            .nunique()
            .sort_values(ascending=False)
            .head(10)
            .sort_values()
            .reset_index(name="Enrollments")
        )

        fig_courses = px.bar(
            top_courses,
            x="Enrollments",
            y="CourseName",
            orientation="h",
            text="Enrollments",
            color="Enrollments",
            color_continuous_scale=["#6EE7B7", "#10B981", "#059669", "#064E3B"]
        )
        fig_courses.update_traces(
            textposition="outside",
            marker_line_width=0,
            hovertemplate="<b>Course:</b> %{y}<br><b>Enrollments:</b> %{x:,}<extra></extra>"
        )
        fig_courses.update_coloraxes(showscale=False)
        fig_courses = apply_emerald_theme(fig_courses, "Top 10 Most Enrolled Courses", height=420)
        st.plotly_chart(fig_courses, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_c2:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        category_counts = (
            filtered_df.groupby("CourseCategory")["TransactionID"]
            .nunique()
            .reset_index(name="Enrollments")
            .sort_values("Enrollments", ascending=False)
        )

        fig_category = px.bar(
            category_counts,
            x="CourseCategory",
            y="Enrollments",
            color="CourseCategory",
            color_discrete_sequence=EMERALD_SEQUENCE,
            text="Enrollments"
        )
        fig_category.update_traces(
            textposition="outside",
            marker_line_width=0,
            hovertemplate="<b>Category:</b> %{x}<br><b>Enrollments:</b> %{y:,}<extra></extra>"
        )
        fig_category.update_layout(xaxis_tickangle=-35, showlegend=False)
        fig_category = apply_emerald_theme(fig_category, "Enrollment by Course Category", height=420)
        st.plotly_chart(fig_category, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    col_c3, col_c4 = st.columns(2)

    with col_c3:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        rating_data = (
            filtered_df.groupby("CourseCategory")["CourseRating"]
            .mean()
            .reset_index()
            .sort_values("CourseRating", ascending=False)
        )

        fig_rating = px.bar(
            rating_data,
            x="CourseCategory",
            y="CourseRating",
            color="CourseRating",
            color_continuous_scale=["#34D399", "#10B981", "#059669", "#064E3B"],
            text_auto=".2f",
            labels={"CourseCategory": "Category", "CourseRating": "Average Rating (0-5)"}
        )
        fig_rating.update_traces(
            textposition="outside",
            marker_line_width=0,
            hovertemplate="<b>Category:</b> %{x}<br><b>Rating:</b> %{y:.2f} ★<extra></extra>"
        )
        fig_rating.update_coloraxes(showscale=False)
        fig_rating.update_layout(xaxis_tickangle=-35, yaxis_range=[0, 5.2])
        fig_rating = apply_emerald_theme(fig_rating, "Average Course Rating by Category", height=380)
        st.plotly_chart(fig_rating, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_c4:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        level_data = (
            filtered_df.groupby("CourseLevel")["TransactionID"]
            .nunique()
            .reset_index(name="Enrollments")
        )

        fig_level = px.bar(
            level_data,
            x="CourseLevel",
            y="Enrollments",
            color="CourseLevel",
            color_discrete_sequence=["#059669", "#10B981", "#34D399"],
            text="Enrollments"
        )
        fig_level.update_traces(
            textposition="outside",
            marker_line_width=0,
            hovertemplate="<b>Level:</b> %{x}<br><b>Enrollments:</b> %{y:,}<extra></extra>"
        )
        fig_level.update_layout(showlegend=False)
        fig_level = apply_emerald_theme(fig_level, "Enrollment by Course Difficulty Level", height=380)
        st.plotly_chart(fig_level, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ==================== TAB 3: TRENDS & FINANCIALS ====================
with tab3:
    month_names = {
        1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr",
        5: "May", 6: "Jun", 7: "Jul", 8: "Aug",
        9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
    }

    col_t1, col_t2 = st.columns(2)

    with col_t1:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        monthly_counts = (
            filtered_df.groupby("EnrollmentMonth")["TransactionID"]
            .nunique()
            .reindex(range(1, 13), fill_value=0)
            .rename_axis("Month")
            .reset_index(name="Enrollments")
        )
        monthly_counts["MonthName"] = monthly_counts["Month"].map(month_names)

        fig_month = go.Figure()
        fig_month.add_trace(go.Scatter(
            x=monthly_counts["MonthName"],
            y=monthly_counts["Enrollments"],
            mode="lines+markers",
            line=dict(color="#059669", width=3.5, shape="spline"),
            marker=dict(size=8, color="#047857", line=dict(color="#FFFFFF", width=2)),
            fill="tozeroy",
            fillcolor="rgba(16, 185, 129, 0.12)",
            name="Enrollments",
            hovertemplate="<b>Month:</b> %{x}<br><b>Enrollments:</b> %{y:,}<extra></extra>"
        ))
        fig_month = apply_emerald_theme(fig_month, "Monthly Enrollment Trend (Annual Cycle)", height=390)
        st.plotly_chart(fig_month, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_t2:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        monthly_amount = (
            filtered_df.groupby("EnrollmentMonth")["Amount"]
            .sum()
            .reindex(range(1, 13), fill_value=0)
            .rename_axis("Month")
            .reset_index(name="Total Amount")
        )
        monthly_amount["MonthName"] = monthly_amount["Month"].map(month_names)

        fig_amount = go.Figure()
        fig_amount.add_trace(go.Scatter(
            x=monthly_amount["MonthName"],
            y=monthly_amount["Total Amount"],
            mode="lines+markers",
            line=dict(color="#047857", width=3.5, shape="spline"),
            marker=dict(size=8, color="#064E3B", line=dict(color="#FFFFFF", width=2)),
            fill="tozeroy",
            fillcolor="rgba(5, 150, 105, 0.12)",
            name="Revenue ($)",
            hovertemplate="<b>Month:</b> %{x}<br><b>Revenue:</b> $%{y:,.2f}<extra></extra>"
        ))
        fig_amount = apply_emerald_theme(fig_amount, "Monthly Transaction Revenue Trend", height=390)
        st.plotly_chart(fig_amount, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    col_t3, col_t4 = st.columns([1, 1])

    with col_t3:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        type_counts = (
            filtered_df.groupby("CourseType")["TransactionID"]
            .nunique()
            .reset_index(name="Enrollments")
        )

        fig_type = px.pie(
            type_counts,
            names="CourseType",
            values="Enrollments",
            hole=0.55,
            color="CourseType",
            color_discrete_map={"Free": "#34D399", "Paid": "#059669"}
        )
        fig_type.update_traces(
            textposition="inside",
            textinfo="percent+label",
            marker=dict(line=dict(color="#FFFFFF", width=3)),
            hovertemplate="<b>%{label} Courses</b><br>Enrollments: %{value:,} (%{percent})<extra></extra>"
        )
        fig_type = apply_emerald_theme(fig_type, "Free vs Paid Course Breakdown", height=370)
        st.plotly_chart(fig_type, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_t4:
        st.markdown('<div class="content-box">', unsafe_allow_html=True)
        if "PaymentMethod" in filtered_df.columns:
            payment_counts = (
                filtered_df.groupby("PaymentMethod")["TransactionID"]
                .nunique()
                .reset_index(name="Transactions")
                .sort_values("Transactions", ascending=False)
            )
            fig_payment = px.bar(
                payment_counts,
                x="PaymentMethod",
                y="Transactions",
                color="PaymentMethod",
                color_discrete_sequence=EMERALD_SEQUENCE,
                text="Transactions"
            )
            fig_payment.update_traces(
                textposition="outside",
                marker_line_width=0,
                hovertemplate="<b>Payment:</b> %{x}<br><b>Count:</b> %{y:,}<extra></extra>"
            )
            fig_payment.update_layout(showlegend=False)
            fig_payment = apply_emerald_theme(fig_payment, "Preferred Payment Methods", height=370)
            st.plotly_chart(fig_payment, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ==================== TAB 4: STRATEGIC INSIGHTS ====================
with tab4:
    st.markdown("""
    <div style="margin-bottom:1.25rem;">
        <h3 style="margin:0 0 0.3rem 0; font-family:'Outfit', sans-serif; color:#064E3B;">💡 Automated Strategic Intelligence</h3>
        <p style="margin:0; font-size:0.92rem; color:#426356;">Synthesized takeaways computed in real-time from your active filter selection.</p>
    </div>
    """, unsafe_allow_html=True)

    col_ins1, col_ins2 = st.columns(2)

    # Insight 1: Most popular course
    course_counts = filtered_df["CourseName"].value_counts()
    if not course_counts.empty:
        popular_course = course_counts.idxmax()
        popular_count = course_counts.max()
        pct_of_enrollments = (popular_count / len(filtered_df)) * 100

        with col_ins1:
            st.markdown(f"""
            <div class="insight-card">
                <div class="insight-title-row">
                    <span>🏆</span> Most Popular Course Offering
                </div>
                <div class="insight-desc">
                    <b>{popular_course}</b> leads the catalog with <b>{popular_count:,}</b> enrollments, representing <b>{pct_of_enrollments:.1f}%</b> of all filtered registrations.
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Insight 2: Most popular category
    category_counts = filtered_df["CourseCategory"].value_counts()
    if not category_counts.empty:
        popular_category = category_counts.idxmax()
        category_count = category_counts.max()
        pct_cat = (category_count / len(filtered_df)) * 100

        with col_ins2:
            st.markdown(f"""
            <div class="insight-card">
                <div class="insight-title-row">
                    <span>📚</span> Dominant Subject Category
                </div>
                <div class="insight-desc">
                    <b>{popular_category}</b> ranks as the highest-demand category with <b>{category_count:,}</b> enrollments (<b>{pct_cat:.1f}%</b> of active volume).
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Insight 3: Peak enrollment month
    full_month_names = {
        1: "January", 2: "February", 3: "March",
        4: "April", 5: "May", 6: "June",
        7: "July", 8: "August", 9: "September",
        10: "October", 11: "November", 12: "December"
    }
    monthly_counts_agg = filtered_df.groupby("EnrollmentMonth")["TransactionID"].nunique()

    if not monthly_counts_agg.empty:
        highest_month = monthly_counts_agg.idxmax()
        highest_month_name = full_month_names.get(int(highest_month), str(highest_month))
        highest_month_count = monthly_counts_agg.max()

        with col_ins1:
            st.markdown(f"""
            <div class="insight-card">
                <div class="insight-title-row">
                    <span>📅</span> Peak Enrollment Season
                </div>
                <div class="insight-desc">
                    <b>{highest_month_name}</b> registered the highest single-month activity with <b>{highest_month_count:,}</b> student enrollments.
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Insight 4: Free vs Paid
    if "CourseType" in filtered_df.columns:
        type_counts_agg = filtered_df["CourseType"].value_counts()
        if not type_counts_agg.empty:
            most_common_type = type_counts_agg.idxmax()
            type_count_val = type_counts_agg.max()
            pct_type = (type_count_val / len(filtered_df)) * 100

            with col_ins2:
                st.markdown(f"""
                <div class="insight-card">
                <div class="insight-title-row">
                    <span>💎</span> Primary Enrollment Model
                </div>
                <div class="insight-desc">
                    <b>{most_common_type}</b> courses account for the primary share with <b>{type_count_val:,}</b> enrollments (<b>{pct_type:.1f}%</b> of total).
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Insight 5: Revenue & Monetization
    with col_ins1:
        st.markdown(f"""
        <div class="insight-card">
            <div class="insight-title-row">
                <span>💰</span> Cumulative Transaction Volume
            </div>
            <div class="insight-desc">
                The total recorded transaction volume across the selected criteria stands at <b>${total_amount:,.2f}</b>, averaging <b>${avg_spend_per_learner:,.2f}</b> per active learner.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Insight 6: Rating Health
    if "CourseRating" in filtered_df.columns:
        overall_rating = filtered_df["CourseRating"].mean()
        high_rated_count = len(filtered_df[filtered_df["CourseRating"] >= 4.0])
        pct_high_rated = (high_rated_count / len(filtered_df)) * 100

        with col_ins2:
            st.markdown(f"""
            <div class="insight-card">
                <div class="insight-title-row">
                    <span>⭐</span> Catalog Quality & Learner Satisfaction
                </div>
                <div class="insight-desc">
                    The average course rating across filtered records is <b>{overall_rating:.2f} / 5.0</b>, with <b>{pct_high_rated:.1f}%</b> of records rated 4.0 or above.
                </div>
            </div>
            """, unsafe_allow_html=True)

# ==================== TAB 5: DATA EXPLORER & EXPORT ====================
with tab5:
    st.markdown("""
    <div style="margin-bottom:1rem;">
        <h3 style="margin:0 0 0.3rem 0; font-family:'Outfit', sans-serif; color:#064E3B;">📋 Filtered Enrollment Records Explorer</h3>
        <p style="margin:0; font-size:0.92rem; color:#426356;">Inspect records with active parameters or export the slice directly to CSV.</p>
    </div>
    """, unsafe_allow_html=True)

    display_columns = [
        "TransactionID",
        "UserID",
        "UserName",
        "Age",
        "Gender",
        "CourseName",
        "CourseCategory",
        "CourseType",
        "CourseLevel",
        "CoursePrice",
        "CourseRating",
        "EnrollmentMonth",
        "Amount",
        "PaymentMethod"
    ]
    display_columns = [col for col in display_columns if col in filtered_df.columns]

    st.dataframe(
        filtered_df[display_columns],
        use_container_width=True,
        hide_index=True
    )

    col_exp1, col_exp2 = st.columns([1, 1])
    with col_exp1:
        st.markdown(f"""
        <div style="font-size:0.85rem; font-weight:600; color:#064E3B; padding-top:0.6rem;">
            Displaying <b>{len(filtered_df):,}</b> records • Ready for export
        </div>
        """, unsafe_allow_html=True)

    with col_exp2:
        csv_data = filtered_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Download Filtered Data as CSV",
            data=csv_data,
            file_name="edupro_filtered_data.csv",
            mime="text/csv",
            use_container_width=True
        )

# ---------------- DASHBOARD FOOTER ----------------
st.markdown("""
<div class="footer-wrap">
    <span style="font-weight:700; color:#064E3B;">EduPro Analytics Hub</span> •Academic Data Analysis Project
</div>
""", unsafe_allow_html=True)
