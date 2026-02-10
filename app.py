import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Descargador Familiar", page_icon="📥")

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
st.write("YouTube • TikTok • Instagram")

formato = st.radio("¿Qué querés descargar?", ["Video (MP4)", "Música (MP3)"], horizontal=True)
url = st.text_input("Pegá el enlace aquí:", placeholder="https://...")

if st.button("PREPARAR DESCARGA"):
    if url:
        with st.spinner("Descargando... un momento"):
            # Opciones optimizadas para evitar bloqueos de TikTok
            ydl_opts = {
                'nocheckcertificate': True,
                'quiet': True,
                'no_warnings': True,
                'outtmpl': 'archivo_descargado.%(ext)s',
                # Estas líneas son para que TikTok crea que somos un navegador real
                'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'referer': 'https://www.tiktok.com/',
            }

            if formato == "Video (MP4)":
                ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'
            else:
                # Bajamos el mejor audio disponible
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
                    
                    # Forzar extensión .mp3 si es música
                    if formato == "Música (MP3)":
                        base, ext = os.path.splitext(filename)
                        new_filename = base + ".mp3"
                        # yt-dlp a veces ya lo renombró solo
                        if os.path.exists(new_filename):
                            filename = new_filename
                        elif os.path.exists(filename):
                            os.rename(filename, new_filename)
                            filename = new_filename

                with open(filename, "rb") as file:
                    st.download_button(
                        label="⬇️ TOCAR AQUÍ PARA GUARDAR",
                        data=file,
                        file_name=os.path.basename(filename),
                        mime="video/mp4" if formato == "Video (MP4)" else "audio/mpeg"
                    )
                
                # Borramos para no llenar el servidor de Streamlit
                os.remove(filename)

            except Exception as e:
                st.error("Error técnico. Probá copiar el link de nuevo desde la app de TikTok.")
    else:
        st.warning("Copiá un link primero.")
