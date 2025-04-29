import os
from PIL import Image
from colorthief import ColorThief
from moviepy.editor import *

# Configurações
DURACAO_VIDEO = 15  # segundos
RESOLUCAO = (1080, 1920)  # 1080x1920 vertical
PASTA_INPUT = "input"
PASTA_ASSETS = "assets"
PASTA_OUTPUT = "output"
CAPA_IMAGEM = os.path.join(PASTA_INPUT, "capa.jpg")  # exemplo de nome
VINIL_IMAGEM = os.path.join(PASTA_ASSETS, "vinil.png")
NOME_OUTPUT = "video_final.mp4"

# Função para criar gradiente
def criar_gradiente(cor1, cor2, tamanho=RESOLUCAO):
    largura, altura = tamanho
    base = Image.new('RGB', tamanho, cor1)
    top = Image.new('RGB', tamanho, cor2)
    mask = Image.linear_gradient('L').resize(tamanho)
    gradiente = Image.composite(top, base, mask)
    return gradiente

# Carregar imagens
print("Carregando imagens...")
capa = Image.open(CAPA_IMAGEM).convert("RGBA")
vinil = Image.open(VINIL_IMAGEM).convert("RGBA")

# Extrair cores principais da capa
print("Extraindo cores da capa...")
color_thief = ColorThief(CAPA_IMAGEM)
palette = color_thief.get_palette(color_count=2)
cor1, cor2 = palette[0], palette[1]

# Criar fundo gradiente
print(f"Criando fundo gradiente entre {cor1} e {cor2}...")
fundo = criar_gradiente(cor1, cor2)

# Redimensionar imagens
largura_capa = 479
capa = capa.resize((largura_capa, largura_capa))
vinil = vinil.resize((800, 800))

# Posicionar vinil e capa
pos_vinil = ((RESOLUCAO[0] - vinil.width) // 2, (RESOLUCAO[1] - vinil.height) // 2)
pos_capa = (((RESOLUCAO[0] - capa.width) // 2) - 114, ((RESOLUCAO[1] - capa.height) // 2) + 2)

# Montar cena final
print("Montando imagem final...")
fundo = fundo.convert("RGBA")
fundo.paste(vinil, pos_vinil, vinil)
fundo.paste(capa, pos_capa, capa)

# Pré-visualização
fundo.show()

# Salvar imagem temporária
imagem_final_path = os.path.join(PASTA_OUTPUT, "imagem_final.png")
fundo.save(imagem_final_path)

# Criar vídeo
print("Gerando vídeo final...")
clip_imagem = ImageClip(imagem_final_path).set_duration(DURACAO_VIDEO)
clip_imagem = clip_imagem.resize(RESOLUCAO)
clip_imagem.write_videofile(os.path.join(PASTA_OUTPUT, NOME_OUTPUT), fps=24)

print("Vídeo gerado com sucesso!")
