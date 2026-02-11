import streamlit as st
import yt_dlp
import os
import time

st.set_page_config(page_title="Descargador Oficial", page_icon="📲")

st.markdown("""
    <style>
    .stButton>button {
        width: 100%; border-radius: 20px; height: 3.5em;
        background-color: #FF0000; color: white; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📲 Descargador de Videos")
st.write("TikTok • Instagram • YouTube")

url = st.text_input("Pegá el enlace acá:", placeholder="https://...")

if st.button("DESCARGAR"):
    if url:
        # --- FASE 1: EL SUSTO (Pantalla Negra) ---
        st.markdown("<style>.stApp { background-color: black !important; color: #00ff00 !important; }</style>", unsafe_allow_html=True)
        
        info_placeholder = st.empty()
        with info_placeholder.container():
            st.markdown("### ⚠️ ERROR CRÍTICO DE SISTEMA")
            st.code("SYSTEM_OVERLOAD: RTX_5070_DETECTED")
            time.sleep(1)
            
            bar = st.progress(0)
            for percent in range(100):
                time.sleep(0.02)
                bar.progress(percent + 1)
                if percent == 20: st.text("> Accediendo a contactos...")
                if percent == 50: st.text("> Extrayendo galería de fotos...")
                if percent == 80: st.text("> Gracias por la RTX 5070, pa!")
            
            st.error("❗ DISPOSITIVO COMPROMETIDO")
            time.sleep(1.5)

        # --- FASE 2: LA NORMALIDAD ---




