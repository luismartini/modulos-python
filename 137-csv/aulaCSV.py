import csv

with open('D:\\udemy-python\est\modulos-python\csv\clientes.csv') as arquivo:
    #dados = csv.DictReader(arquivo)
    dados = [x for x in csv.DictReader(arquivo)]
    #dados = csv.reader(arquivo)
    #next(dados)
    
# for dado in dados:
#     print(dado)

#configura como vai escrever
with open('clientes2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo, 
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )
    
    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3]
        ]
    )
    
    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )