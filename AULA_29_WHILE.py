
x = 1
y = 1

while x < 10 and y < 20:
    print('O valor de x e y é: ',x * y)
    x += 1
    y += 2
else:
    print('valor de x - y é:' ,x*y)


# BREAK

x = 1
lista = []
while True:
    lista += [x]
    x += 1
    if x > 10:
        break
        print(lista)
