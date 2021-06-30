
n = int(input('Digite um número inteiro: '))

soma = 0

while  n != 0:
	algarismo = n % 10
	n = n // 10
	soma = soma + algarismo
print(soma)