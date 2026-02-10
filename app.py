import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Descargador Pro", page_icon="📲")

# Estilo para botones grandes en el celular
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3.5em;
        background-color: #FF0000;
        color: white;
        font-weight: bold;
        font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📲 Descargador de Videos")
st.write("Pegá el link de YouTube, TikTok o Instagram abajo.")

url = st.text_input("Enlace del video:", placeholder="https://...")

if st.button("DESCARGAR"):
    if url:
        with st.spinner("Descargando... un momento"):
            # Opciones de descarga directa (formato MP4 único para evitar errores)
            ydl_opts = {
                'format': 'best[ext=mp4]/best', 
                'outtmpl': 'video_final.mp4',
                'nocheckcertificate': True,
                'quiet': True
            }

            try:
                # Limpiar descargas anteriores si existen
                if os.path.exists("video_final.mp4"):
                    os.remove("video_final.mp4")

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                
                if os.path.exists("video_final.mp4"):
                    with open("video_final.mp4", "rb") as file:
                        st.download_button(
                            label="⬇️ TOCAR PARA GUARDAR",
                            data=file,
                            file_name="video.mp4",
                            mime="video/mp4"
                        )
                else:
                    st.error("No se pudo crear el archivo. Intentá de nuevo.")
            
            except Exception as e:
                st.error("El servidor está saturado o el link es incorrecto.")
    else:
        st.warning("Falta el link.")



