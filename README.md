# Ferramentas de Vídeo - Streamlit App

Este é um aplicativo em Python desenvolvido com Streamlit que oferece duas ferramentas principais para vídeos: transcrição de vídeos do YouTube e download de vídeos. O aplicativo possui uma interface amigável com uma barra lateral para facilitar a navegação entre as funcionalidades.

## 🎯 Funcionalidades

### 📝 Transcrição de Vídeo do YouTube

Esta ferramenta permite transcrever vídeos do YouTube de forma rápida e fácil. Basta inserir o link do vídeo, e a transcrição será gerada diretamente no aplicativo. Ideal para capturar o conteúdo de palestras, entrevistas e outros vídeos educativos.

### 📥 Download de Vídeos

Com esta ferramenta, é possível baixar vídeos de diferentes plataformas. Você pode inserir o link do vídeo desejado e realizar o download de forma prática, facilitando o acesso offline ao conteúdo.

## 🚀 Como Usar

1. **Clone o repositório para sua máquina local**:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. **Instale as dependências necessárias** (Streamlit, pytube, youtube-transcript-api, etc.):

   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o aplicativo Streamlit**:

   ```bash
   streamlit run main.py
   ```

4. **Navegue até a barra lateral e selecione a ferramenta que deseja usar**:

   - **Transcrição de Vídeo YouTube**: insira a URL do vídeo do YouTube para gerar a transcrição.
   - **Download de Vídeos**: insira a URL do vídeo para baixá-lo.

## 🛠️ Requisitos

- Python 3.7 ou superior
- Streamlit
- pytube
- youtube-transcript-api

## 📂 Estrutura do Código

- **transcricao\_video\_youtube()**: Função responsável por realizar a transcrição dos vídeos do YouTube.
- **download\_video()**: Função que permite o download dos vídeos.
- **main()**: Função principal que configura o layout e a navegação entre as ferramentas.

## 📈 Melhorias Futuras

- Adicionar suporte para transcrição em diferentes idiomas.
- Melhorar a interface com mais estilos e elementos gráficos para uma experiência mais atraente.
- Implementar autenticação para limitar o uso das ferramentas, garantindo segurança e controle de acesso.
- Adicionar suporte para download de apenas áudio dos vídeos.
- Integrar com APIs de tradução para oferecer transcrições em outros idiomas.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request. Queremos tornar este projeto cada vez mais útil e acessível.

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Desenvolvido com ❤️ e Streamlit para facilitar o acesso e o uso de conteúdo em vídeo.