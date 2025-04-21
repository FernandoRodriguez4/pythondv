texto = "Hola Fabiana"
print(texto.upper()) #Metodo upper = Cambia la cadena de texto a mayuscula
print(texto.lower()) #Metodo lower = Cambia la cadena de texto a minusculas
print(texto.find("ola")) # Busca la cadena de texto en un string
print(texto.replace	("bi", "vi")) # Remplaza la cadena de texto por otra sin afectar la cadena de la var original
nuevavar = texto.replace("bi", "vi")
print(texto, nuevavar)

print("bi" in texto)