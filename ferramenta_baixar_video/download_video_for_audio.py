import streamlit as st
import yt_dlp
import os
import re
from pathlib import Path


def main():
    # Função para baixar vídeo ou áudio do YouTube
    def download_youtube_video(youtube_url, format_type, quality=None):
        # Pasta para salvar os arquivos baixados
        download_folder = Path("downloads")
        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        # Definindo as opções do yt_dlp dependendo do formato solicitado
        if format_type == "mp3":
            ydl_opts = {
                "format": "bestaudio/best",  # Melhor qualidade de áudio disponível
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",  # Qualidade do áudio
                    }
                ],
                "outtmpl": str(download_folder / "%(title)s.%(ext)s"),  # Modelo do nome do arquivo de saída
                "restrictfilenames": True,  # Sanitize filenames to prevent errors
            }
        elif format_type == "mp4":
                ydl_opts = {
                    "format": f"bestvideo[height<={quality}]+bestaudio/best",  # Melhor vídeo disponível até a qualidade especificada, com melhor áudio
                    "merge_output_format": "mp4",
                    "outtmpl": str(download_folder / "%(title)s.%(ext)s"),
                    "restrictfilenames": True,  # Sanitize filenames to prevent errors
                }
                
                
        else:
            st.error("Formato inválido")
            return None

        try:
            # Usando yt_dlp para baixar o vídeo/áudio
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(youtube_url, download=True)
                # Determinar o nome do arquivo resultante
                title = info_dict.get('title', 'video').replace('/', '_')
                title = re.sub(r'[^\w\-_\. ]', '_', title)  # Ajustar o título para um padrão seguro
                
                # Encontrar o arquivo baixado mais recente na pasta
                files = [f for f in os.listdir(download_folder) if os.path.isfile(os.path.join(download_folder, f))]
                if not files:
                    raise FileNotFoundError("Arquivo baixado não encontrado")
                
                downloaded_file = os.path.join(download_folder, files[-1])

                # Abrir o arquivo gerado e carregar no buffer
                with open(downloaded_file, "rb") as f:
                    file_bytes = f.read()

            return file_bytes, downloaded_file
        except yt_dlp.utils.DownloadError as e:
            # Verificando se o erro corresponde ao vídeo não disponível
            if "Video unavailable" in str(e):
                st.error(f"Erro ao baixar o arquivo: {str(e)}. O vídeo não está disponível.")
            else:
                st.error(f"Erro ao baixar o arquivo: {str(e)}")
        return None, None

    # Título do aplicativo
    st.title("Download de Vídeos (MP3/MP4)")

    # Campo de texto para inserir a URL do vídeo
    youtube_url = st.text_input("Digite a URL do vídeo")

    # Opção para escolher o formato de download
    format_type = st.selectbox("Escolha o formato de download", ("mp3", "mp4"))

    # Se o formato for mp4, permitir escolher a qualidade
    quality = None
    if format_type == "mp4":
        quality = st.selectbox(
            "Escolha a qualidade do vídeo", ("360", "480", "720", "1080")
        )

    # Botão para iniciar o download
    if st.button("Baixar"):
        if youtube_url:
            # Exibindo um spinner enquanto o download está em progresso
            with st.spinner("Baixando dados..."):
                file_bytes, file_title = download_youtube_video(youtube_url, format_type, quality)
                if file_bytes:
                    # Definindo o nome e o tipo do arquivo para download
                    file_name = os.path.basename(file_title)
                    if format_type == "mp3":
                        mime_type = "audio/mpeg"
                    else:
                        mime_type = "video/mp4"

                    # Botão para o usuário baixar o arquivo
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
