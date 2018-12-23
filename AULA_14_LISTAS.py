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

# TAMANHO DA LISTA

print('='*80)
print('\n')
print('Foram informados {} registros na lista 1'.format(len(lista1)))
print('E {} registros na lista 2'.format(len(lista2)))

