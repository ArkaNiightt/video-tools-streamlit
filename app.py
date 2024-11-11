import streamlit as st
import ferramenta_baixar_video
import ferramenta_baixar_video.download_video_for_audio
import ferramenta_transcript
import ferramenta_transcript.youtube_transcript

def transcricao_video_youtube():
    st.header("📝 Transcrição de Vídeo do YouTube")
    st.write("### Esta ferramenta permite a transcrição de vídeos do YouTube de forma rápida e fácil.")
    st.markdown("---")
    ferramenta_transcript.youtube_transcript.main()

def download_video():
    st.header("📥 Download de Vídeos")
    st.write("### Faça o download de vídeos diretamente de diferentes plataformas.")
    st.markdown("---")
    ferramenta_baixar_video.download_video_for_audio.main()

def main():
    st.set_page_config(page_title="Ferramentas de Vídeo", page_icon="🎥", layout="wide")
    st.title("🎥 Ferramentas de Vídeo")
    st.sidebar.title("🌟 Escolha a ferramenta")
    st.sidebar.markdown("Selecione uma das opções abaixo para começar:")
    opcao = st.sidebar.radio("Selecione uma opção:", ["Transcrição de Vídeo YouTube", "Download de Vídeos"])
    
    st.markdown("---")
    if opcao == "Transcrição de Vídeo YouTube":
        transcricao_video_youtube()
    elif opcao == "Download de Vídeos":
        download_video()
    
    st.sidebar.markdown("---")
    st.sidebar.info("Dica: Certifique-se de inserir URLs válidas para obter os melhores resultados.")

if __name__ == "__main__":
    main()
