print('### SOMA SEQUENCIA DE NUMEROS INTEIROS ###')

n = int(input('Digite quantos números terá sua sequencia: '))
i = 1
soma = 0

if n == 0:
	print('não existem números para somar !!')
else:
	while i <= n:
		print('entre com o ', i,'º número da sequencia')
		valor = int(input())
		soma = soma + valor
		i = i + 1
	print('A soma é: ', soma)

