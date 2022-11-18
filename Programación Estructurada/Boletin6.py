'''
Created on 3 oct 2022

@author: leonr
'''

'''
# Ejercicio 1

for x in range (1,101):
    print(x)
    
num1 = int(input("Elija un número del 1 al 100:"))

if num1%7 == 0:
    print("El número elegido es múltiplo de 7")
    
elif num1%13 == 0:
    print("El número elegido es múltiplo de 13")
    
elif num1%7 == 0 and num1%13 == 0:
    print("El numero elegido es múltiplo de 7 y 13")

elif 1 <= num1 <= 100:
    print("Su número es el " + str(num1))
    
else:
    print("Su número no está dentro del intervalo")

print("-----------")

# Ejercicio 2

num = int(input("Introduzca un número entre 0 y 10:"))

if 0 <= num <= 10:
    for x in range(0,11):
        print(num * x)

else:
    print("El número está fuera del intervalo")

print("---------------")


# Ejercicio 3

numeros = int(input("How many numbers do you want to input?:"))

while numeros <= 0:
    numeros = int(input("The number is not valid, it should be greater than 0"))
    
for i in range (numeros):
    num = int(input("Enter a number greater than 0"))
    while num <= 0:
        num = int(input("The number is not valid, it should be greater than 0"))
        
    if num%2 == 0:
        print("The number " + str(num) + " is even")
    else:
        print("The number " + str(num) + " is odd")
        


print("-------------")

# Ejercicio 4

number = int(input("Enter one number greater than 0:"))
suma = (number*(number+1)/2)

while number <= 0:
    number = int(input("The number is not right, try again:")) 
    
if number > 0:
    for x in range(1, number+1):
        print(suma)
        
        break
       
print("-------------")

# Ejercicio 5

number = 1
cont = 0


while number >= 0:
    number = int(input("Enter a number (negative to finish):"))
    if number >= 0:
        cont = cont + 1
print(cont)

print("---------")

# Ejercicio 6

number1 = int(input("Enter one number:"))
number2 = int(input("Enter another number:"))
producto = 0
if number1 > 0:
    for x in range(number1):
        producto+=number2
        
elif number1 < 0:
    for x in range(abs(number1)):
        producto-=number2 
    
    print(f"The product is {producto}")


print("-----------")
# Ejercicio 7

num1 = int(input("How many numbers do you want input?: "))

while num1 <= 0:
    num1 = int(input("How many numbers do you want input?: "))
    
total = 0
    
for x in range (num1):
    num2 = int(input("Enter one number greater than 0: "))
    while num2 <= 0:
        num2 = int(input("The number is not valid, it should be greater than 0: "))
    total += num2
    
print(f"The medium is {total/num1}")

print("-----------")

# Ejercicio 8

num = int(input("Enter one number:"))
question = input("Do you want to enter more numbers (Y/N)?:")     
answer = question.upper()
menor = num

while answer == "Y":
    number = int(input("Enter another number:"))
    if number < menor:
        menor = number
    question = input("Do you want to enter more numbers (Y/N)?:")
    answer = question.upper()

print("The smallest number is " + str(menor))





# Ejercicio 9    

number = int(input("Enter an integer positive number greater than 0:"))
suma = 0


while number <= 0:
    number = int(input("The number is not valid, try again:"))
    
for x in range(1,number):
    if(number % x == 0):
        suma += x
if number == suma:
    print("The number is perfect")
else:
    print("The number is not perfect")
    

print("-----------")

# Ejercicio 10

number = int(input("Enter an integer positive number:"))

while number < 0:
    number = int(input("The number is not valid, try again:"))

total = 1    
for i in range (1,number+1):
    total *= i
print(total)

# Ejercicio 10 con while

numero = 6
total = 1
while numero > 0:
    total*=numero
    numero-=1
print(total)

'''                  
        
    
    
    

 
        
      
    
    



  

