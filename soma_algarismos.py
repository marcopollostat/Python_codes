
###### SOMA ALGARISMOS

n = int(input('Digite um número inteiro: '))

soma = 0 # declara e contador inicia da soma

#if n<0: #caso onde ocorre problemas com números negativos
#	print('SÓ POSITIVOS !!!!!!!!!!!!!!!!!!')
#else: # caso em que o numero é >= 0 (positivo)
while  n != 0: # condição verdadeira até que n = n // 10 seja igual a zero
	algarismo = n % 10 # começa a retirar e guardar os algarismo do número n
	n = n // 10 # essa divisão inteira retira a unidade (ultimo numero/algarismo)
	soma = soma + algarismo # incremento da soma
print('a soma é', soma)