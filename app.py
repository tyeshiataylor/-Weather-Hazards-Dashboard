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

# ── Chart theme ───────────────────────────────────────────────────────────────
CHART_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="DM Sans", color="#8b949e"),
    title_font=dict(family="DM Sans", color="#e6edf3", size=14),
    legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color="#8b949e")),
    xaxis=dict(gridcolor="#21262d", zerolinecolor="#21262d", color="#8b949e"),
    yaxis=dict(gridcolor="#21262d", zerolinecolor="#21262d", color="#8b949e"),
    margin=dict(t=40, b=40, l=40, r=20),
)

# ── World Map ─────────────────────────────────────────────────────────────────
st.markdown('<p class="section-header">Global Impact Map</p>', unsafe_allow_html=True)
map_metric = st.radio("Colour map by:", ["Total Deaths", "Total Affected", "Total Events"], horizontal=True)
map_data = (
    filtered.groupby(["Country", "ISO"])[map_metric]
    .sum().reset_index().dropna(subset=[map_metric])
)
fig_map = px.choropleth(
    map_data, locations="ISO", color=map_metric,
    hover_name="Country", color_continuous_scale="Reds",
)
fig_map.update_layout(
    **CHART_LAYOUT,
    geo=dict(
        bgcolor="rgba(0,0,0,0)", showframe=False,
        showcoastlines=True, coastlinecolor="#30363d",
        showland=True, landcolor="#161b22",
        showocean=True, oceancolor="#0d1117",
        lakecolor="#0d1117", showcountries=True, countrycolor="#30363d",
    ),
    coloraxis_colorbar=dict(tickfont=dict(color="#8b949e"), title=dict(font=dict(color="#8b949e"))),
    height=450,
)
st.plotly_chart(fig_map, use_container_width=True)
# ── Trends Over Time ──────────────────────────────────────────────────────────
st.markdown('<p class="section-header">Trends Over Time</p>', unsafe_allow_html=True)

col_l, col_r = st.columns(2)

with col_l:
    deaths_time = filtered.groupby("Year")["Total Deaths"].sum().reset_index()
    fig_deaths = px.line(
        deaths_time, x="Year", y="Total Deaths",
        title="Deaths per Year",
        markers=True,
        color_discrete_sequence=["#f85149"],
    )
    fig_deaths.update_traces(line=dict(width=2.5), marker=dict(size=5))
    fig_deaths.update_layout(**CHART_LAYOUT, height=320)
    st.plotly_chart(fig_deaths, use_container_width=True)

with col_r:
    affected_time = (
        filtered.groupby(["Year", "Disaster Type"])["Total Affected"]
        .sum().reset_index()
    )
    fig_affected = px.area(
        affected_time, x="Year", y="Total Affected",
        color="Disaster Type",
        title="People Affected by Disaster Type",
        color_discrete_sequence=px.colors.qualitative.Bold,
    )
    fig_affected.update_layout(**CHART_LAYOUT, height=320)
    st.plotly_chart(fig_affected, use_container_width=True)

# ── Disaster Type Breakdown ───────────────────────────────────────────────────
st.markdown('<p class="section-header">Disaster Type Breakdown</p>', unsafe_allow_html=True)
col_a, col_b = st.columns(2)
with col_a:
    type_deaths = filtered.groupby("Disaster Type")["Total Deaths"].sum().reset_index().sort_values("Total Deaths", ascending=True)
    fig_bar = px.bar(type_deaths, x="Total Deaths", y="Disaster Type", orientation="h", title="Total Deaths by Disaster Type", color="Total Deaths", color_continuous_scale="Reds")
    fig_bar.update_layout(**CHART_LAYOUT, height=380, showlegend=False, coloraxis_showscale=False)
    st.plotly_chart(fig_bar, use_container_width=True)
with col_b:
    subgroup_events = filtered.groupby("Disaster Subgroup")["Total Events"].sum().reset_index()
    fig_pie = px.pie(subgroup_events, values="Total Events", names="Disaster Subgroup", title="Events by Disaster Subgroup", color_discrete_sequence=px.colors.qualitative.Bold, hole=0.45)
    fig_pie.update_traces(textfont_color="#e6edf3")
    fig_pie.update_layout(**CHART_LAYOUT, height=380)
    st.plotly_chart(fig_pie, use_container_width=True)
# ── Human vs Economic Cost ────────────────────────────────────────────────────
st.markdown('<p class="section-header">Human vs Economic Cost</p>', unsafe_allow_html=True)
col_x, col_y = st.columns(2)

with col_x:
    scatter_data = (
        filtered.groupby("Country")[["Total Deaths", "Total Damage Adjusted", "Total Affected"]]
        .sum().reset_index().dropna()
    )
    scatter_data = scatter_data[scatter_data["Total Deaths"] > 0]
    fig_scatter = px.scatter(
        scatter_data, x="Total Damage Adjusted", y="Total Deaths",
        size="Total Affected", hover_name="Country",
        title="Economic Damage vs Deaths (bubble = people affected)",
        color="Total Deaths", color_continuous_scale="OrRd",
        size_max=50, log_x=True, log_y=True,
    )
    fig_scatter.update_layout(**CHART_LAYOUT, height=380, coloraxis_showscale=False)
    st.plotly_chart(fig_scatter, use_container_width=True)

with col_y:
    top10 = (
        filtered.groupby("Country")["Total Affected"]
        .sum().nlargest(10).reset_index()
        .sort_values("Total Affected", ascending=True)
    )
    fig_top = px.bar(
        top10, x="Total Affected", y="Country",
        orientation="h", title="Top 10 Most Affected Countries",
        color="Total Affected", color_continuous_scale="Blues",
    )
    fig_top.update_layout(**CHART_LAYOUT, height=380, showlegend=False, coloraxis_showscale=False)
    st.plotly_chart(fig_top, use_container_width=True)

# ── Data Explorer ─────────────────────────────────────────────────────────────
st.markdown('<p class="section-header">Data Explorer</p>', unsafe_allow_html=True)
with st.expander("📋 View filtered dataset"):
    st.dataframe(
        filtered.sort_values("Total Deaths", ascending=False).reset_index(drop=True),
        use_container_width=True,
        height=350,
    )

st.markdown("---")
st.caption("Data: EM-DAT Country Profiles — Centre for Research on the Effect of Disasters (CRED) via HDX | Dashboard by Tyeshia Taylor|University of Westminster")