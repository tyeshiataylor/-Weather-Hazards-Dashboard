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