"""# Escribir la siguiente expresion en forma de expresion algoritmica
# Se necesita pedir al usuario que ingrese 3 valores (a , b , c)

a = int(input("Ingresa el primer numero :")) 
b = int(input("Ingresa el segundo numero :"))
c = int (input("Ingresa el tercer numero :"))
resultado = round((a ** 3 * (b ** 2 - 2 * a * c)) / (2 * b))
print(resultado)

#Ejercicio 2

a= 10
b= 5
solucion = ((3+5*8) < 3 and ((-6 / 3 * 4) + 2 < 2)) or (a > b )
print (solucion)
"""
"""
#Ejercicio3
#Hacer un programa para intercambiar el valor de 2 variables
# a=10 --> a = 5
# b=5  ---> b = 10

a = 10 
b = 5

a,b= b,a
print(f"El nuevo valor de a es {a} ")
print(f"El nuevo valor de b es {b} " )
"""
"""#Hacer un programa paa ingresar el radio de un circulo y se reporte el area y su longitud de la circunferencia.
 
radio = float(input("Ingresa el radio del circulo en cm : "))
area = 3.1415 * radio ** 2
longitud = 2 * 3.1415 * radio
print(f"El area del circulo es {area}")
print(f"La circunferencia es {longitud}")"""

#5
"""Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente 
desea saber cuanto debera pagar finalmente por su compra 
"""
print("Solo por hoy ofrecemos un 15 '%' de descuento")
p1 = float(input("Digita el precio de la prenda :"))

"""totalcompra = p1 + p2 * 0.15 #Esto no es valido porque se esta aplicando el desuento 
                            # solo a la prenda 2 porque segun el orden de prioridad de operadores
                            # primero se ejecuta la * 
   """
descuento = p1 * 0.15
totalcompra = p1 - descuento                   
                            

print(f"El monto final es {totalcompra}")