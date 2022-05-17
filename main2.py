def print_hi(name):
    print(f'Hi, {name}')

def calcular_area_retangulo(largura, comprimento):
    return largura * comprimento

def contagem_progressiva(fim):
	for numero in range(fim): #repetir o bloco de zero até o fim
		print(numero) # exibir o numero

def apoiar_candidato(nome, vezes):
    for numero in range(vezes):

        if numero < 9:
            print(f'00{numero + 1} - {nome}')
        elif numero < 99:
            print(f'0{numero + 1} - {nome}')
        else:
            print(f'{numero + 1} - {nome}')


# Estrutura de identificação / execução do script
if __name__ == '__main__':

    resposta = 'C'

    while resposta != '0':
        resposta = input('Escolha sua opção ')
        print(f'A sua escolha foi: {resposta} ')

        if resposta != '0':
            if resposta == '1':
                print_hi('José')
            elif resposta == '2':
                resultado = calcular_area_retangulo(2,6)
                print(f'A área do retângulo é de {resultado}m²')
            elif resposta == '3':
                contagem_progressiva(5)
            elif resposta == '4':
                apoiar_candidato('Teste', 6)
            else:
                print('Valor Inválido')
        else:
            print('Você escolheu sair')

