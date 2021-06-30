n = int(input('entre número inteiro diferente de 0: '))

seq = [n]
ordem_decresc = 0

while abs(n) > 0:
    n = int(input('entre com outro número: '))
    if n == 0:
        print('a sequencia em ordem decrescente é: ')
    else:
        seq.append(n)
        ordem_decresc = len(seq) - 1

while ordem_decresc >= 0:
    print(seq[ordem_decresc], end=", ")
    ordem_decresc = ordem_decresc - 1
