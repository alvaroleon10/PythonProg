'''
# Ejercicio 1

numero = int(input("Inserte un número:"))
def computeFactorial (numero):
    while numero > 0:
        contador = 1
        factorial = 1
        while contador <= numero:
            factorial *= contador
            contador += 1
        return factorial
    return None
print(computeFactorial(numero))

# Ejercicio 2

number = int(input("Pick a number:"))

def isLeapYear (number):
    if (number%4) and not number%100!=0 or number%400:
        mensaje = True
    else:
        mensaje = False 
    return mensaje
print(isLeapYear(number))
        
        
# Ejercicio 3

month = int(input("Inserte un mes (1-12):"))
year = int(input("Inserte un año:"))
listaMeses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
sumaDias = 0
def computeDaysInMonth (month, year):
    while 0 > month > 12  or year < 0:
        return -1
    if month == listaMeses[0, 2, 4, 6, 7, 9, 11]:
        sumaDias += 31
    elif month == listaMeses[3, 5, 8, 10]:
        sumaDias += 30
    else:
        sumaDias += 28
        
    if (year%4) and not year%100!=0 or year%400:
        sumaDias += 366
    else:
        sumaDias += 365
    return sumaDias 
print(computeDaysInMonth(month, year))

# Ejercicio 4 

lista = [18, 4, 2008]

def getDayOfWeek (lista):
    
    

# Ejercicio 5

number1 = int(input("Choose one number:"))
number2 = int(input("Choose another number:"))
def powerlt (number1,number2):
    contador = 0
    while contador > number2:
        number1 *= number1
        contador += 1
    return number1
print(powerlt(number1, number2))


# Ejercicio 6

number = int(input("Choose one number:"))
def getNumberOfDigits (number):
    
    
    

# Ejercicio 7

number = int(input("Choose one number:"))

def isPrime (number):
    for i in range (2,number):
        if (number%i) == 0:
            mensaje = False
        else:
            mensaje = True 
    return mensaje
print(isPrime(number))

# Ejercicio 8

a = int(input("Pick one number"))
b = int(input("Pick one number"))
c = int(input("Pick one number"))

def solveSecondOrderEquation (a,b,c):



# Ejercicio 9

number = int(input("Choose one number:"))

def getPrimeDivisors (number):
    listaDiv = []
    for i in range(1, number+1):
        if number % i == 0:
            listaDiv.append(i)
    return listaDiv 
print(getPrimeDivisors(number))

'''

# Ejercicio 10

number1 = int(input("Pick one number"))
number2 = int(input("Pick another number"))

def isFriendNumber (number1, number2):
    listaDiv1 = []
    listaDiv2 = []
    for i in range(1,number1+1):
        if number1%i==0:
            listaDiv1.append(i)
    for x in range(1,number2+1):
        if number2%x==0:
            listaDiv2.append(x)
    for i in listaDiv1:

    
    


    