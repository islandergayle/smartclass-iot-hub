import streamlit as st
import pandas as pd
import numpy as np

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="SmartClass AI Dashboard",
    page_icon="⚡",
    layout="wide"
)

# --- TITLE ---
st.title("⚡ Smart Classroom AI Dashboard")
st.caption("Workspace / Room 301 - Live IoT Monitoring")

# --- METRICS ROW ---
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Temperature", value="26.1°C", delta="Normal")
with col2:
    st.metric(label="Humidity", value="61%", delta="Normal")
with col3:
    st.metric(label="Occupancy", value="24 people", delta="40 capacity")
with col4:
    st.metric(label="Energy Usage", value="3.7 kWh", delta="Today")

st.markdown("---")

# --- CHART & CONTROLS ---
left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("Live Environment Stream")
    chart_data = pd.DataFrame(
        np.random.randn(20, 2) * [0.5, 2] + [26.1, 61],
        columns=['Temperature (°C)', 'Humidity (%)']
    )
    st.line_chart(chart_data)

with right_col:
    st.subheader("Room Controls")
    lights = st.toggle("Classroom Lights", value=True)
    ac = st.toggle("Air Conditioning", value=True)
    auto_mode = st.toggle("Automatic ML Mode", value=False)
    
    if auto_mode:
        st.info("Autopilot active: Adjusting climate automatically.")

# --- ALERTS ---
st.markdown("---")
st.subheader("Recent System Alerts")
st.warning("⚠️ Room temperature normal. ML Anomaly Detection Engine running smoothly.")
