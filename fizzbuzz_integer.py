x = int(input('digite um número inteiro: '))
div3 = x%3
div5 = x%5
if div3 == 0 and div5 == 0:
	print('FizzBuzz')
else:
	print(x)