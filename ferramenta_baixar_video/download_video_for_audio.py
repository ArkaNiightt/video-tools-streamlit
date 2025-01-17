import streamlit as st
import yt_dlp
import os
import re
from pathlib import Path
import time

def clean_downloads_folder(folder):
    """Limpa a pasta de downloads após o download ser concluído"""
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            st.error(f"Erro ao limpar arquivo temporário: {e}")

def download_youtube_video(youtube_url, format_type, quality=None):
    download_folder = Path("downloads")
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
    
    # Limpa a pasta antes de iniciar novo download
    clean_downloads_folder(download_folder)

    if format_type == "mp3":
        ydl_opts = {
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "outtmpl": str(download_folder / "%(title)s.%(ext)s"),
            "restrictfilenames": True,
        }
    else:
        ydl_opts = {
            "format": f"bestvideo[height<={quality}]+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": str(download_folder / "%(title)s.%(ext)s"),
            "restrictfilenames": True,
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=True)
            title = info['title']
            # Espera um momento para garantir que o arquivo foi salvo
            time.sleep(1)
            
            # Encontra o arquivo mais recente na pasta
            files = list(download_folder.glob('*'))
            if not files:
                raise FileNotFoundError("Arquivo baixado não encontrado")
            
            newest_file = max(files, key=os.path.getctime)
            
            # Lê o arquivo
            with open(newest_file, 'rb') as f:
                file_bytes = f.read()

            return file_bytes, newest_file.name

    except Exception as e:
        st.error(f"Erro no download: {str(e)}")
        return None, None

def main():
    st.title("Download de Vídeos (MP3/MP4)")
    
    youtube_url = st.text_input("Digite a URL do vídeo")
    format_type = st.selectbox("Escolha o formato de download", ("mp3", "mp4"))
    
    quality = None
    if format_type == "mp4":
        quality = st.selectbox("Escolha a qualidade do vídeo", ("360", "480", "720", "1080"))

    if st.button("Baixar"):
        if youtube_url:
            with st.spinner("Baixando..."):
                file_bytes, file_name = download_youtube_video(youtube_url, format_type, quality)
                if file_bytes and file_name:
                    mime_type = "audio/mpeg" if format_type == "mp3" else "video/mp4"
                    
                    st.download_button(
                        label="Clique aqui para baixar",
                        data=file_bytes,
                        file_name=file_name,
                        mime=mime_type,
                    )
                    st.success("Download concluído!")
        else:
            st.warning("Por favor, insira uma URL válida.")

if __name__ == "__main__":
    main()
