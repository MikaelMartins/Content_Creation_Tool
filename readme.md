# 🛠️ Ferramentas Python para Criação de Conteúdo

Este repositório reúne uma coleção de scripts Python pensados para auxiliar a criação de conteúdo digital. As ferramentas permitem automatizar partes do processo criativo, como:

- 🖼️ Busca de imagens temáticas via API do Unsplash
- 🔊 Conversão de texto em narração com gTTS
- 🎬 Geração de vídeos verticais prontos para redes sociais (Reels, Shorts, etc.)

---

## 📁 Estrutura dos Scripts

├── `input/` # Imagens de entrada (ex: capa.jpg)  
├── `assets/` # Elementos gráficos (ex: vinil.png)  
├── `output/` # Conteúdos finais gerados  
├── `find_image.py` # Busca uma imagem no Unsplash a partir de texto  
├── `text_to_speech.py` # Converte um texto em voz (voz.mp3)  
├── `generate_video_disc.py` # Gera um vídeo vertical com imagem e vinil

---

## 🧰 Requisitos

Instale as dependências com:

```bash
pip install requests gtts moviepy Pillow colorthief
```

---

## 🔑 Configuração da API Unsplash

Abra o arquivo `find_image.py` e adicione sua chave de API no campo:

```python
UNSPLASH_ACCESS_KEY = 'SUA_CHAVE_AQUI'
```
Você pode criar sua chave gratuita em: [Unsplash Developers](https://unsplash.com/developers)

---

## 🚀 Como Usar as Ferramentas

### 1. Buscar Imagem Temática
```bash
python3 find_image.py
```
Digite um tema ou frase, e uma imagem será baixada automaticamente.

### 2. Gerar Narração a partir de Texto
```bash
python3 text_to_speech.py
```
Digite o texto desejado, e o áudio será salvo como `voz.mp3`.

### 3. Montar Vídeo Vertical com Design Pronto

Coloque a imagem de capa em `input/capa.jpg` e o vinil em `assets/vinil.png`, depois execute:

```bash
python generate_video_disc.py
```
O vídeo final será salvo em `output/video_final.mp4`.

---

## 📲 Aplicações
- Post para o TikTok
- Shorts do YouTube
- Vídeos de citações, resumos, música ou reflexões
- Conteúdos automatizados com estética consistente

---

## 📄 Licença
MIT License
