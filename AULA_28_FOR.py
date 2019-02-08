
l = [1,2,3,4,5,6,7]
for i in l:
    print(i,end=(' ,'))

print('\n{:=^80}'.format(' TABUADA DO 2 '))
for num in l:
    print(num,'x',num * 2)


print('{:=^80}'.format(' SE IMPAR ou PAR '))
for i in l:
    if i % 2 == 0:
        print('é par')
    else:
        print('é impar')