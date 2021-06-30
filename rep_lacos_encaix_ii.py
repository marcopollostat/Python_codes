
valor = int(input('entre com valor: '))

while valor >= 0:
	fat = 1
	while valor > 1:
		fat = fat * valor
		valor = valor - 1
	print(fat)
	valor = int(input('entre com valor: '))
