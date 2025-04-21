temperatura = float(input("Ingrese la Temperatura a convertir :"))
escala = input("Es Fahrenheit (F) o es Celsius (C) :")

if escala == "f":
    c =  (temperatura * 9/5) + 32
    print (c)
elif escala == "c":
    f =  (temperatura - 32) * 5/9
    print (f)
else:
    print("Error")