# ARQUIVOS

# NECESSÁRIO QUE O ARQUIVO SEJA CRIADO NA RAIZ DO DIRETORIO REFERENTE AO PROJETO
arquivo = open('teste.txt')
#arquivo.write('Este arquivo foi alterado!!! novamente.')
print(arquivo)
#RESULTADO É O OBEJTO:
#<_io.TextIOWrapper name='teste.txt' mode='r' encoding='UTF-8'>


#MÉTODO (.read)
#RETORNA O CONTEUDO DO ARQUIVO
print(arquivo.read())


#MÉTODO (.seek)
#RETORNA O INCIO DO CURSOR, POIS O PYTHON NECESSITA SABER ONDE INICIAR A LEITURA DA LINHA.
print(arquivo.seek(0))


#MÉTODO (.readline)
# RETORNA O CONTEUDO DO ARQUIVO APÓS A EXECUÇÃO DO (.seek), POIS O CURSO INCIOU DO ZERO.
#print(arquivo.readline())

print('='*80)

for line in arquivo:
    print(line)





