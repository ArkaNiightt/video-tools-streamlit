# Ferramentas de Vídeo - Streamlit App

Este é um aplicativo em Python desenvolvido com Streamlit que oferece ferramentas essenciais para lidar com vídeos: transcrição de vídeos do YouTube, download de vídeos, e download em massa de vídeos em diferentes formatos (MP3/MP4). Com uma interface intuitiva e uma barra lateral para navegação fácil, ele torna o processamento de vídeos mais acessível e rápido.

## 🌟 Funcionalidades Principais

### 📜 Transcrição de Vídeos do YouTube

Com esta ferramenta, você pode transcrever qualquer vídeo do YouTube de maneira rápida e prática. Basta inserir o link do vídeo, e o aplicativo gera a transcrição automaticamente. Ótimo para capturar o conteúdo de palestras, entrevistas e outros vídeos educativos.

### 📥 Download de Vídeos

Esta ferramenta permite o download de vídeos de diversas plataformas. Você só precisa inserir o link, e o vídeo é baixado diretamente, facilitando o acesso ao conteúdo offline.

### 🚀 Download em Massa de Vídeos (MP3/MP4)

Esta ferramenta permite que você baixe múltiplos vídeos de uma só vez, em formatos de vídeo (MP4) ou áudio (MP3). Basta inserir uma lista de URLs e selecionar o formato desejado, facilitando o download em grande escala. É ideal para baixar conteúdos para uso offline em diferentes qualidades e formatos.

## 🚀 Como Usar

1. **Clone o repositório para sua máquina local**:

   ```bash
   git clone https://github.com/ArkaNiightt/video-tools-streamlit.git
   ```

2. **Instale as dependências necessárias** (Streamlit, pytube, youtube-transcript-api, yt-dlp, etc.):

   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o aplicativo Streamlit**:

   ```bash
   streamlit run app.py
   ```

4. **Navegue pela barra lateral e selecione a ferramenta desejada**:
   - **Transcrição de Vídeos do YouTube**: Insira a URL do vídeo do YouTube para obter a transcrição.
   - **Download de Vídeos**: Insira a URL do vídeo para baixá-lo.
   - **Download em Massa de Vídeos**: Insira múltiplas URLs para baixar vídeos em formato MP3 ou MP4.

## 🚒 Requisitos

- Python 3.7 ou superior
- Streamlit
- pytube
- youtube-transcript-api
- yt-dlp

## 📂 Estrutura do Código

- **transcricao\_video\_youtube()**: Função para realizar a transcrição dos vídeos do YouTube.
- **download\_video()**: Função para realizar o download dos vídeos, agora incluindo suporte a diferentes formatos e qualidades.
- **main()**: Função principal que configura o layout e gerencia a navegação entre as ferramentas.
- **download\_em\_massa()**: Função que permite o download de múltiplas URLs de vídeos de uma só vez.

## 📊 Melhorias Futuras

- Suporte para transcrição em diferentes idiomas.
- Melhorias na interface para torná-la mais atrativa, com mais estilos e elementos gráficos.
- Implementar autenticação para garantir segurança e controle de acesso.
- Suporte aprimorado para download de áudio apenas, com diferentes bitrates.
- Integração com APIs de tradução para oferecer transcrições em outros idiomas.
- Opção de organizar os downloads por pasta ou título do vídeo.

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request. Queremos tornar este projeto cada vez mais útil e acessível.

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

