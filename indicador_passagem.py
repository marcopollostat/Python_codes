
decrescente = True # variavel booleana = indicador de passagem

anterior = int(input('Digite o primeiro numero da sequencia: ')) # valor inicial do 'anterior'

valor = 1 # porque ao começar o while requer uma atribuição diferente de zero para iniciar 'valor'

while valor != 0 and decrescente: # critério de parada => mas tambem executar enquanto for decrescente => 
	valor = int(input('Digite o proximo numero da sequencia: ')) #
	if valor > anterior: # pra ser decrescente o 'valor' tem que ser menor que o 'anterior' (MAS O CONTRARIO QUE INTERESSA => USAR INDIC PASSAG)
		decrescente = False # a sequencia não está em ordem decrescente
	anterior = valor # nessa interação o 'valor' será o 'anterior' da proxima interação

if decrescente:
	print('A sequencia esta em ordem decrescente')
else:
	print('A sequencia não esta em ordem decrescente')