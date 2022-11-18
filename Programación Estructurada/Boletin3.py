'''
Created on 26 sept 2022

@author: leonr
'''

# Ejercicio 1

numero = int(input("Inserte un número:"))

if numero%2 == 0:
    print("Su numero es par")
    
else:
    print("Su numero es impar")
 
 
print("------------")   

# Ejercicio 2

numero1 = int(input("Inserte un número:"))
numero2 = int(input("Inserte otro número:"))

if numero1 == numero2:
    print("Sus números son iguales")
    
elif numero1 > numero2:
    print("El primer número es mayor que el segundo")
      
else:
    print("Su primer número es menor que el segundo")
    
    
print("----------")

# Ejercicio 3

numero = int(input("Por favor, inserte un número:"))

if numero%2 == 0:
    print("Su número es múltiplo de 2")
    
if numero%3 == 0:
    print("Su número es múltiplo de 3")
    
print("---------")
# Ejercicio 4

edad = int(input("¿Cuál es su edad?:"))

if 0 >= edad <= 12:
    print("Es un niño")
    
elif 13 >= edad <= 17:
    print("Es un adolescente")
    
elif 18 >= edad <= 29:
    print("Es un jóven")    

elif 30 >= edad <= 99:
    print("Es un adulto")
    
    
print("---------")   


# Ejercicio 5

num1 = int(input("Inserte un número:"))
num2 = int(input("Inserte un número:"))
num3 = int(input("Inserte un número:"))
num4 = int(input("Inserte un número:"))

media = ((num1 + num2 + num3 + num4) / 4)
print(media)

if num1 > media:
    print("Su primer número es mayor que la media de los 4")

if num2 > media:
    print("Su segundo número es mayor que la media de los 4")

if num3 > media:
    print("Su tercer número es mayor que la media de los 4")

if num4 > media:
    print("Su cuarto número es mayor que la media de los 4")


print("---------")

# Ejercicio 6

letra = input("Escriba una letra:")
letras = letra.upper()

vocal1 = "A"
vocal2 = "E"
vocal3 = "I"
vocal4 = "O"
vocal5 = "U"

if letras == vocal1:
    print("Es la primera vocal")    
elif letras == vocal2:
    print("Es la segunda vocal")    
elif letras == vocal3:
    print("Es la tercera vocal")   
elif letras == vocal4:
    print("Es la cuarta vocal")     
elif letras == vocal5:
    print("Es la quinta vocal")
else:
    print("Es un carácter distinto a una vocal") 
    
print("---------")  
# Ejercicio 7

estadocivil = "S"
edad = 45


if (estadocivil == "S" or estadocivil == "D") and edad < 35:
    print("Pertenece al 12%")
    
elif edad > 50:
    print("Pertenece al 8'5%")
    
elif (estadocivil == "V" or estadocivil == "C") and edad < 35:
    print("Pertenece al 11'3%")

else:
    print("Pertenece al 10'5%")
    
print("---------") 

        
# Ejercicio 8

hora1 = 30
hora2 = 16
minuto1 = 40
minuto2 = 40
segundo1 = 30
segundo2 = 11

if 0 <= hora1 < 24 and 0 <= hora2 < 24 and 0 <= minuto1 < 60 and 0 <= minuto2 < 60 and 0 <= segundo1 < 60 and 0 <= segundo2 < 60:
    if hora1 > hora2:
        print("Hora 1 es mayor")

    elif hora2 > hora1:
        print("Hora 2 es mayor")
    
    else:
        if minuto1 > minuto2:
            print("Hora 1 es mayor")
    
        elif minuto2 > minuto1:
            print("Hora 2 es mayor")
    
        else:
            if segundo1 > segundo2:
                print("Hora 1 es mayor")
    
            elif segundo2 > segundo1:
                print("Hora 2 es mayor")
    
            else:
                print("Son iguales las 2 horas")    
    
else:
    print("Los datos son incorrectos")    

print("---------")

# Ejercicio 9

tipoProducto = input("¿Qué tipo de producto tiene?:")
precioOriginal = int(input("Cuál es su precio original?:"))
productomayus = tipoProducto.upper()

if productomayus == "A":
    print("Obtiene un 7% de descuento")    
    print(precioOriginal - ((precioOriginal * 7)/100))
    
elif productomayus == "C" or precioOriginal < 500:
    print("Obtiene un 12% de descuento")
    print(precioOriginal - ((precioOriginal * 12)/100))

else:
    print("Obtiene un 9% de descuento")
    print(precioOriginal - ((precioOriginal * 9)/100))
    
print("---------")
# Ejercicio 10

caracter = input("Introduzca un carácter:")
num1 = int(input("Introduzca un número:"))
num2 = int(input("Introduzca otro número:"))

if caracter == "+":
    print(num1 + num2)
    
elif caracter == "*" :
    print(num1 * num2)
    
elif caracter == "-":
    print(num1 - num2)
    
elif caracter == "/":
    print(num1 / num2)
    
else:
    print("ERROR")

'''
