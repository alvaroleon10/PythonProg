'''
Created on 14 oct 2022

@author: leonr
'''

'''
# Ejercicio 1

num1 = int(input("Introduzca un número:"))
num2 = int(input("Introduzca otro número:"))
cociente = 0
resta = 0
if num1 > num2:
    resta = num1
    while resta >= num2:
        resta -= num2
        cociente+=1
    print(f"El cociente de la división es {cociente}")
    print(f"El resto es {resta}")
if num2 > num1:
    resta = num2
    while resta >= num1:
        resta -=num1
        cociente+=1
    print(f"El cociente de la división es {cociente}")
    print(f"El resto es {resta}")
    
'''
print("----------")
# Ejercicio 2

num1 = int(input("Inserte un número:"))
num2 = int(input("Inserte otro número:"))
contador = 0
cadena = ""

while contador<10:
    num1+=1
    if num1%num2==0:
        contador+=1
        if contador != 10:
            cadena+=str(num1) + ", "
        else:
            cadena+=str(num1)              
print(cadena)


'''
# Ejercicio 3

number = int(input("Introduzca un número:"))
cuadrado = number * number

while number != 0:
    cuadrado = number * number
    if number%2==0:
        if number < 0:
            print("Es par, negativo y su cuadrado es " + str(cuadrado))
        
        elif number >= 0:
            print("Es par, positivo y su cuadrado es " + str(cuadrado))
    
    else:
        if number < 0:
            print("Es impar, negativo y su cuadrado es " + str(cuadrado))
        
        elif number >= 0:
            print("Es impar, positivo y su cuadrado es " + str(cuadrado))
    number = int(input("Introduzca un número:"))
    
print("---------------")


# Ejercicio 4

num = int(input("Inserte el tamaño de su secuencia numérica:"))

contador = 1
numero = 1
secuenciaA = ""
while contador<=num:
    secuenciaA += str(numero)
    if contador != num:
        secuenciaA+= ","
    numero*=-5
    contador+=1
print(secuenciaA)

secuenciaB = ""
numero = 0
contador=0
while contador < num:
    
    if numero%3==0:
        numero=1
    elif numero%3==1:
        numero=-1
    elif contador%3==2:
        numero=0
    if contador != (num-1):
        secuenciaB+= str(numero) + ","
    else:
        secuenciaB+= str(numero)
    contador+=1
print(secuenciaB) 

secuenciaC = ""
numero = 1
contador = 1

while contador <= num:
    secuenciaC += str(numero)
    if contador != num:
        secuenciaC += ", "
    numero *= 3
    contador += 1
print(secuenciaC)


# Ejercicio 5
numero = int(input("Introduzca un numero:"))
lista = [numero]
while numero != 1:
    if numero % 2 == 0:
        numero = numero//2
    else:
        numero = numero*3+1
    lista.append(numero)
print(lista)
    
    



# Ejercicio 6
 
edad = int(input("¿Qué edad tiene Juan?:"))
puzzle = 1
dinero = 20
contador = 0
acumPuzzle = 0
acumDinero = 0

    
while contador < edad:
    if edad % 2 != 0:
        puzzle *= 2
        dinero += 0
        acumPuzzle += puzzle
    else:
        dinero += 15
        puzzle += 0
        acumDinero += dinero
    
    
print(f'Recibe {puzzle} puzzles y {dinero} euros')
print(f'Acumula {acumPuzzle} puzzles y {acumDinero} euros')
        

    


# Ejercicio 7

contador = 0
numero = 3

while contador <= 3:
    


'''






















































































































































































'''

print("------")
 
        
# Ejercicio 5

n = int(input("Inserte un número"))


print("---------")


# Ejercicio 6

edad = int(input("¿Qué edad tiene Juan?:"))
dinero = 20

while 0 > edad > 100:
    edad = int(input("Edad no válida, pruebe otra vez:"))
    
if edad%2 == 0:
    for x in range(edad+1):
        puzzle = 1
        x*=2
        print(x)

'''    
    
    
        
   
        

        


    
    
        
            