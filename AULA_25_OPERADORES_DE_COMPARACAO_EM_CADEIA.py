# OPERADORES

a = 1
b = 2
c = 1
res1 = a == c
res2 = a == c and b == 2 and c == 2  # RETORNA VERDADEIRO TODOS DEVE SER VERDADEIROS
res3 = a == 2 or b == 2  # SENDO SOMENTE UM VERDADEIRO O RETORNO E "TRUE"
res4 = (a != b or a == c) and b == 2
print(res1)
print(res2)
print(res3)
print(res4)