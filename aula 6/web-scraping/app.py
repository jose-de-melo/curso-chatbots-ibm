from bs4 import BeautifulSoup
import requests
import re
import json



url = 'https://www.tastemade.com.br/videos/toalha-felpuda-dona-benta'

res = requests.get(url)

data = {}


#print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
ul = soup.find("ul", class_= re.compile(r'VideoRecipe__ColumnList'))

data['receitas'] = []

receita = {}
receita['ingredientes'] = []


for li in ul.find_all('li'):
    receita['ingredientes'].append(li.p.text)


h1 = soup.find("h1", class_ = re.compile(r'VideoInfoDetail__Title'))
receita['nome'] = h1.a.text
receita['instrucoes'] = []

ol = soup.find("ol", class_ = re.compile(r'recipe-steps-list'))

for li in ol.find_all('li'):
    receita['instrucoes'].append(li.p.text)

data['receitas'].append(receita)

with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4, ensure_ascii=False)