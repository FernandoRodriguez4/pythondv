
lenguajes =  ["rubi", "java", "js", "react"]

#Aplicado a un listado
i=0
while i < len(lenguajes):
    print(lenguajes[i])
    i = i + 1


conteo = int(input("Ingresa un numero para realizar un conteo hacia atras: "))

while conteo >= 0:
    print (conteo)
    conteo = conteo - 1

print("Cuenta realizada correctamente ")