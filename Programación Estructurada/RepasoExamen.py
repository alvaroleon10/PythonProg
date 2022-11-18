'''
Created on 25 oct 2022

@author: leonr
'''
#BOLETIN 6
'''
# Ejercicio 4
number = int(input("Insert one number:"))
suma = 0
while number < 0:
    number = int(input("The number is not right, try again:"))

for x in range (number+1):
    suma += x
print(suma)

# Ejercicio 5
number = int(input("Enter a number (negative to finish):"))
positive = 0

while number >= 0:
    number = int(input("Enter a number (negative to finish):"))
    positive += 1
print(f'You have entered {positive} positive numbers')


# Ejercicio 10

number = int(input("Enter an integer positive number:"))
factorial = 1
while number < 0:
    number(int(input("The number is not valid, try again:")))
    
if number == 0 or number == 1:
    print(f'The factorial is {1}')
else:   
    for x in range(number):
        factorial *= number-x
    print(f'The factorial is {factorial}')
    

# Ejercicio 9
number = int(input("Enter a number greater than 0:"))
suma = 0

while number <= 0:
    number = int(input("The number is not valid, try again:"))
                 
for x in range(1,number):
    if (number % x == 0):
        suma += x
if number == suma:
    print(f'The number is perfect')
else:
    print(f'The number is not perfect')
    

# Ejercicio 8
number = int(input("Enter one number:"))
question = input("Do you want to enter more numbers (Y/N)?:")
answer = question.upper()
menor = number

while answer == "Y":
    number = int(input("Enter another number:"))
    question = input("Do you want to enter more numbers (Y/N)?:")
    if number < menor:
        menor = number
else:
    print(f'The smallest number is {menor}')
    

#BOLETIN 7
# Ejercicio 1

num1 = int(input("Introduzca un número:"))
num2 = int(input("Introduzca otro número:"))
cociente = 0
resto = 0

if num1 >= num2:
    resto = num1
    while resto >= num2:
        resto -= num2
        cociente += 1
    print(cociente)
    print(resto)
    
if num2 >= num1:
    resto = num2
    while resto >= num2:
        resto -= num1
        cociente += 1  
    
    print(cociente)
    print(resto)
 
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
   
# Ejercicio 17 Boletin 4

num = int(input("Inserte un número:"))

for x in range(0,num+1):
    if x % 2 == 0:
        print(x)

# Ejercicio 18 Boletin 4

limInferior = int(input("Inserte un número:"))
limSuperior = int(input("Inserte un número:"))
suma = 0
numout = 0
numigual = 0

while limInferior > limSuperior:
    print("Valores erróneos, pruebe de nuevo")
    limInferior = int(input("Inserte un número:"))
    limSuperior = int(input("Inserte un número:"))
num = int(input("Introduzca un número:"))
while num != 0:
    if num != limInferior and num != limSuperior:
        suma += num
    if num < limInferior or num > limSuperior:
        numout += 1
    if num == limInferior or num == limSuperior:
        numigual += 1
    num = int(input("Introduzca un número:"))
if num == 0:
    print(f'La suma total de los números introducidos es {suma}')
    print(f'Hay {numout} números fuera del intervalo')
    print(f'Hay {numigual} números iguales que algun límite del intervalo')
   

# Ejercicio 19 Boletin 4

num1 = int(input("Base de la potencia:"))
num2 = int(input("Exponente de la potencia:"))
potencia = 1
contador = 1


if num2 == 0:
    print(f'El resultado de la potencia es 1')
if num2 == 1:
    print(f'El resultado de la potencia es {num1}')
    
while contador <= num2:
    potencia*=num1
    contador+=1
print(f'El resultado de la potencia es {potencia}')

'''

# Ejercicio 20 Boletin 4

pagado = 10
contador = 1

while contador <= 20:
    pagado*=2
    contador+=1
print(f'Tras los 20 meses paga {pagado}')
    



    
        


    




    
    