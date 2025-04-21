#Lista
lista = ["Fernando" , "Rodrigo", "Yuki", "Alejandro" , 10, 60.10]
"""print(lista[-2]) #Para acceder a un elemento de la lista."""


#sublistas --> Desde un rango a otro

"""print(lista[0: ])"""

#Sin poner un rango

"""print(lista[:3])  # Desde el inicio hasta la pos 2
print(lista[1:])  # Aca imprime desde la pos 1 hasta el final"""

# Determinar cuantos elemenos tiene la lista

print(len(lista))

"""lista1 = [1,2,3,4,5]
lista1.append("Valeria")
lista1.insert(3,"Fernando")
lista1.extend([7,8,9])
print(lista1)"""

lista3= [1,2,3,4, "Fernando"]

print(3 in lista3)
print(lista3.index(4))
print(lista3.count((2 in lista3)))