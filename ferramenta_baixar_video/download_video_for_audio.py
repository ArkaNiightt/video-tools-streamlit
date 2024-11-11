import streamlit as st
import yt_dlp
import os


def main():
    # Função para baixar áudio do YouTube
    def download_youtube_video(youtube_url, format_type, quality=None):
        if format_type == "mp3":
            ydl_opts = {
                "format": "bestaudio/best",
                "postprocessors": [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ],
                "outtmpl": "%(title)s.%(ext)s",
            }
        elif format_type == "mp4":
            if quality:
                ydl_opts = {
                    "format": f"bestvideo[height<={quality}]+bestaudio/best",
                    "outtmpl": "%(title)s.%(ext)s",
                }
            else:
                ydl_opts = {
                    "format": "bestvideo+bestaudio",
                    "outtmpl": "%(title)s.%(ext)s",
                }
        else:
            st.error("Formato inválido")
            return None

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(youtube_url, download=True)
                if format_type == "mp3":
                    file_title = (
                        ydl.prepare_filename(info_dict).rsplit(".", 1)[0] + ".mp3"
                    )
                else:
                    file_title = ydl.prepare_filename(info_dict)

                # Abrir o arquivo gerado e carregar no buffer
                with open(file_title, "rb") as f:
                    file_bytes = f.read()

                # Excluir o arquivo temporário após o uso
                os.remove(file_title)

            return file_bytes
        except yt_dlp.utils.DownloadError as e:
            # Verificando se o erro corresponde ao vídeo não disponível
            if "Video unavailable" in str(e):
                print(
                    f"Erro ao baixar o arquivo: {str(e)}. O vídeo não está disponível."
                )
            else:
                print(f"Erro ao baixar o arquivo: {str(e)}")

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
            with st.status("Baixando dados...", expanded=True) as status:
                file_bytes = download_youtube_video(youtube_url, format_type, quality)
                if file_bytes:
                    if format_type == "mp3":
                        file_name = f"{youtube_url}_audio.mp3"
                        mime_type = "audio/mpeg"
                    else:
                        file_name = f"{youtube_url}_video.mp4"
                        mime_type = "video/mp4"

                    # Tornar o arquivo disponível para download
                    st.download_button(
                        label="Clique aqui para baixar",
                        data=file_bytes,
                        file_name=file_name,
                        mime=mime_type,
                    )
                    status.update(
                        label="Download concluído!", state="complete", expanded=False
                    )
                    st.success("Download concluído!")
        else:
            st.warning("Por favor, insira uma URL válida.")
