'''TIPOS NUMÉRICOS'''

# numero1 = 10

# print (numero1)
# print (type(numero1))

# numero2 = 10.4

# print (type(numero2))


'''LISTA SÃO OBJETOS MUTAVEIS'''

'''TUPLAS SÃO LISTAS IMUTAVEIS'''

# lista = []
# lista.append('caguei mole')
# print(lista)
# lista.append('agora caguei duro')
# print(lista)

# for item in lista:
#     print(item)


'''Em Python, um conjunto é uma coleção não ordenada de elementos únicos. Os conjuntos são úteis quando você precisa armazenar itens sem duplicatas e realizar operações matemáticas como união, interseção e diferença entre conjuntos.'''
# c1 = set(list(range(1,10)))
# print (c1)
# c2 = set(list(range(5,15)))
# c3 = set(list(range(7,20)))
# print(c1.intersection(c2))
# print(c1.union(c2))
# print(c1.intersection(c2).intersection(c3))


'''DICIONÁRIO, TIPO UMA ARRAY ASSOCIATIVA'''
'''ESTRUTURA DE DADO CHAVE - VALOR'''
lista_telefonica = {}
print(type(lista_telefonica))

lista_telefonica['Orlando'] = ('orlando', 'python')

print(lista_telefonica['Orlando'])


print(lista_telefonica.keys())

lista_telefonica['Nilton'] = ('nilton', 'algoritmo')

print(lista_telefonica.keys())

print(lista_telefonica.get('Orlando'))

'''RETORNA NÃO ENCONTREI SE NÃO TIVER A ESSA CHAVE NA ARRAY'''
print(lista_telefonica.get('orlando', 'nao encontrei'))
