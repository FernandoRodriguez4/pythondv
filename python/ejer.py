"""Escribir un programa donde tenga una lista y que a continuacion,
elimine los elementos repetidos, por ultimo mostrar la lista"""
"""#1
lista = [1,2,3,4,5,6,7,8,9,10,6,5,4,2]
limpia = set(lista)
lista = list(limpia)
print(lista)
"""
"""#2
lista2 = [1,2,4,5,6,7,5,4,2]
lista2 = list(set(lista2))

print(lista2)"""


"""Escriba un programa que tenga 2 listas y que, a continuacion, cree
las siguientes listas (en las que no debe de haber repeticiones)
- Lista de elementos que aparecen en las dos listas
- Lista de elementos que aparecen en la primera lista, pero no en la 2da
- Lista de elementnos que aparecen en la lista, pero no en la primera
- Lista de elementos en ambas listas 
"""

"""lista1 = ["Fernando", "Luisa","Lorena", "Alejandra","Lorena", "Alejandra", "Valeria", "Melany", "Valeria" ]
lista1 = set(lista1)
lista2 = ["Fernando", "Luisa","Lorena", "Alejandra", "Cesar", "Roberto", "Alex", "Nadia", "Liz", "Valerie "]
lista2 = set(lista2)

print(lista1)
print(lista2)

a = list(lista1 | lista2)
print(f"Los elementos de ambas listas son: {a}")
b = list(lista1 - lista2)
print(f"Los elementos que aparecen en A son: {b}")
c = list(lista2 - lista1)
print(f"Los elementos que aparecen en B son: {c}")
d = list(lista1 & lista2)
print(f"Los elementos de ambas listas son: {d}") """


# 3
"""Escriba un programa donde cree una lista con los siguientes personajes 
del señor de los anillos
Personaje1
1- Nombre: Aragon
2- Clase: Guerrero
3- Raza : Dundan del Norte
Personaje2
1- Nombre: Gandalf
2- Clase: Guerrero
3- Raza : Dundan del Norte
Personaje3
1- Nombre: Legolas
2- Clase: Arquero
3- Raza : Elfo Sindar
"""

p1 = {"Personaje1": {"Nombre": "Aragon", "Clase":"Guerrero","Raza":"Dundan del norte"}, "Personaje2": {"Nombre": "Gandalf", "Clase":"Mago","Raza":"Istar"},"Personaje3": {"Nombre": "Legolas", "Clase":"Guerrero","Arquero":"Elfo Sindar"} }
print(p1["Personaje1"])


lista = []
p= lista.append({"Nombre": "Aragon", "Clase":"Guerrero","Raza":"Dundan del norte"})
print(lista)


