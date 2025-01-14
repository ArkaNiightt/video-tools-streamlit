import streamlit as st
import yt_dlp
import os
import uuid
import logging

# Configuração do logger
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Diretório padrão para salvar os downloads
download_folder = "downloads"


# Função para baixar vídeos ou áudios
def download_video(url, format_type, quality=None, cookies_path="cookies.txt"):
    logger.info(f"Iniciando download para URL: {url}")

    if not os.path.exists(download_folder):
        os.makedirs(download_folder)
        logger.info(f"Criado diretório de download: {download_folder}")

    ydl_opts = {
        "format": (
            "bestaudio/best"
            if format_type == "mp3"
            else (
                f"bestvideo[height<={quality}]+bestaudio/best"
                if quality
                else "bestvideo+bestaudio"
            )
        ),
        "postprocessors": (
            [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ]
            if format_type == "mp3"
            else []
        ),
        "outtmpl": os.path.join(
            download_folder, f"%(title).15s_{uuid.uuid4().hex[:4]}.%(ext)s"
        ),
        "cookiefile": cookies_path if os.path.exists(cookies_path) else None,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            logger.info("Iniciando extração de informações e download.")
            info_dict = ydl.extract_info(url, download=True)
            # Verifica o arquivo mais recente na pasta de download
            latest_file = max(
                [os.path.join(download_folder, f)
                 for f in os.listdir(download_folder)],
                key=os.path.getctime,
            )
            logger.info(f"Arquivo baixado detectado: {latest_file}")
            return latest_file
    except yt_dlp.utils.DownloadError as e:
        logger.error(f"Erro de download: {e}")
        st.error(f"Erro ao baixar o arquivo: {str(e)}")
    except Exception as e:
        logger.error(f"Erro inesperado: {e}")
        st.error(f"Ocorreu um erro inesperado: {str(e)}")

    logger.info("Download falhou para esta URL.")
    return None


# Função principal para baixar múltiplas URLs
def main():
    st.title("Download em Massa de Vídeos (MP3/MP4)")

    urls_text = st.text_area("Digite as URLs dos vídeos (uma por linha)")
    format_type = st.selectbox("Escolha o formato de download", ("mp3", "mp4"))
    quality = (
        st.selectbox("Escolha a qualidade do vídeo",
                     ("360", "480", "720", "1080"))
        if format_type == "mp4"
        else None
    )

    if st.button("Baixar Todos"):
        if urls_text:
            urls = [url.strip()
                    for url in urls_text.splitlines() if url.strip()]
            total_videos = len(urls)
            logger.info(f"Total de vídeos para download: {total_videos}")
            st.info(f"Total de vídeos inseridos: {total_videos}")

            download_paths = []
            failed_downloads = []

            with st.spinner("Baixando vídeos..."):
                for url in urls:
                    file_path = download_video(url, format_type, quality)
                    if file_path and os.path.exists(file_path):
                        download_paths.append(file_path)
                        logger.info(f"Download concluído para URL: {url}")
                    else:
                        failed_downloads.append(url)
                        logger.warning(f"Download falhou para URL: {url}")

            if download_paths:
                st.success("Download dos vídeos concluído!")
                logger.info(
                    "Todos os downloads bem-sucedidos foram concluídos.")
                if failed_downloads:
                    st.warning(
                        f"Alguns vídeos não foram baixados. Total de falhas: {
                            len(failed_downloads)}"
                    )
                    st.write("Vídeos que falharam no download:")
                    for failed_url in failed_downloads:
                        st.write(failed_url)
                        logger.warning(f"URL que falhou: {failed_url}")

                for path in download_paths:
                    file_name = os.path.basename(path)
                    with open(path, "rb") as file:
                        file_data = file.read()
                        st.download_button(
                            label=f"Baixar {file_name}",
                            data=file_data,
                            file_name=file_name,
                            mime="audio/mpeg" if format_type == "mp3" else "video/mp4",
                        )
            else:
                st.error(
                    "Não foi possível baixar os vídeos. Verifique as URLs e tente novamente."
                )
                logger.error("Nenhum download foi bem-sucedido.")
        else:
            st.warning("Por favor, insira pelo menos uma URL válida.")
            logger.warning("Nenhuma URL inserida.")


if __name__ == "__main__":
    main()
