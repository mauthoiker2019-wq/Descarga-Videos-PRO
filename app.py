import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Descargador Familiar", page_icon="📥")

st.markdown("""
    <style>
    .stButton > button {
        width: 100%;
        border-radius: 20px;
        height: 3.5em;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📥 Descargador Pro")
st.write("YouTube • TikTok • Instagram")

formato = st.radio("¿Qué quieres descargar?", ["Video (MP4)", "Música (MP3)"], horizontal=True)
url = st.text_input("Pega el enlace aquí:", placeholder="https://...")

if st.button("PREPARAR DESCARGA"):
    if url:
        # Limpieza básica de URL para evitar rastreadores
        url_clean = url.split('?')[0] if 'tiktok' in url else url
        
        with st.spinner("Descargando... un momento"):
            ydl_opts = {
                'nocheckcertificate': True,
                'quiet': True,
                'no_warnings': True,
                'outtmpl': 'archivo_descargado.%(ext)s',
                # Simulamos un iPhone real para TikTok
                'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
                'add_header': [
                    'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language: es-es',
                ],
            }

            if formato == "Video (MP4)":
                # Forzamos formato compatible con Galería de iPhone
                ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
            else:
                ydl_opts['format'] = 'bestaudio/best'
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]

            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    # Forzamos la descarga directa
                    ydl.download([url_clean])
                    
                    # Buscamos el archivo generado
                    filename = "archivo_descargado.mp4" if formato == "Video (MP4)" else "archivo_descargado.mp3"
                    
                    if os.path.exists(filename):
                        with open(filename, "rb") as file:
                            st.download_button(
                                label="⬇️ TOCAR AQUÍ PARA GUARDAR",
                                data=file,
                                file_name=f"descarga_{'video' if formato == 'Video (MP4)' else 'audio'}.{filename.split('.')[-1]}",
                                mime="video/mp4" if formato == "Video (MP4)" else "audio/mpeg"
                            )
                        os.remove(filename)
                    else:
                        st.error("El servidor procesó el video pero no pudo crear el archivo. Intenta de nuevo.")
            except Exception as e:
                st.error("TikTok bloqueó el acceso. Intenta copiar el link de nuevo o usa otro video para probar.")
    else:
        st.warning("Pega un link primero.")

