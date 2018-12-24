# DICIONÁRIOS
# OS DICIONÁRIOS TRABALHA COM UMA CHAVE PARA INDEXAR O EXEMPLO DE UMA LISTA.
# DICIONARIOS SÃO MULTAVEIS PODE SER ALTERADOS

my_list = [1,2,3,4]
print(my_list[0:4])

my_dict = {'chave1':1.2, 'chave2':'Teste'}
my_dict2 = {'chave4':1.2,'chave3':'novoteste'}

my_dict3 = {'chave5':my_list,'chave3':{'key1':'ola'}}


print(my_dict)
print(my_dict2)
print(my_dict3)

# PODEMOS TER UM DICIONARIO DENTRO DE OUTRO DICIONARIO (ANINHA OS DICIONARIOS)
print(my_dict3['chave3'])

# MÉTODOS

# METODOS (.KEIS) INFORMA TODAS AS CHAVES DENTRO DO SEU DICIONARIO.
print('Esse método retorna quantas chaves foram criadas',my_dict.keys())
print('O list retorna sem o dict_keys',list(my_dict.keys()))
print('A list pode retorna somente um unico indice [0]',list(my_dict3.keys())[0])

# MÉTODO (.VALUES) CONTEM TODOS OS VALORES DA CHAVES INCLUISIVE O ANINHADO.

print(my_dict3.values())
print(list(my_dict3.values()))

# MÉTODO (.ITEMS) RETORNA TODOS OS INDEICES

print(my_dict.items(),my_dict3.items())





