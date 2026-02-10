import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Descargador Familiar", page_icon="📥")

# Diseño especial para celulares
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #FF0000;
        color: white;
        font-weight: bold;
    }
    input {
        border-radius: 10px !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📥 Descargador Pro")
st.write("Copia el link de YouTube, TikTok o IG y pégalo abajo.")

url = st.text_input("Enlace del video:", placeholder="Pega aquí...")

if st.button("PREPARAR DESCARGA"):
    if url:
        with st.spinner("Cocinando el video..."):
            # Configuramos para descargar en el servidor temporalmente
            ydl_opts = {
                'format': 'best',
                'outtmpl': 'video_descargado.%(ext)s',
                'nocheckcertificate': True,
            }
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    filename = ydl.prepare_filename(info)
                
                # Botón de descarga real para el iPhone
                with open(filename, "rb") as file:
                    st.download_button(
                        label="⬇️ TOCAR AQUÍ PARA GUARDAR",
                        data=file,
                        file_name=filename,
                        mime="video/mp4"
                    )
                os.remove(filename) # Limpieza
            except Exception as e:
                st.error("Hubo un error con el link. Intenta con otro.")
    else:
        st.warning("Primero pega un link.")