
s ='hello'
print(s)
print('Total de caracteres: ',len(s))
res = len(s) - 1
print('Total menos (-1) = ',res)
print('A ultima letra é :',s[res:len(s)])

ss = []
print('='*80)
print(s)
for i in range(1,len(s)+1):
   print('{} - {}'.format(i,s[i-1:i]))
print('\nA ultima letra é :', s[res:len(s)])


ss = []
print('='*80)
print(s)
for i in range(1,len(s)+1):
    ss.append(i)
print(ss)
print(ss.pop())



