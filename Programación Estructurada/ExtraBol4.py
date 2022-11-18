'''
Created on 3 oct 2022

@author: leonr
'''
'''
# Ejercicio 17

num1 = int(input("Introduzca un número:"))
num2 = int(input("Introduzca otro número:"))

for pares in range (num1, num2, 2):
    if pares%2 == 0:
        print(pares)


print("-------------")

# Ejercicio 18

limInferior = int(input("Introduce un número:"))
limSuperior = int(input("Introduce otro número:"))

while limInferior >= limSuperior:
    limInferior = int(input("Pruebe otro límite inferior:"))
num = int(input("Inserte un nuevo número:"))

suma = 0 
fuera = 0
igual = 0
while num != 0:
     
    if limInferior < num < limSuperior:
        suma += num
           
    elif num < limInferior or num > limSuperior:
        fuera+=1
              
    else:
        igual+=1
    num = int(input("Inserte un nuevo número:"))

print(f"La suma de los números dentro del intervalo es {suma}, fuera del intervalo hay {fuera} números")
print(f"Existe {igual} números que coinciden con los límites")       
        

print("--------------")
'''
# Ejercicio 19

base = int(input("Introduzca la base de la potencia:"))
exponente = int(input("Introduzca ahora el exponente:"))
contador = 1
potencia = 1

if exponente == 0:
    print(f"El resultado de la potencia es {1}")
if exponente == 1:
    print(f"El resultado de la potencia es {base}")
    
while contador <= exponente:
    potencia*=base
    contador+=1
print(f"El resultado de la potencia es {potencia}")
    
'''

# Ejercicio 20

total = 10
contador = 1


while contador <= 20:
    total*=2
    contador+=1
    print(total)
    





    

    
        
    
    
   '''