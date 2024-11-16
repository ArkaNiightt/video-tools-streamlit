import streamlit as st
import ferramenta_baixar_video
import ferramenta_baixar_video.download_all_videos
import ferramenta_baixar_video.download_video_for_audio
import ferramenta_transcript
import ferramenta_transcript.youtube_transcript

# Função para transcrever vídeos do YouTube
def transcricao_video_youtube():
    st.header("📝 Transcrição de Vídeo do YouTube")
    st.write("### Esta ferramenta permite a transcrição de vídeos do YouTube de forma rápida e fácil.")
    st.markdown("---")
    ferramenta_transcript.youtube_transcript.main()

# Função para download de vídeo ou áudio
def download_video():
    st.header("📥 Download de Vídeos")
    st.write("### Faça o download de vídeos diretamente de diferentes plataformas.")
    st.markdown("---")
    ferramenta_baixar_video.download_video_for_audio.main()

# Função para download em massa de vídeos do YouTube
def download_em_massa():
    st.header("📥 Download em Massa de Vídeos")
    st.write("### Faça o download de múltiplos vídeos de uma só vez.")
    st.markdown("---")
    ferramenta_baixar_video.download_all_videos.main()

# Função principal do aplicativo
def main():
    st.set_page_config(page_title="Ferramentas de Vídeo", page_icon="🎥", layout="wide")
    st.title("🎥 Ferramentas de Vídeo")
    st.sidebar.title("🌟 Escolha a ferramenta")
    st.sidebar.markdown("Selecione uma das opções abaixo para começar:")
    opcao = st.sidebar.radio("Selecione uma opção:", ["Transcrição de Vídeo YouTube", "Download de Vídeos", "Download em Massa de Vídeos"])
    
    st.markdown("---")
    if opcao == "Transcrição de Vídeo YouTube":
        transcricao_video_youtube()
    elif opcao == "Download de Vídeos":
        download_video()
    elif opcao == "Download em Massa de Vídeos":
        download_em_massa()
    
    st.sidebar.markdown("---")
    st.sidebar.info("Dica: Certifique-se de inserir URLs válidas para obter os melhores resultados.")

if __name__ == "__main__":
    main()