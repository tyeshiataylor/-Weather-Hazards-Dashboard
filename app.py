import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page config 
st.set_page_config(
    page_title="Global Weather Hazards | Human Impact Dashboard",
    page_icon="🌪️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=DM+Sans:wght@300;400;500&display=swap');
  html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; background-color: #0d1117; color: #e6edf3; }
  section[data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
  section[data-testid="stSidebar"] * { color: #e6edf3 !important; }
  .dashboard-title { font-family: 'Bebas Neue', sans-serif; font-size: 3rem; letter-spacing: 0.08em; color: #f0f6fc; margin-bottom: 0; line-height: 1; }
  .dashboard-subtitle { font-size: 0.95rem; color: #8b949e; margin-top: 4px; margin-bottom: 1.5rem; font-weight: 300; }
  .kpi-card { background: #161b22; border: 1px solid #30363d; border-radius: 10px; padding: 1.2rem 1.5rem; text-align: center; }
  .kpi-value { font-family: 'Bebas Neue', sans-serif; font-size: 2.4rem; letter-spacing: 0.05em; margin: 0; line-height: 1; }
  .kpi-label { font-size: 0.78rem; color: #8b949e; text-transform: uppercase; letter-spacing: 0.1em; margin-top: 4px; }
  .kpi-deaths { color: #f85149; } .kpi-affect { color: #e3b341; } .kpi-events { color: #58a6ff; } .kpi-damage { color: #3fb950; }
  .section-header { font-family: 'Bebas Neue', sans-serif; font-size: 1.5rem; letter-spacing: 0.07em; color: #f0f6fc; border-left: 4px solid #58a6ff; padding-left: 0.6rem; margin-top: 2rem; margin-bottom: 0.8rem; }
  hr { border-color: #30363d; }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="dashboard-title">🌪️ Global Weather Hazards</p>', unsafe_allow_html=True)
st.markdown('<p class="dashboard-subtitle">Human Impact Analysis · EM-DAT Dataset · 2000–2026 · University of Westminster</p>', unsafe_allow_html=True)

# ── Data loading ──────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_excel("data/emdat-country-profiles_2026_04_17 (1).xlsx", header=0)
    df = df.iloc[1:].reset_index(drop=True)
    df.columns = [
        "Year", "Country", "ISO", "Disaster Group", "Disaster Subgroup",
        "Disaster Type", "Disaster Subtype", "Total Events",
        "Total Affected", "Total Deaths",
        "Total Damage Original", "Total Damage Adjusted", "CPI"
    ]
    for col in ["Year", "Total Events", "Total Affected",
                "Total Deaths", "Total Damage Original", "Total Damage Adjusted"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df[df["Disaster Group"] == "Natural"]
    return df

df = load_data()

# ── Sidebar filters ───────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🌪️ Dashboard Filters")
    st.markdown("---")
    year_min, year_max = int(df["Year"].min()), int(df["Year"].max())
    year_range = st.slider("📅 Year Range", year_min, year_max, (2000, 2024))
    disaster_types = sorted(df["Disaster Type"].dropna().unique())
    selected_types = st.multiselect("🌊 Disaster Type", options=disaster_types, default=disaster_types)
    subgroups = sorted(df["Disaster Subgroup"].dropna().unique())
    selected_subgroups = st.multiselect("📂 Disaster Subgroup", options=subgroups, default=subgroups)
    all_countries = sorted(df["Country"].dropna().unique())
    selected_countries = st.multiselect("🌍 Filter by Country (optional)", options=all_countries, default=[], placeholder="All countries")
    st.markdown("---")
    st.caption("Data source: EM-DAT via Humanitarian Data Exchange (HDX)")

# ── Apply filters ─────────────────────────────────────────────────────────────
filtered = df[
    (df["Year"] >= year_range[0]) &
    (df["Year"] <= year_range[1]) &
    (df["Disaster Type"].isin(selected_types)) &
    (df["Disaster Subgroup"].isin(selected_subgroups))
]
if selected_countries:
    filtered = filtered[filtered["Country"].isin(selected_countries)]

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<p class="dashboard-title">🌪️ Global Weather Hazards</p>', unsafe_allow_html=True)
st.markdown('<p class="dashboard-subtitle">Human Impact Analysis · EM-DAT Dataset · 2000–2026 · University of Westminster</p>', unsafe_allow_html=True)

# ── KPI Cards ─────────────────────────────────────────────────────────────────
total_deaths   = int(filtered["Total Deaths"].sum())
total_affected = int(filtered["Total Affected"].sum())
total_events   = int(filtered["Total Events"].sum())
total_damage   = filtered["Total Damage Adjusted"].sum()

def fmt(n):
    if n >= 1_000_000_000: return f"${n/1e9:.1f}B"
    if n >= 1_000_000: return f"${n/1e6:.1f}M"
    if n >= 1_000: return f"${n/1e3:.0f}K"
    return f"${n:.0f}"

c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f'<div class="kpi-card"><p class="kpi-value kpi-deaths">{total_deaths:,}</p><p class="kpi-label">Total Deaths</p></div>', unsafe_allow_html=True)
with c2:
    st.markdown(f'<div class="kpi-card"><p class="kpi-value kpi-affect">{total_affected:,}</p><p class="kpi-label">People Affected</p></div>', unsafe_allow_html=True)
with c3:
    st.markdown(f'<div class="kpi-card"><p class="kpi-value kpi-events">{total_events:,}</p><p class="kpi-label">Total Events</p></div>', unsafe_allow_html=True)
with c4:
    st.markdown(f'<div class="kpi-card"><p class="kpi-value kpi-damage">{fmt(total_damage)}</p><p class="kpi-label">Economic Damage (adj.)</p></div>', unsafe_allow_html=True)