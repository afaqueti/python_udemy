
x = 1
y = 1

while x < 10 and y < 20:
    print('O valor de x e y é: ',x * y)
    x += 1
    y += 2
else:
    print('valor de x - y é:' ,x*y)


# BREAK quando falso o loop irá encerrar

x = 1
lista = []
while True:
    lista += [x]
    x += 1
    if x > 10:
        break
print(lista)

# CONTINUE

ate = 50
x = 1
while x < ate:
    x += 1
    if x % 2 == 1:
        continue
    if x % 2 == 0:
        print(x,end=(' -'))
