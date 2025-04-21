"""edad = 22
print(edad > 18)
print(edad >= 18 and edad <=23)
print(edad >= 18 or edad <=22)
print(not(edad <=23)) # 22 es menor que 23? si pero al poner not se esta inviertiendo
"""
## Crea 3 variables

a = 12
b = 13
c = 15 

resultado =not (((a < b)) and ((a > c)) or (( c == a)) and (( c < a)))
print(resultado)