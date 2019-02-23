# FUNÇÕES

def primeira_funcao():
    '''
    ola mundo
    '''
    st = 'Print only the word that start with s in this sentence'
    s = st.split()
    for i in s:
        ta = len(i)
        if ta % 2 == 0:
            print('A palavra ({}) é par'.format(i))

primeira_funcao()

print('='*80)

def segunda_funcao():
    n1 = 'teste'
    print(n1)

segunda_funcao()