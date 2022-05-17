def brincar_de_para_ou_continua():

	resposta = 'C' #C aqui significa que continua

	# while resposta == 'C' or resposta == 'c':
	while resposta.upper() == 'C':
		resposta = input('Digite C para CONTINUAR ou outro caracter para PARAR ')

	print('Você decidiu PARAR com a brincadeira')


if __name__ == '__main__':

	brincar_de_para_ou_continua()
