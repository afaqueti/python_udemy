# .set somente permiter valores unicos, sets  possuiem alguns metodos

x = set()
print(x)

# NÃO CONFUNDIR O RESULTADO COMO CHAVES SENDO UM DICIONARIO.
x.add(1)
x.add(2)
print(x)

# o resultado serve para retornar a lista ordenada, conforme seus valores e não repetindo
lista = [11,11,11,22,22,22,4,4,5,5,8,8,8,9,10,10]
setlista = set(lista)
print(setlista)