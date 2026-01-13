import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- 1. PAGE SETUP (The "Canvas") ---
st.set_page_config(
    page_title="My Portfolio", 
    page_icon="🧵", 
    layout="wide"
)

# --- 2. SIDEBAR (The Navigation & Quick Info) ---
with st.sidebar:
    # You can replace this URL with a path to your actual photo later!
    st.image("https://images.unsplash.com/photo-1550684848-fac1c5b4e853", caption="Textile Engineer")
    st.markdown("### 📧 Contact Me")
    st.write("📍 Giza, Egypt")
    st.write("✉️ email@example.com")
    
    st.divider()
    
    st.markdown("### 🗣️ Languages")
    st.caption("Arabic (Native)")
    st.caption("English (Fluent)")
    st.caption("Japanese (Learning 🇯🇵)")
    st.caption("Korean (Learning 🇰🇷)")

# --- 3. MAIN HEADER ---
st.title("🧵 [Your Name]")
st.markdown("##### Textile Engineer | Nanofiber Researcher | Visual Designer")
st.write("Bridging the gap between *material science* and *human comfort*.")

st.divider()

# --- 4. THE CONTENT TABS ---
# This matches your desire to show different "aspects" of yourself
tab_home, tab_research, tab_hobbies, tab_history = st.tabs([
    "🏠 Home", 
    "🔬 Research & Engineering", 
    "🎨 Creative & Languages",
    "🕌 History & Faith"
])

# === TAB 1: HOME (Jikoshoukai) ===
with tab_home:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://images.unsplash.com/photo-1492571350019-22de08371fd3", caption="Focus Mode")
        
    with col2:
        st.subheader("はじめまして (Nice to meet you)")
        st.write("""
        **Hello! I am a Textile Engineer based in Egypt.**
        
        I specialize in **Nanofiber Fabrication** and **Yarn Production**, but my passion extends beyond the lab. 
        I believe in the intersection of technology, art, and tradition.
        
        * **Current Focus:** ZnO-PVDF electrospun nanofibers for energy scavenging.
        * **Goal:** Developing smart garments that provide comfort and utility.
        """)
        
        if st.button("✨ Click for a Fun Fact"):
            st.success("I also build PCs and love troubleshooting hardware! 💻")
            st.balloons()

# === TAB 2: RESEARCH (The "Project A" Graph) ===
with tab_research:
    st.header("🧪 Nanofiber Lab Data")
    st.write("Below is a simulation of the Tensile Stress-Strain curve for my recent PVDF samples.")
    
    # -- THE PYTHON GRAPH CODE --
    # 1. Generate Data
    strain = np.linspace(0, 15, 100)
    stress = 20 * (1 - np.exp(-0.3 * strain)) + (0.5 * strain)
    
    # 2. Plotting
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(strain, stress, color='#E91E63', linewidth=3, label='PVDF Nanofiber')
    ax.set_title("Stress-Strain Curve (Simulated)", fontweight='bold')
    ax.set_xlabel("Strain (%)")
    ax.set_ylabel("Stress (MPa)")
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend()
    
    # 3. Show Graph in Streamlit
    col_graph, col_stats = st.columns([2, 1])
    
    with col_graph:
        st.pyplot(fig)
        
    with col_stats:
        st.info("**Key Metrics**")
        st.metric(label="Yield Strength", value="7.5 MPa", delta="0.5 MPa")
        st.metric(label="Elastic Modulus", value="120 MPa")
        st.write("Sample shows promising piezoelectric properties suitable for wearable sensors.")

# === TAB 3: CREATIVE & LANGUAGES ===
with tab_hobbies:
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.header("🇯🇵 Japanese Journey")
        st.write("Documenting my progress in learning Japanese.")
        st.progress(30, text="Kanji Proficiency")
        st.code("継続は力なり (Keizoku wa chikara nari) - 'Continuance is power.'")
        
    with col_b:
        st.header("📸 Photography & Design")
        st.write("Using visual media to communicate scientific concepts.")
        # Gallery Placeholder
        st.image("https://images.unsplash.com/photo-1626785774573-4b799314346d", caption="Graphic Design Work")

# === TAB 4: HISTORY & FAITH ===
with tab_history:
    st.header("📚 Islamic & Historic Studies")
    st.markdown("""
    > *"Read! In the Name of your Lord, Who has created..."*
    """)
    st.write("""
    I am deeply interested in the history of Islamic civilization and Quranic studies. 
    I believe understanding our past is key to building a balanced future.
    """)
    
    # Expandable section for details
    with st.expander("See my current reading list"):
        st.checkbox("The Sealed Nectar (Ar-Raheeq Al-Makhtum)")
        st.checkbox("History of Textiles in the Islamic Golden Age")