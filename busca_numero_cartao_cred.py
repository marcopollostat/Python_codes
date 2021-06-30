meuCartão = int(input('Digite o número do seu cartão de crédito: '))

cartãoLido = 1 # atribuição valor para o criterio de parada do while => entrar primera vez no while

encontreiMeuCartãoNaLista = False # indicador de passagem => inicialmente não encontrei meu cartão na lista
									# iniciar o valor dessa variável ==> 1º valor do while
									#

while cartãoLido != 0 and not encontreiMeuCartãoNaLista: # criterios de parada enquanto não encontrei meu cartão na lista e não digitei 0.
	cartãoLido = int(input('Digite o número do próximo cartão de crédito: '))
	if cartãoLido == meuCartão: #
		encontreiMeuCartãoNaLista = True # indicador de passagem ==> aqui representa as itereções do while não fora

if encontreiMeuCartãoNaLista: #
	print('EBA!!! Meu cartão está lá!')
else:
	print('Xi, Meu cartão não está lá!')
