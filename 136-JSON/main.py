"""
JavaScript Object Notation - JSON

"""
from dados import *
import json 

with open('clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)

for chave, valor in dados.items():
    print(chave)
    print(valor)