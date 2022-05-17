def dia_semana(dia):
	match dia:
		case 1:
			print('Domingo')
		case 2:
			print('Segunda')
		case 3:
			print('Terça')
		case 4:
			print('Quarta')
		case 5:
			print('Quinta')
		case 6:
			print('Sexta')
		case 7:
			print('Sábado')
		case _:
			print("Valor {} invalido".format(dia))

def cor_favorita(cor):
	match cor:
		case 1:
			return 'azul'
		case 2:
			return 'amarelo'
		case 3:
			return "Valor {} invalido".format(dia)

if __name__ == '__main__':

	escolha_dia = int(input('Escolha um número '))
	dia_semana(escolha_dia)

	escolha_cor = int(input('Escolha um numero de cor favorita: '))
	print(cor_favorita(escolha_cor))