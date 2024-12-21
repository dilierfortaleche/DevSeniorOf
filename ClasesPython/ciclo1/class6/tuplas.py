# tuplas

paises = ('Colombia', 'Mexico', 'Ecuador', 'Venezuela')

# ver tipo
print(type(paises))

print(len(paises))

print(paises[2])

print(paises[-1])

for pais in paises:
    print(pais)


paisesLista =list(paises)
paisesLista[1] = 'Argentina'
paises = tuple(paisesLista)

del paises
print(paises)