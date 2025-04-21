"""#

numero = int(input("Digita un numero :"))

if numero > 0:
    print("Es positivo")
    
elif numero == 0: 
    print(f"Ingresa nuevamente un numero : {numero}")
else: 
     print("Es negativo")
     
print("Fin del programa")
    """
    
"""#Ejercicios. 
#Hacer un programa que pida 2 numerosy se de cueta cual de ellos es par o si ambos lo son

numero1 = int(input("Ingresa el primer numero : "))
numero2 = int(input("Ingresa el segundo numero : "))


if numero1 %2==0 and numero2 %2==0:
        print("Ambos numeros son pares")
  
    
elif numero1 % 2==0 and numero2 %2!=0:
    print(f"{numero1} es par")
elif numero1 % 2!=0 and numero2 %2==0:
       print(f"{numero2} es par")
    
else: 
    print("Fin del programa")
    
"""

"""#Ejercicio2 
#Hacer un programa que pida 3 numeros y determine cual es el mayor

a= int(input("Ingresa el primer valor :"))
b= int(input("Ingresa el segundo valor :"))
c= int(input("Ingresa el tercer valor : "))

if a > b and a> c:
    print(f"{a} es el mayor")
elif b>a and b>c:
    print(f"{b} es el mayor")
elif c>a and c >b:
    print(f"{c} es el mayor")
else: 
    print("Fin del programa")"""
    
"""#Ejercicio3
#Hacer un programa que pida caracter e indique si es una vocal o no.

a= input("Ingresa un caracter :").lower()


if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
    print("es vocal")
    
else:
    print("Fin del programa")"""
    
"""#Ejercicio4
#Construir un programa que simule el funcionamiento de una calculadora que puede 
# realizar 4 operaciones aritmeticas basicas (suma, resta, multiplicaion y 
# division). El usuario debe de especificar la operacion con el primer caracter del nombr de la operacion

print("-------------------- Bienvenido a tu calculadora personalizada -----------------")
a= float(input("Ingresa un numero :"))
b= float(input("Ingresa un numero :"))

suma= a+b
resta= a-b
multiplicacion= a*b
division= a/b

operacion = input("Ingrese el primer caracter de la operacion que desee :").lower()

if operacion == 's':
    print((f"La suma es {suma}"))
elif operacion == 'r':
    print(f"La resta es {resta}")
elif operacion == 'm' or operacion == 'p':
    print(f"La multiplicacion es {multiplicacion}")
elif operacion == 'd':
   
        print(f"La division es {division}")
   

else: 
    print("Fin del programa")"""

#Hacer un programa que simule un cajero automatico con saldo inicial de 1000 
#y tendra el siguiente menu de opciones. 

"""
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero dispobilble
4.Salir
"""

saldo = 1000

print("\t ---- Menu de opciones ---- " )
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. salir")

opcion = int(input("Ingrese una opcion valida del 1 - 4 :"))

if opcion == 1:
    agregado=float(input("Ingresa el monto a abonar"))
    agregado+= saldo
    print(f"El monto total es {agregado}")
elif opcion ==2:
    retiro= float(input("Ingresa el monto a retirar : "))
    if retiro > saldo:
        print("No tienes esa cantidad")
    else:
        print(f"El monto total es {saldo - retiro}")
        
elif opcion==3:
    print(f"El sado disponible es : {saldo}")

elif opcion==4:
    


    print(" \t   ---- Gracias por usar nuestro servicio, regrese pronto ----")
