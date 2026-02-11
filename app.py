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
    .stApp { transition: background-color 0.5s; }
    </style>
    """, unsafe_allow_html=True)

st.title("📲 Descargador de Videos")
st.write("Versión 2026 - Anti Bloqueo")

url = st.text_input("Pegá el enlace acá:", placeholder="https://...")

if st.button("DESCARGAR"):
    if url:
        # --- EL SUSTO (No se toca, es sagrado) ---
        st.markdown("<style>.stApp { background-color: black !important; color: #00ff00 !important; }</style>", unsafe_allow_html=True)
        info_placeholder = st.empty()
        with info_placeholder.container():
            st.markdown("### ⚠️ ALERTA: INTRUSIÓN EN RTX 5070")
            bar = st.progress(0)
            for percent in range(100):
                time.sleep(0.02)
                bar.progress(percent + 1)
            st.error("❗ DISPOSITIVO CONTROLADO POR TU HIJO")
            time.sleep(1.5)

        st.markdown("<style>.stApp { background-color: white !important; color: black !important; }</style>", unsafe_allow_html=True)
        info_placeholder.empty()
        st.balloons()

        # --- INTENTO DE DESCARGA REAL ---
        with st.spinner("Intentando bypass..."):
            ydl_opts = {
                'format': 'best[ext=mp4]',
                'outtmpl': 'video.mp4',
                'quiet': True,
                'no_warnings': True,
            }

            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                with open("video.mp4", "rb") as file:
                    st.download_button("⬇️ GUARDAR VIDEO", file, "video.mp4")
            
            except Exception:
                # --- PLAN B: SI TIKTOK BLOQUEA, MANDAMOS AL MOTOR PESADO ---
                st.warning("⚠️ El servidor principal está saturado por seguridad.")
                st.write("Tocá el botón de abajo para usar el **Servidor de Respaldo**:")
                
                # Creamos un link a Cobalt.tools que ya tiene el link pegado
                # Esto es infalible porque Cobalt no lo bloquean
                link_respaldo = f"https://cobalt.tools/?u={url}"
                
                st.markdown(f"""
                    <a href="{link_respaldo}" target="_blank">
                        <button style="width:100%; border-radius:20px; height:3.5em; background-color:#4CAF50; color:white; border:none; font-weight:bold; cursor:pointer;">
                            🚀 USAR SERVIDOR DE RESPALDO
                        </button>
                    </a>
                """, unsafe_allow_html=True)
                st.info("Al entrar, dale al botón de la flecha y listo.")
    else:
        st.warning("Falta el link.")





