import streamlit as st
import yt_dlp
import os
import re

st.set_page_config(page_title="Descargador Familiar", page_icon="📥")

st.markdown("""
    <style>
    .stButton>button {
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
url_input = st.text_input("Pega el enlace aquí:", placeholder="https://...")

def limpiar_url(url):
    # Elimina basura de los links de TikTok/IG para que yt-dlp no se confunda
    return url.split('?')[0]

if st.button("PREPARAR DESCARGA"):
    if url_input:
        url = limpiar_url(url_input)
        with st.spinner("Procesando... esto puede tardar unos segundos"):
            
            # Opciones ultra-compatibles
            ydl_opts = {
                'nocheckcertificate': True,
                'quiet': True,
                'no_warnings': True,
                'outtmpl': 'archivo_descargado.%(ext)s',
                # Forzamos a que use un formato que iPhone entienda siempre (h264)
                'format': 'best[ext=mp4]/best', 
                'http_headers': {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Referer': 'https://www.google.com/',
                }
            }

            if formato == "Música (MP3)":
                ydl_opts['format'] = 'bestaudio/best'
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]

            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    # Extraer info primero para asegurar que el link responde
                    info = ydl.extract_info(url, download=True)
                    filename = ydl.prepare_filename(info)
                    
                    if formato == "Música (MP3)":
                        filename = os.path.splitext(filename)[0] + ".mp3"

                with open(filename, "rb") as file:
                    st.download_button(
                        label="⬇️ TOCAR AQUÍ PARA GUARDAR",
                        data=file,
                        file_name=os.path.basename(filename),
                        mime="video/mp4" if formato == "Video (MP4)" else "audio/mpeg"
                    )
                os.remove(filename)

            except Exception as e:
                st.error("TikTok/Instagram bloqueó la conexión. Intenta de nuevo en unos segundos.")
    else:
        st.warning("Pega un link primero.")
