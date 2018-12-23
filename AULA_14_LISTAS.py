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