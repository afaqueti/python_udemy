# EXPERSSÃO LAMBDA

def square(num):
    res = num ** 2
    return res
print(square(16))


print('='*80)

# RETORNO OTMIZADO

def square_2(num):
    return num ** 2
print(square_2(4))

print('='*80)

def square_3(num): return num ** 2
print(square_3(12))

print('='*80)
def par(x):
    res = x % 2 == 0
    return res
if par(2) == True:
    print('par')
else:
    print('impar')

print('='*80)


# A FUNÇÃO "LAMBDA" É UM METODO E CRIAÇÃO DE FUNÇÃO OTMIZADA.

x = lambda num: num ** 2
print(x(10))


par = lambda x: x % 2 == 0
print(par(2))

