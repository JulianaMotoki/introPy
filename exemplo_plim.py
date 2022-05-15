def brincar_de_plim(fim):

	for numero in range(1, fim + 1):
		if numero % 4 == 0:
			print('Plim!')
		else:
			print('{:0>3}'.format(numero))

brincar_de_plim(100)