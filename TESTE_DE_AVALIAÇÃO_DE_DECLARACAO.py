# TESTE DE AVALIAÇÃO DE DECLARAÇÕES

'''

USE FOR, SPLIT() E IF PARA DECLARAÇÃO QUE IMPRIMA AS PALAVRAS QUE COMEÇAM COM 'S'

'''

st = 'Print only the words that start with s in this sentence'
s = st.split()
for i in s:
    if i[0] == 's':
        print(i)


for i in st.split():
    if i[0] != 's':
        print(i)


#===================================================================================================

'''
USE RANGE() PARA IPRIMIR TODOS OS NÚMEROS PARES DE 0 A 10
'''

for i in range(0,11,2):
    print(i,end=' ')

#===================================================================================================

'''
USE A COMPREENSÃO DE LISTA PARA CRIAR UMA LISTA DE TODOS OS NÚMEROS ENTRE 1 A 50 QUE SÃO DIVISIVEIS POR 3
'''


