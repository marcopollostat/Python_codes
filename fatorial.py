
n = int(input('Digite o valor de n: '))

FAT = n

if n == 0:
	print('1')
else:
	while n != 1:
		n_1 = n - 1
		FAT = FAT * n_1
		n = n_1
	print(FAT)	