import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Descargador Familiar", page_icon="📥")

st.title("📥 Descargador Pro")
st.write("Versión Ultra-Compatible (YouTube, TikTok, IG)")

formato = st.radio("¿Qué quieres?", ["Video", "Música"], horizontal=True)
url = st.text_input("Pega el link aquí:")

if st.button("DESCARGAR"):
    if url:
        with st.spinner("Descargando..."):
            # Opciones básicas para que no falle el servidor
            ydl_opts = {
                'nocheckcertificate': True,
                'outtmpl': 'archivo.%(ext)s',
                'quiet': True,
            }

            if formato == "Video":
                # Buscamos un formato mp4 ya combinado para no estresar al servidor
                ydl_opts['format'] = 'best[ext=mp4]/best'
            else:
                ydl_opts['format'] = 'bestaudio/best'
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]

            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    # Obtenemos el nombre real del archivo descargado
                    filename = ydl.prepare_filename(info)
                    
                    # Si pedimos MP3, yt-dlp lo renombra al final
                    if formato == "Música":
                        filename = os.path.splitext(filename)[0] + ".mp3"

                if os.path.exists(filename):
                    with open(filename, "rb") as f:
                        st.download_button(
                            label="⬇️ GUARDAR EN CELULAR",
                            data=f,
                            file_name=os.path.basename(filename),
                            mime="video/mp4" if formato == "Video" else "audio/mpeg"
                        )
                    os.remove(filename)
                else:
                    st.error("El video se procesó pero el archivo no se encontró. Reintenta.")
            except Exception as e:
                st.error(f"Error: El servicio de video está saturado. Intenta de nuevo en un minuto.")
    else:
        st.warning("Pega un link primero.")


