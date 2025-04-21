"""#Conjunto ->

conjunto = set()

conjunto = {"Fernando", "Fernando", 1, 2 }

conjunto.add(5) # --> Al agregar un elemento se asigna aleatomiamente
conjunto.add("Valeria") # --> Al agregar un elemento se asigna aleatomiamente
conjunto.discard(2)
conjunto.remove(1)


#Buscar elementos
#Verificar si hay elementos

print("Valeri" in conjunto)



print(conjunto)"""

#Crear 2 conjuntos
"""a = set() #Conjuntos vacios
b = set() #Conjuntos vacios"""

a = {1,2,3,4}
b = {4,5,6}

c= { 1,2,3,4,5,6,7}

print(a.issubset(c))
print(b.issubset(c))
print(c.issuperset(a))
print(c.issuperset(b))
print(a.isdisjoint(b))


"""#Operaciones con conjuntos
c= a | b   #Union -> Conbina elementos
print(c)
d= a & b # Interseccion -> Elementos en ambos conjuntos
print(d)
e= a - b # Diferencia -> elemento de A que no esta en B
print(e)
f= a ^ b  #Diferencia simetrica -> Elementos que estan en ambos conjuntos pero no en ambos
print(f)"""

#Subconjuntos

