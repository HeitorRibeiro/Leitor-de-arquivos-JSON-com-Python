import json

#Lendo o arquivo JSON
def ler_json():
    with open('arquivo.json', 'r', encoding='utf8')as f:
        return json.load(f)

#Resposta do arquivo JSON
data = ler_json()
print(data)