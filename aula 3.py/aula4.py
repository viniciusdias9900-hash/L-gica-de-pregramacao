# exercício a) lousa

lista = [
    3,
    "oi",
    42,
]

print(lista)

lista = [3, 'oi', 42]

print(lista)

print('posição 0:', lista[0])
print('posição 1:', lista[1])
print('posição 2:', lista[2])


lista_b = [
    ["vitamina", 2],
    ["ferro", 5],
    ["carboidrato", 3.14],
]

print(lista_b) 

# print (lista)
for item in lista_b: 
    # print(item)
    for subitem in item: 
         print(subitem) 