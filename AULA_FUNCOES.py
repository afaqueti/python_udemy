# FUNÇÕES

def primeira_funcao():
    """
    ola mundo
    """
    st = 'Print only the word that start with s in this sentence'
    s = st.split()
    for i in s:
        ta = len(i)
        if ta % 2 == 0:
            print('A palavra ({}) é par'.format(i))


primeira_funcao()

print('=' * 80)


def segunda_funcao():
    """""
    Teste para nome de funções
    """""
    n1 = 'teste'
    print(n1)


segunda_funcao()

print('=' * 80)


def somar(num1, num2):
    print(num1 + num2)
somar(2, 5)
somar('Ola, ','Mundo')

print('=' * 80)


def subtrair(n1, n2):
    """
    COMANDO RETORN IRÁ RETORNA A RESPOSTA DA MINHAD FUNÇÃO.
    """
    return n1 - n2
x = subtrair(120,15)
print(x)


print('='*80)
def primo(num):
    """
    :param num:
    :return: Retornará os nmero primos até o primeiro que não for primo.
             Portanto o 'break' ira para o comando FOR.
    """
    for i in range(2,num):
        if num % i == 0:
            print('Não é primo')
            break
    else:
        print('É primo')

primo(117)
