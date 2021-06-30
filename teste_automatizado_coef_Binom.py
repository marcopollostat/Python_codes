
def fatorial(n):
#	FAT = n
#	if n == 0:
#		print('1')
#	else:
#	while n != 1:
#		n_1 = n - 1
#		FAT = FAT * n_1
#		n = n_1
#	return FAT
#       print(FAT)

	fat = 1
	while n > 1:
		fat = fat * n
		n = n - 1
	return fat

def num_bin(n,k):
	return fatorial(n) // ( fatorial(k) * fatorial(n-k) )


#### testes automatizados para o fatorial

def testa_fatorial():
	if fatorial(1) == 1 :
		print('Funciona para 1')
	else:
		print('Não funciona para 1')
	if fatorial(2) == 2 :
		print('Funciona para 2')
	else:
		print('Não funciona para 2')
	if fatorial(0) == 1 :
		print('Funciona para 0')
	else:
		print('Não funciona para 0')
	if fatorial(5) == 120 :
		print('Funciona para 5')
	else:
		print('Não funciona para 5')
