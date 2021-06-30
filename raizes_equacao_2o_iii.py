
import math

#def delta(a,b,c):
 #   d = b ** 2 - 4 * a * c
  #  sqrt_d = math.sqrt(d)
   # return sqrt_d

#def raizes(a,b,c):
 #   x1 = ( - b + delta(a,b,c) ) / ( 2 * a )
  #  x2 = ( - b - delta(a,b,c) ) / ( 2 * a )
   # print(x1, 'e', x2)
    
# exemplo prof refatorando o exercicio da obtençaõ raizes eq 2º grau
def delta(a,b,c):
		return b ** 2 - 4*a*c

def main():
	a = float(input('digite valor de a'))
	b = float(input('digite valor de b'))
	c = float(input('digite valor de c'))
	imprime_raizes(a,b,c)

def imprime_raizes(a,b,c):
	d = delta(a,b,c)
	if d == 0:
		raiz1 = (-b + math.sqrt(d)) / (2 * a)
		print('A unica raiz é: ', raiz1)
	else:
		if d < 0:
			print('Esta equacao não tem raizes reais')
		else:
			raiz1 = (-b + math.sqrt(d)) / (2 * a)
			raiz1 = (-b - math.sqrt(d)) / (2 * a)
			print('A primeira raiz é: ', raiz1)
			print('A segunda raiz é: ', raiz2)
