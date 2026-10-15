import streamlit as st
import pandas as pd
import numpy as np

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="SmartClass. AI Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM DARK THEME STYLING ---
st.markdown("""
    <style>
    .main { background-color: #0a0a0a; color: #f5f5f5; }
    .sidebar .sidebar-content { background-color: #121212; }
    div.stMetric { background-color: #171717; padding: 15px; border-radius: 12px; border: 1px solid #262626; }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("### ⚡ Smart Classroom.")
    st.caption("Workspace / Room 301")
    
    selected_tab = st.radio(
        "Navigation", 
        ["Dashboard", "Analytics", "Devices", "Alerts", "Settings"]
    )
    
    st.markdown("---")
    st.markdown("##### System Status")
    st.success("System online • 6 devices connected")
    
    # Simulated hardware signal bars
    cols = st.columns(10)
    for i, col in enumerate(cols):
        color = "#ccff00" if i < 8 else "#333333"
        col.markdown(f"<div style='background-color: {color}; height: 12px; border-radius: 2px;'></div>", unsafe_allow_html=True)

# --- MAIN CONTENT ---
if selected_tab == "Dashboard":
    
    # Header Section
    st.markdown("### Room overview.")
    st.caption("A comfortable classroom. A smarter way to manage it.")
    
    # Top Metric Cards Row
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        st.markdown("""
            <div style='background-color: #ccff00; padding: 15px; border-radius: 12px; color: #000000;'>
                <small style='font-weight: bold; text-transform: uppercase;'>Live reading</small>
                <h2 style='margin: 5px 0;'>26.1°C</h2>
                <small style='font-weight: bold;'>Normal • Temperature</small>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.metric(label="Humidity (Live)", value="61%", delta="Normal")
    with col3:
        st.metric(label="Occupancy", value="24 people", delta="40 capacity")
    with col4:
        st.metric(label="Light Level", value="72%", delta="Normal")
    with col5:
        st.metric(label="Energy Usage", value="3.7 kWh", delta="Today")
    with col6:
        st.metric(label="Room Status", value="Occupied", delta="Class in session")

    st.markdown("<br>", unsafe_allow_html=True)

    # Charts and Controls Grid
    grid_col1, grid_col2 = st.columns([2, 1])
    
    with grid_col1:
        st.markdown("##### Live Environment (Real-time Stream)")
        chart_data = pd.DataFrame(
            np.random.randn(20, 2) * [0.5, 2] + [26.1, 61],
            columns=['Temperature (°C)', 'Humidity (%)']
        )
        st.line_chart(chart_data, color=["#ccff00", "#3b82f6"])

    with grid_col2:
        st.markdown("##### Room Controls")
        lights = st.toggle("Classroom lights (72% bright)", value=True)
        ac = st.toggle("Air conditioning (Cooling to 24°C)", value=True)
        auto_mode = st.toggle("Automatic mode (ML-driven)", value=False)
        
        if auto_mode:
            st.info("🤖 GenAI + ML Autopilot active: Adjusting room climate automatically based on occupancy.")

    # Recent Alerts Section
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("##### Recent Alerts")
    st.warning("⚠️ **Room temperature exceeded 30°C spike.** Triggered by ML Anomaly Detection Engine 12 mins ago.")

elif selected_tab == "Analytics":
    st.markdown("### Advanced ML Analytics")
    st.write("Detailed historical telemetry charts for energy optimization and predictive maintenance.")
    df_history = pd.DataFrame(np.random.randn(50, 3), columns=['Energy Load', 'Predicted Load', 'Anomaly Score'])
    st.area_chart(df_history)

elif selected_tab == "Devices":
    st.markdown("### Connected Hardware Nodes")
    st.table([
        {"Device": "Temperature Sensor #301", "Type": "IoT Node", "Status": "Online", "Battery": "94%"},
        {"Device": "Humidity & Air Quality Monitor", "Type": "IoT Node", "Status": "Online", "Battery": "88%"},
        {"Device": "Smart AC Relay Controller", "Type": "Actuator", "Status": "Online", "Power": "Active"},
        {"Device": "Smart LED Dimmable Driver", "Type": "Actuator", "Status": "Online", "Power": "Active"}
    ])

elif selected_tab == "Alerts":
    st.markdown("### System Alert Logs")
    st.error("14:02 - Temperature threshold warning in Room 301.")
    st.success("12:30 - Routine system diagnostic check completed with zero errors.")

elif selected_tab == "Settings":
    st.markdown("### Configuration & Gemini API Integration")
    st.text_input("Gemini API Key", type="password", placeholder="Enter your API key here...")
    st.number_input("Temperature Threshold Limit (°C)", value=30.0)
    st.button("Save Configurations")
