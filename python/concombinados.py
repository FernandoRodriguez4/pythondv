#Condicional combinado

edad = int(input("Ingresa tu edad :"))

if edad >0 and edad >= 18 : 
    print("Edad correcta")
    if edad >= 18:
        print("Es mayor de edad")
else: 
    print("Es menor de edad")