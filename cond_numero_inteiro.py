n = int(input('Digite um número inteiro: '))
igual = False
anterior = 0.5

while n != 0 and not igual:
	x = n % 10
	y = n // 10
	n = y
	if anterior == x:
		igual = True
	else:
		anterior = x

if igual == False:
	print('não')
else:
	print('sim')