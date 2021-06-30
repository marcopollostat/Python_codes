#ler 4 numeros e ao final informar quantos numeros estao
#no intervalo entre 10 (inclusive) e 150 (inclusive)

print('### VC VAI DIGITAR 4 NUMEROS ###')
print()

cont = []
n = []
n.append(int(input('entre com o 1o numero')))
tam = len(n)

while tam < 4:
    n.append(int(input('entre com o proximo numero')))
    tam = len(n)

for x in n:
    if 10 <= x <= 150:
        cont.append(True)
        
    else:
        cont.append(False)

total = sum(cont)

print('existem ', total, 'números no intervalo de [10,150]')
