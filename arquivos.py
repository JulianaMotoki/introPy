# 1 - importação de pacotes

import json

# 2 - Classe

# 3 - Definições (Funções e métodos)

dados = {}

dados['cliente'] = []
dados['cliente'].append({
    'nome':'Juca',
    'telefone':'11999999999',
    'email': 'juca@iterasys.com.br'
})
dados['cliente'].append({
    'nome':'Ana',
    'telefone':'21888888888',
    'email': 'ana@iterasys.com.br'
})

def criar_json():
    with open('clientes.json','w') as outfile:
        json.dump(dados,outfile)


def testar_criar_json():
    criar_json()
    print(dados['cliente'])