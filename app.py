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
        st.markdown("<style>.stApp { background-color: white !important; color: black !important; }</style>", unsafe_allow_html=True)
        info_placeholder.empty()
        st.balloons()
        st.success("¡Es joda! Preparando tu descarga...")

        # --- FASE 3: MOTOR DE DESCARGA MULTI-PLATAFORMA ---
        with st.spinner("Procesando link..."):
            ydl_opts = {
                # Forzamos MP4 para iPhone
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': 'video_final.mp4',
                'nocheckcertificate': True,
                'quiet': True,
                # Headers para que TikTok/IG no nos bloqueen
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'referer': 'https://www.google.com/',
            }

            try:
                if os.path.exists("video_final.mp4"):
                    os.remove("video_final.mp4")

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                if os.path.exists("video_final.mp4"):
                    with open("video_final.mp4", "rb") as file:
                        st.download_button(
                            label="⬇️ TOCAR AQUÍ PARA GUARDAR",
                            data=file,
                            file_name="video.mp4",
                            mime="video/mp4"
                        )
                else:
                    st.error("El video no se encontró. Probá copiar el link de nuevo.")
            except Exception as e:
                st.error("Error: El servidor de la red social bloqueó la conexión.")
    else:
        st.warning("Falta el link, che.")




