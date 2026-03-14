import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="Descargador & Recortador Profesional", page_icon="✂️")

# Estilos limpios y modernos
st.markdown("""
    <style>
    .stButton>button {
        width: 100%; border-radius: 10px; height: 3em;
        background-color: #4A90E2; color: white; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("✂️ Descargador y Recortador de Video")
st.write("Analiza el video y descarga solo la parte que necesites.")

url = st.text_input("Pega el enlace del video (YouTube, TikTok, etc.):", placeholder="https://...")

if url:
    try:
        # --- SECCIÓN DE ANÁLISIS ---
        with st.spinner("Analizando video..."):
            ydl_opts_info = {'quiet': True, 'no_warnings': True}
            with yt_dlp.YoutubeDL(ydl_opts_info) as ydl:
                info = ydl.extract_info(url, download=False)
                duration = info.get('duration', 0)
                title = info.get('title', 'Video sin título')
                thumbnail = info.get('thumbnail')

        # Mostrar información del video
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(thumbnail, use_container_width=True)
        with col2:
            st.subheader(title)
            st.info(f"Duración total: {duration} segundos")

        st.divider()

        # --- SECCIÓN DE RECORTE ---
        st.subheader("Configura tu recorte")
        start_time = st.number_input("Segundo de inicio:", min_value=0, max_value=int(duration), value=0)
        end_time = st.number_input("Segundo de fin:", min_value=1, max_value=int(duration), value=int(duration))

        if start_time >= end_time:
            st.error("El tiempo de inicio debe ser menor al de fin.")
        else:
            if st.button("PROCESAR Y DESCARGAR"):
                output_filename = "video_recortado.mp4"
                
                # Configuración para descargar solo el fragmento
                ydl_opts = {
                    'format': 'best[ext=mp4]',
                    'outtmpl': output_filename,
                    'quiet':




