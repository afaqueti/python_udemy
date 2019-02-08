# COMPREENSÃO EM LISTA

x = []
for i in range(0,10):
    x += [i]
    print(i)

x2 = [i for i in range(0,11)]
print(x2)

x3 = [i* 2 for i in range(1,11)]
print(x3)