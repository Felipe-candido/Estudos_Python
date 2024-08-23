def fizzbuzz(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        return 'fizzbuzz'

    elif numero % 3 == 0:
        return 'fizz'
        
    elif numero % 5 == 0:
        return 'buzz'
        
        
    else:
        return numero

for i in range (100):
    assert fizzbuzz(i)

lista = []
for i in range(1,101):
    if i % 5 == 0 and i % 3 == 0:
        lista.append('fizzbuzz')

    elif i % 3 == 0:
        lista.append('fizz')
        
    elif i % 5 == 0:
        lista.append('buzz')
    lista.append(i)

print (lista)