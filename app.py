import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Descargador Familiar", page_icon="📥")

# Estilo visual
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3.5em;
        background-color: #FF0000;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📥 Descargador Pro")
st.write("Funciona con: YouTube, TikTok e Instagram")

formato = st.radio("¿Qué querés descargar?", ["Video (MP4)", "Música (MP3)"], horizontal=True)
url = st.text_input("Pegá el enlace aquí:", placeholder="https://...")

if st.button("PREPARAR DESCARGA"):
    if url:
        with st.spinner("Buscando el video..."):
            # OPCIONES MEJORADAS PARA REDES SOCIALES
            ydl_opts = {
                'nocheckcertificate': True,
                'quiet': True,
                'no_warnings': True,
                'outtmpl': 'archivo_%(title)s.%(ext)s',
                'referer': 'https://www.google.com/', # Engaña a TikTok/IG para que no bloqueen
            }

            if formato == "Video (MP4)":
                # 'best' es más seguro para iPhone
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
                    info = ydl.extract_info(url, download=True)
                    filename = ydl.prepare_filename(info)
                    
                    # Corrección de extensión para MP3
                    if formato == "Música (MP3)" and not filename.endswith('.mp3'):
                        filename = os.path.splitext(filename)[0] + '.mp3'

                with open(filename, "rb") as file:
                    st.download_button(
                        label="⬇️ TOCAR AQUÍ PARA GUARDAR",
                        data=file,
                        file_name=os.path.basename(filename),
                        mime="video/mp4" if formato == "Video (MP4)" else "audio/mpeg"
                    )
            except Exception as e:
                st.error("No se pudo bajar. A veces Instagram bloquea el acceso si el video es privado.")
    else:
        st.warning("Primero poné el link.")

