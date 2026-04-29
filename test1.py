import streamlit as st
import math

# ===== Custom CSS =====
st.markdown("""
    <style>
    body {
        background-color: #f4f6f9;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        color: #2c3e50;
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: #7f8c8d;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# ===== Title =====
st.markdown("<div class='title'>🛠️ Terzaghi Bearing Capacity Calculator</div>", unsafe_allow_html=True)

# ===== Input Section =====
st.sidebar.header("Input Parameters")
c = st.sidebar.number_input("Cohesion (c) [kN/m²]", min_value=0.0, value=25.0)
phi = st.sidebar.number_input("Friction Angle (φ) [degrees]", min_value=0.0, max_value=45.0, value=30.0)
gamma = st.sidebar.number_input("Unit Weight (γ) [kN/m³]", min_value=0.0, value=18.0)
Df = st.sidebar.number_input("Foundation Depth (Df) [m]", min_value=0.0, value=1.5)
B = st.sidebar.number_input("Foundation Width (B) [m]", min_value=0.0, value=2.0)

# ===== Bearing Capacity Factors =====
phi_rad = math.radians(phi)
Nq = math.exp(math.pi * math.tan(phi_rad)) * (math.tan(math.radians(45) + phi_rad/2))**2
Nc = (Nq - 1) / math.tan(phi_rad) if phi > 0 else 5.7
Ngamma = 2 * (Nq + 1) * math.tan(phi_rad)

# ===== Terzaghi Equation =====
qult = c * Nc + gamma * Df * Nq + 0.5 * gamma * B * Ngamma
qall = qult / 3.0  # Factor of safety assumed = 3

# ===== Output =====
st.subheader("📊 Results")
st.write(f"Ultimate Bearing Capacity (q_ult): **{qult:.2f} kN/m²**")
st.write(f"Allowable Bearing Capacity (q_all): **{qall:.2f} kN/m²**")

# ===== Footer =====
st.markdown("<div class='footer'>Developed by Geotechnical Engineer | Powered by Streamlit</div>", unsafe_allow_html=True)
