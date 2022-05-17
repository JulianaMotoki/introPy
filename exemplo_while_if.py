def dia_semana(dia):

		if continua == '1':
			print('Você escolheu o Domingo')
		elif continua == '2':
			print('Você escolheu a Segunda')
		elif continua == '3':
			print('Você escolheu a Terça')
		elif continua == '4':
			print('Você escolheu a Quarta')
		elif continua == '5':
			print('Você escolheu a Quinta')
		elif continua == '6':
			print('Você escolheu a Sexta')
		elif continua == '7':
			print('Você escolheu o Sábado')
		else:
			print("Valor {} invalido".format(dia))

if __name__ == '__main__':

	continua = 'C'

	while continua != '0':

		continua = input('Escolha sua opção ')
		print(dia_semana(continua))


	print('Você escolheu sair')