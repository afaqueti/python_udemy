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
print(x(30))



par = lambda x: x % 2 == 0
xx = par(23)
if xx == True:
    print('par')
else:
    print('impar')

print('='*80)

p = lambda s: s[1]

print(p([1,2,3,4,5]))

def lamb(p):
    p = lambda s: s[4:7]
    return p ('Isso ai')
print(lamb(p))