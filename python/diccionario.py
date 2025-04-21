"""#Diccionario

dc1 = {"azul" : "blue","rojo":"red","negro":"black"}

#Agregar elementos al diccionario
dc1["amarillo"] = "yelow"

#Modificar un elemento del diccionario
dc1["negro"] = "BLACK"

#Eliminar elementos de un diccionario

del(dc1["amarillo"])

#Consultar un solo elemento del diccionario
print(dc1["negro"])"""

"""#Ejemplo

dc2 = {"fernando": {"edad":22, "peso" : 80.0},"valeria": {"edad":19, "peso" : 60.0}}

dc2["Luisa"] = {"edad": 20, "peso": 60.0 }
"""

#Ejemplo 2

madrid = {11:{"Nombre": "Bale","posicion": "extremo" }, 10: {"Nombre":"modric","posicion":"mediocampista"},7:{"Nombre":"Ronaldo","posicion":"delantero"}}
print(madrid.get(9,"no existe un jugador con ese dorsal"))