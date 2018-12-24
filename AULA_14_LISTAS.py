# LISTAS

# LISTA NO PYTHON NÃO TEM LIMITES, DIFERENTE DE OUTRAS LINGUAGENS QUE USA ESSE METODO COMO "ARRAY"

lista1 = [1,2,3,4,5]
print('Lista Um --- ',lista1)

# LISTA - CONTANDO QUANTOS CARACTERES EXISTE NA COLUNA STRING
lista2 = [1,3,4,'Nicolas',10]
print('lLsta Dois --- ',lista2)
print('Lista Dois',lista2[3:4])
s = str(lista2[3:4])
print('Nome digitado como string --- ',s[2:-2])
print('A string contem {} letras'.format(len(s[2:-2])))


# JUNTANDO AS DUAS LISTA (LISTA1 + LISTA)

a = lista1 + lista2
print(a)

print('='*80)
lista2 = lista2 + ['Alessandro',1,11.15,14]
print('\n',lista2)

# MULTIPLICAR A LISTA POR UM VALOR USANDO LAÇO DE REPSTIÇÃO
# TIRANDO OS COLCHETES DO PRINT PARA QUE A SAIDA FIQUE LIMPA

print('='*80)
num1 = int(input('\nQuantas vezes a lista será repetida? '))
if num1 > 10:
    print('O valor digitado é muito alto')
else:
    for i in range(1,num1+1):
        num = str(lista2)
        print(num[1:-1])

# TAMANHO DA LISTA, UANDO COANDO "(LEN)"

print('='*80)
print('\n')
print('Foram informados {} registros na lista 1'.format(len(lista1)))
print('E {} registros na lista 2'.format(len(lista2)))


# MÉTODOS DE LISTAS

# O MÉTODO (.APPEND) INCLUI UM OBJETO AO FINAL DA LISTA
print('='*80)
lista1.append('Mais um valor')
print('Método .APPEND ---- ',lista1)

# O MÉTODP (.POP) RETORNA SEMPRE O ULTIMO VALOR
print('='*80)
print('Método .POP ------ ',lista1.pop())


print(lista1.pop(0))

v = lista1.pop(0)
print(lista1)
print(v)

# MÉTODO REVERSE, INVERTE A SEQUENCIA DA LISTA

print('='*80)
print('\n{:=^80}'.format(' MÉTODO REVERSE '))
new_lista = ['a','e','x','b','c']
print(new_lista)
new_lista.reverse()
print(new_lista)

# MÉTODO SORT, ORDENA EM FORMA ALFABETICA OU SEQUENCIAL

print('='*80)
print('\n{:=^80}'.format(' MÉTODO SORT '))
new_lista.sort()
print(new_lista)

# USANDO REVERSE COM INDEXÃO

print('='*80)
print('\n{:=^80}'.format(' REVERSE COM INDEXÃO '))
new_lista
print(new_lista)
print(new_lista[::-1])


# LISTA DENTRO DE LISTAS

print('='*80)
print('\n{:=^80}'.format(' lISTA DENTRO DE LISTAS '))
list_1 = [1,2,3]
list_2 = [4,5,6]
list_3 = [7,8,9]
matrix = [list_1,list_2,list_3]
print('As 3 listas juntas dentro de uma MATRIX: ',matrix)
print('Retorna qual lista dentro da matriz: ',matrix[2])
print('Retorna o valor dentro da lista:',matrix[2][1])

# IDENTIFICAR ATRAVÉS DO (FOR) DENTRO DA LISTA, QUAIS REGISTRO DA COLUNA 0 DE TODAS A LISTAS
first_colun= [row[0] for row in matrix]
print(first_colun)

t = ['a','b','c']
print(t[0:])










