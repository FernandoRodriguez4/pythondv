lenguajes =  ["rubi", "java", "js", "react"]
lenguajes.insert(1, "Node.js") # Este metodo se usa para insertar un elemento a la lista
lenguajes.insert(0, "Express")
lenguajes.remove("rubi") # Se usa cuando se quiere eliminar un elemento
print("js" in lenguajes) # Palabra reservada retorna True or False
lenguajes.sort() # ordena la lista alfabeticamente
lenguajes.reverse() # invierte la lista desde el ultimo indice
lenguajes.append("Django") #Para agregar un elemento al final de la lista
lenguajes.pop(1) # Para eliminar un elemento de la lista. 
lenguajes.index("java") #Para saber la posicion de un elemento
lenguajes.count("js") #Para contar cuantas veces se repite un elemento

print(len(lenguajes)) #Para contar la longitud de la lista

 
print(lenguajes)