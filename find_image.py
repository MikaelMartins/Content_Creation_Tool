import requests

# Coloque sua chave da API do Unsplash aqui
UNSPLASH_ACCESS_KEY = 'SUA_CHAVE_AQUI'

def buscar_e_salvar_imagem(texto):
    url = "https://api.unsplash.com/search/photos"
    params = {
        "query": texto,
        "per_page": 1,
        "client_id": UNSPLASH_ACCESS_KEY
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        dados = response.json()
        if dados["results"]:
            imagem_url = dados["results"][0]["urls"]["regular"]
            nome_arquivo = texto.replace(" ", "_") + ".jpg"

            img_data = requests.get(imagem_url).content
            with open(nome_arquivo, 'wb') as handler:
                handler.write(img_data)

            print(f"Imagem salva como '{nome_arquivo}' na raiz do projeto.")
        else:
            print("Nenhuma imagem encontrada para o texto fornecido.")
    else:
        print("Erro na consulta da API:", response.status_code)

if __name__ == "__main__":
    texto = input("Digite um texto para buscar uma imagem: ")
    buscar_e_salvar_imagem(texto)
