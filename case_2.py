def dia_semana(dia):
	match dia:
		case '1':
			print('Você escolheu o Domingo')
		case '2':
			print('Você escolheu a Segunda')
		case '3':
			print('Você escolheu a Terça')
		case '4':
			print('Você escolheu a Quarta')
		case '5':
			print('Você escolheu a Quinta')
		case '6':
			print('Você escolheu a Sexta')
		case '7':
			print('Você escolheu o Sábado')
		case '0':
			print('Você escolheu sair')
			exit()
		case _:
			print("Valor {} invalido".format(dia))



if __name__ == '__main__':

	continuar = True

	while continuar == True:

		print('##################')
		print('#                #')
		print('# DIAS DA SEMANA #')
		print('#                #')
		print('# 1 - Domingo    #')
		print('# 2 - Segunda    #')
		print('# 3 - Terça      #')
		print('# 4 - Quarta     #')
		print('# 5 - Quinta     #')
		print('# 6 - Sexta      #')
		print('# 7 - Sábado     #')
		print('#                #')
		print('# Z - Sair       #')
		print('#                #')
		print('##################')

		escolha_dia = input('Qual dia da semana você escolhe? ')
		dia_semana(escolha_dia)

	print('Você escolheu sair')