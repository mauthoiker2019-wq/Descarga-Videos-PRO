import streamlit as st
import yt_dlp
import os
import time

# Configuración de la página
st.set_page_config(page_title="Descargador Oficial", page_icon="📲")

# Estilos CSS para el troleo y botones
st.markdown("""
    <style>
    .stButton>button {
        width: 100%; border-radius: 20px; height: 3.5em;
        background-color: #FF0000; color: white; font-weight: bold; font-size: 20px;
    }
    .stApp { transition: background-color 0.5s; }
    </style>
    """, unsafe_allow_html=True)

st.title("📲 Descargador de Videos")
st.write("YouTube • TikTok • Instagram")

url = st.text_input("Pegá el enlace acá:", placeholder="https://...")

if st.button("DESCARGAR"):
    if url:
        # --- FASE 1: EL SUSTO (PANTALLA NEGRA) ---
        st.markdown("<style>.stApp { background-color: black !important; color: #00ff00 !important; }</style>", unsafe_allow_html=True)
        
        info_placeholder = st.empty()
        with info_placeholder.container():
            st.markdown("### ⚠️ ALERTA DE SISTEMA CRÍTICA")
            st.code("ERROR: INTRUSIÓN DETECTADA\nIP_DESTINO: 192.168.1.105 (RTX_MASTER)")
            
            bar = st.progress(0)
            for percent in range(100):
                time.sleep(0.03)
                bar.progress(percent + 1)
                if percent == 25: st.text("> Accediendo a archivos locales...")
                if percent == 55: st.text("> Clonando galería de fotos...")
                if percent == 85: st.text("> Gracias por la RTX 5070, pa!")
            
            st.error("❗ DISPOSITIVO ENCRIPTADO CON ÉXITO")
            time.sleep(2)

        # --- FASE 2: VOLVER A LA NORMALIDAD ---
        st.markdown("<style>.stApp { background-color: white !important; color: black !important; }</style>", unsafe_allow_html=True)
        info_placeholder.empty()
        st.balloons()
        st.success("¡Es joda, pá! Ya te estoy bajando el video...")

        # --- FASE 3: MOTOR DE DESCARGA ---
        with st.spinner("Bypasseando bloqueos..."):
            # Opciones optimizadas para no ser bloqueado
            ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': 'video_final.mp4',
                'nocheckcertificate': True,
                'quiet': True,
                'no_warnings': True,
                'user_agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1',
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
                            label="⬇️ TOCAR AQUÍ PARA GUARDAR VIDEO",
                            data=file,
                            file_name="video_descargado.mp4",
                            mime="video/mp4"
                        )
                    st.info("Recordá: Buscá la flechita azul de descargas en Safari para guardarlo en tus fotos.")
                else:
                    st.error("No se pudo generar el archivo. Intentá de nuevo.")
            except Exception as e:
                st.error("TikTok/IG bloqueó la conexión. Intentá borrar la app en Streamlit y crearla de nuevo para cambiar la IP.")
    else:
        st.warning("Falta el link, che.")





