# 1 - imports / bibilhotecas

# 2 - Classe

# 3 - Metodos e Fuções
# def = deffinition = definição

# def print_hi(name):
#     print(f'Hi, {name}')

# def calcular_area_retangulo(largura, comprimento):
#     return largura * comprimento

# def contagem_progressiva(fim):
# 	for numero in range(fim): #repetir o bloco de zero até o fim
# 		print(numero) # exibir o numero

def apoiar_candidato(nome, vezes):
    for numero in range(vezes):
        # contador = numero + 1
        # print(f'{contador} - {nome}')

        if numero < 9:
            print(f'00{numero + 1} - {nome}')
        elif numero < 99:
            print(f'0{numero + 1} - {nome}')
        else:
            print(f'{numero + 1} - {nome}')



# Estrutura de identificação / execução do script
# if __name__ == '__main__':
#     print_hi('Juliana')
#
# resultado = calcular_area_retangulo(3,4)
# print (f'A area do retangulo é de {resultado} m²')

# Executar uma contagem progressiva
# contagem_progressiva (10)

nome = input(f'Qual é o seu candidato? ')
vezes = int(input(f'Quantas vezes você quer apoiar seu candidato? '))

apoiar_candidato(nome,vezes)
