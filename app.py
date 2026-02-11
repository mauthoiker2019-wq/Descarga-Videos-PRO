import streamlit as st
import time
import random

st.set_page_config(page_title="Descargador Oficial", page_icon="📲")

# Estilo para que la página parezca normal... hasta que deja de serlo
st.markdown("""
    <style>
    .stApp { transition: background-color 0.1s; }
    .stButton>button {
        width: 100%; border-radius: 20px; height: 3.5em;
        background-color: #FF0000; color: white; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📲 Descargador de Videos")
st.write("Versión estable para iPhone")

url = st.text_input("Pegá el enlace acá:")

if st.button("DESCARGAR"):
    if url:
        # --- EMPIEZA EL TROLEO ---
        # 1. Pantalla negra de golpe
        st.markdown("<style>.stApp { background-color: black !important; color: #00ff00 !important; }</style>", unsafe_allow_html=True)
        
        placeholder = st.empty()
        with placeholder.container():
            st.markdown("### ⚠️ ERROR DE NÚCLEO DETECTADO")
            st.code("0x000045: SYSTEM_FAILURE\nIniciando volcado de memoria...")
            time.sleep(1.2)
            
            # 2. Mensajes que dan miedo
            mensajes_fake = [
                "Buscando archivos privados...",
                "Enviando fotos de la galería a servidor desconocido...",
                "Sobrecargando procesador Ryzen (Broma)...",
                "BORRANDO SISTEMA OPERATIVO: 15%...",
                "BORRANDO SISTEMA OPERATIVO: 48%...",
                "BORRANDO SISTEMA OPERATIVO: 99%..."
            ]
            
            for msg in mensajes_fake:
                st.text(f"> {msg}")
                time.sleep(0.6)
            
            st.error("❗ FALLO TOTAL: El dispositivo se apagará en 3 segundos.")
            time.sleep(2)

        # 3. VOLVEMOS A LA NORMALIDAD
        st.markdown("<style>.stApp { background-color: white !important; color: black !important; }</style>", unsafe_allow_html=True)
        placeholder.empty()
        
        st.balloons() # Tira globos para que sepan que es joda
        st.success("¡Caíste! Jajaja. Acá tenés tu descarga:")
        
        # --- ACÁ VA TU CÓDIGO REAL DE YT-DLP ---
        # (El mismo que veníamos usando para que el video baje de verdad)
        st.write("*(Simulando descarga real...)*")
    else:
        st.warning("Falta el link, pá.")





