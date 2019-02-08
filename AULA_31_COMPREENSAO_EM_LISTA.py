# COMPREENSÃO EM LISTA

x = []
for i in range(0,10):
    x += [i]
    print(i)

x2 = [i for i in range(0,11)]
print(x2)

x3 = [i* 2 for i in range(1,11)]
print(x3)

x4 = [i for i in range(0,21) if i % 2 == 0]
print(x4)

lista = []
lista = [variavel_igual for variavel_igual in 'alessandro']
print(lista)
print(len(lista))

