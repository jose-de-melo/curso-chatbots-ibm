# encoding: utf-8
from bs4 import BeautifulSoup
import requests
import re
import json

'''
    URL do site onde será feita a raspagem de dados.
'''
url = "http://www.henancius.com/henancius/top100.html"


'''
    Fazendo a requisição da página HTML
'''
res = requests.get(url)


'''
    Convertendo o texto HTML em objeto da classe BeautifulSoup.
'''
soup = BeautifulSoup(res.text.encode('iso-8859-1'), "html.parser")


'''
    Criando o dict para armazenar os dados.
'''
filmes = {'ranking': []}


'''
    Selecionando o conteúdo a ser 'raspado'
'''
tableExtern = soup.find("div", id="conteudo")

tableIntern = tableExtern.find_all("table")[2]

listTr = tableIntern.find_all('tr')

for i in range(1, len(listTr) - 1 ):
        listTd = listTr[i].find_all('td')
        infoFilme = {}
        infoFilme['Posição'] = int(listTd[0].text.replace('.', ''))
        infoFilme['Nome'] = ' '.join(listTd[1].text.split())
        infoFilme['Ano de Lançameto'] = int(listTd[2].text)
        infoFilme['Arrecadação'] = int(listTd[3].text.replace('.', '') + "00000")
        
        '''
            Adicionando um objeto com os dados de um filme na lista.
        '''
        filmes['ranking'].append(infoFilme)
    

'''
    Converte o dict em um objeto JSON e o grava no arquivo data/data.json. 
'''
with open('data/data.json', 'w') as outfile:
    json.dump(filmes, outfile, indent=4, ensure_ascii=False)