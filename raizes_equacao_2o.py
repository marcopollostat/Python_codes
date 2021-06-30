# calcula raizes da equacao 2o grau ==> ax² + bx + c
import math

paramA = float(input('entre com parametro a: '))
paramB = float(input('entre com parametro b: '))
paramC = float(input('entre com parametro c: '))

#equa2oGrau = paramA*x**2 + paramB*x + paramC

#baskara formula
delta = paramB**2 - 4*paramA*paramC


#try:
#	d1 = math.sqrt(delta)
#	except d1 < 0:
#		print ("Please enter 3 valid sides")

#delta = float(delta)
#calcular raizes
x1 = (-paramB + delta)/(2*paramA)
#x1 = float(x1)
x2 = (-paramB - delta)/(2*paramA)
#x2 = float(x2)

#condição das raizes (delta)
if delta == 0:
	print('Ambas as raizes sao iguais a: x1=x2=', x1)
else:
	if delta<0:
		print('As raizes não são reais')
	else:
		print('As raizes são: x1=',x1, 'e x2=',x2)
