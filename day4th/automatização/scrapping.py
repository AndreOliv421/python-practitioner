    # Biblioteca de Requisição
import requests
    # Responsável por tratar o retorno 
from bs4 import BeautifulSoup

# pip install requests
# pip install bs4

headers = { 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Applewebkit/537.36"
}

url = "https://g1.globo.com/"

# Fazendo Requisição http
resposta = requests.get(url, headers=headers)

# Verifica se deu certo
if resposta.status_code == 200:
    print("requisição feita com sucesso")
    # 200 -> Ok

    soup = BeautifulSoup(resposta.text, "html.parser")

    noticias = soup.find_all("a", class_="feed-post-link")
    
    print("Ultimas noticias:")
    for noticia in noticias:
        print(f'{noticia.text} - {noticia['href']}')
