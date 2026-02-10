import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Descargador Familiar", page_icon="📥")

# Estilo para que se vea bien en el celular
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3.5em;
        background-color: #FF0000;
        color: white;
        font-weight: bold;
        font-size: 18px;
    }
    .stRadio > div {
        flex-direction: row;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📥 Descargador Pro")
st.write("Elegí si querés Video o Música, pegá el link y listo.")

# Selección de formato
formato = st.radio("¿Qué querés descargar?", ["Video (MP4)", "Música (MP3)"])

url = st.text_input("Pegá el enlace aquí:", placeholder="https://...")

if st.button("PREPARAR DESCARGA"):
    if url:
        with st.spinner("Procesando..."):
            # Opciones de descarga
            ydl_opts = {
                'nocheckcertificate': True,
                'outtmpl': 'archivo_descargado.%(ext)s',
            }

            if formato == "Video (MP4)":
                ydl_opts['format'] = 'best'
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
                    
                    # Si es audio, yt-dlp a veces cambia la extensión a .mp3 después de procesar
                    if formato == "Música (MP3)" and not filename.endswith('.mp3'):
                        base = os.path.splitext(filename)[0]
                        filename = base + '.mp3'

                with open(filename, "rb") as file:
                    st.download_button(
                        label="⬇️ TOCAR AQUÍ PARA GUARDAR",
                        data=file,
                        file_name=filename,
                        mime="video/mp4" if formato == "Video (MP4)" else "audio/mpeg"
                    )
                # No borramos el archivo inmediatamente para que el botón de descarga funcione
            except Exception as e:
                st.error("No se pudo descargar. Revisá que el link sea correcto.")
    else:
        st.warning("Falta el link, che.")
