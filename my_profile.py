import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --- 1. PAGE SETUP (The "Canvas") ---
st.set_page_config(
    page_title="「わたしについて」", 
    page_icon="🫱🏻‍🫲🏻", 
    layout="wide"
)

# --- 2. SIDEBAR (The Navigation & Quick Info) ---
with st.sidebar:
    # You can replace this URL with a path to your actual photo later!
    st.image("images/sidebar.jpg", caption="University Student")
    st.markdown("### 📧 Contact Me")
    st.write("📍 アレクス－エジプト ")
    st.write("✉️ monarsh626@gmail.com")
    
    st.divider()
    
    st.markdown("### 🗣️ Languages - 言語  ( げんご )")
    st.caption("Arabic (Native) - アラビアご")
    st.caption("English (Fluent) - えいご")
    st.caption("Japanese (Learning 🇯🇵) - 日本語")
    st.caption("Korean (Learning 🇰🇷) - 韓国語")

# --- 3. MAIN HEADER ---
st.title("🧵 [Manar Ahmed Mostafa - マナール]")
st.markdown("##### だいがくせえ")
st.write("A little about me - じこしょうかい")

st.divider()

# --- 4. THE CONTENT TABS ---
# This matches your desire to show different "aspects" of yourself
tab_home, tab_hobbies = st.tabs([
    "🏠 ホムペ", 
    "✨ ゆめ",
])

# === TAB 1: HOME (Jikoshoukai) ===
with tab_home:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("images/myphoto.jpg", caption="私のしゃしん")
        
    with col2:
        st.subheader("はじめまして !")
        st.write("""
        
        なまえはマナールです。エジプトじんです。
        だいがくせいです。さんねんせいです。せんこうはこうがくです。
        しゅみはよむとげんごです。
        かぞくはごにんかぞくです。ははとちちとふたりのおとうとです。

        """)
        
        if st.button("✨ すきなものかんじ"):
            st.success("風　‐ Wind")
            st.balloons()

# === TAB 3: ゆめ ===
with tab_hobbies:
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.write("""
        
      わたしの ゆめは、 にほんへ りょこう すること です。
      さくらが さいているのを みたいです。
      にほんの おかしを たべて みたいです。
      そして、 ふじさんに いきたいです。 そこで たくさん しゃしんを とりたいです。
        """)
        
    with col_b:
        st.header("ゆめのしゃしん")
        # Gallery Placeholder
        st.image("https://images.unsplash.com/photo-1626785774573-4b799314346d", caption="Graphic Design Work")



