import streamlit as st
import yt_dlp
import os
import time

st.set_page_config(page_title="Descargador Oficial", page_icon="📲")

# Estilos iniciales
st.markdown("""
    <style>
    .stButton>button {
        width: 100%; border-radius: 20px; height: 3.5em;
        background-color: #FF0000; color: white; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📲 Descargador de Videos")
st.write("Versión estable para iPhone")

url = st.text_input("Pegá el enlace acá:", placeholder="https://...")

if st.button("DESCARGAR"):
    if url:
        # --- FASE 1: EL SUSTO ---
        st.markdown("<style>.stApp { background-color: black !important; color: #00ff00 !important; }</style>", unsafe_allow_html=True)
        
        info_placeholder = st.empty()
        with info_placeholder.container():
            st.markdown("### ⚠️ ERROR CRÍTICO DE SISTEMA")
            st.code("0x000045: MEMORY_DUMP_INITIATED")
            time.sleep(1)
            
            # El contador que queríamos
            bar = st.progress(0)
            for percent in range(100):
                time.sleep(0.02)
                bar.progress(percent + 1)
                if percent == 30: st.text("> Accediendo a archivos privados...")
                if percent == 60: st.text("> Enviando datos a servidor remoto...")
                if percent == 90: st.text("> Borrando rastros del sistema...")
            
            st.error("❗ FALLO TOTAL: REINICIANDO INTERFAZ...")
            time.sleep(1.5)

        # --- FASE 2: LA NORMALIDAD ---
        st.markdown("<style>.stApp { background-color: white !important; color: black !important; }</style>", unsafe_allow_html=True)
        info_placeholder.empty()
        st.balloons()
        st.success("¡Es broma! Tu video se está procesando ahora mismo:")

        # --- FASE 3: DESCARGA REAL ---
        with st.spinner("Preparando archivo..."):
            ydl_opts = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': 'video_papas.mp4',
                'nocheckcertificate': True,
                'quiet': True
            }

            try:
                # Limpiar si quedó algo
                if os.path.exists("video_papas.mp4"):
                    os.remove("video_papas.mp4")

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                if os.path.exists("video_papas.mp4"):
                    with open("video_papas.mp4", "rb") as file:
                        st.download_button(
                            label="⬇️ TOCAR AQUÍ PARA GUARDAR VIDEO",
                            data=file,
                            file_name="video_descargado.mp4",
                            mime="video/mp4"
                        )
                    # No borramos el archivo acá para que el botón de arriba funcione
                else:
                    st.error("El servidor falló. Intentá de nuevo.")
            except Exception as e:
                st.error("Hubo un problema con el link. Fijate si es correcto.")
    else:
        st.warning("Poné un link primero, che.")




