from bs4 import BeautifulSoup
import requests
import re
import json

'''
    Função que recebe o corpo de uma páginas do Vagalume com letras músicas e retorna a letra da música na
    sua versão original, sem o título.
'''
def get_lyrics_music(pageHTML):
    soup = BeautifulSoup(pageHTML.encode('iso-8859-1'), "html.parser")
    
    lyricsPair = soup.find("div", id="lyricsPair")
    
    lyricsList = lyricsPair.find_all("div", class_="orig")
    
    letra = ''
    for linha in range(2, len(lyricsList)):
        letra += lyricsList[linha].p.text + "\n"
        
    return letra


'''
    URL e rota para buscar os dados do top 100 de músicas do site Vagalume.
'''
url = 'https://www.vagalume.com.br'
rota = '/top100/musicas/'


'''
    Array usado para armazenar as músicas.
'''
musics = []


'''
    Realizando a requisição ao site do vagalume com o top 100 das músicas.
'''
res = requests.get(url + rota)


'''
    Convertendo a resposta da requisição acima em um objeto BeautifulSoup
'''
soup = BeautifulSoup(res.text.encode('iso-8859-1'), "html.parser")



'''
    Lista com as 100 músicas mais tocadas
'''
ol = soup.find("ol", class_="topCard")


'''
    Pegando as informações das músicas do array
'''
for li in ol.find_all('li', class_="borderless"):
    music = {}
    
    value = li.find('div', class_="cardCenterCol").find('div', class_="topInfo topSongs").div.find("p", class_="styleBlack").text
    pontos = li.find('div', class_="cardCenterCol").find('div', class_="topInfo topSongs").div.find("p", class_="styleBlack").p.text
    
    
    value = value.replace(pontos, '')
    
    music['Nome'] = ' '.join(li.find('div', class_="cardCenterCol").find('div', class_="topInfo topSongs").div.a.text.split())
    music['URL'] = url + li.find('div', class_="cardCenterCol").find('div', class_="topInfo topSongs").div.a['href']
    music['Artista(s)'] = value
    music['Posicao'] = li.div.p.text
    music['Letra'] = ''
    
    musics.append(music)



'''
    Buscando as letras das 5 músicas com as maiores avaliações do site.
'''
for music in musics[:5]:
    res = requests.get(music['URL'])
    
    music['Letra'] = get_lyrics_music(res.text)

    print(music)





