
'''
# Ejercicio 1
number = 8
def computeFactorial(n):
    if n > 0:
        suma = 1
        for i in range(1, n + 1):
            suma *= i
        return suma
    else:
        return None
    
print(computeFactorial(n))

# Ejercicio 2

year = 2020
def isLeapYear(year):
    leapYear = True
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leapYear = True
            else: 
                leapYear = False
        else: 
            leapYear = True
    else:
        leapYear = False
    return leapYear

print(isLeapYear(year))


# Ejercicio 3

dias = [31,28,31,30,31,30,31,31,30,31,30,31]
meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio","julio","agosto","septiembre", "octubre", "noviembre", "diciembre"]
month = "septiembre"
year = 2003


def computeDaysInMonth(month, year, meses, dias):
    if (month not in meses) or (type(year) != int):
        return -1
    leapYear = True
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                leapYear = True
            else: 
                leapYear = False
        else: 
            leapYear = True
    else:
        leapYear = False
    if leapYear == True:
        dias[1] = 29
    for n in range(len(meses)):
        if meses[n] == month:
            return dias[n]

print(computeDaysInMonth(month, year, meses, dias))

# Ejercicio 4

dia = 19
mes = 5
anyo = 2021
lista = [dia, mes, anyo]
def getDayOfWeek(lista):
    fecha = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]
    
    a = (14-mes)//12
    y = anyo-a
    m = mes + 12 * a - 2
    d = (dia + y + y/4 - y/100 + y/400 + (31*m)/12)%7
    return fecha[int(d)]
    
print(getDayOfWeek(list))


# Ejercicio 5

number1 = 7
number2 = 2
def powerlt (number1, number2):
    numero = 1
    contador = 0
    if type(number2)!=int:
        return number1**0
    else:
        while contador < number2:
            numero*=number1
            contador+=1
        return numero
print(powerlt(number1, number2))


# EJercicio 6

num = 12
numeros = ["0","1","2", "3", "4","5","6","7","8","9"]
def getNumberOfDigits(num, numeros):
    num1 = str(num)
    digitos = 0
    for i in num1:
        if i in numeros :
            digitos += 1
        else:
            pass
    return digitos
print(getNumberOfDigits(num, numeros))




# Ejercicio 7

num = 8

def isPrime (num):
    if type(num) != int:
        return None
    for i in range(2,num):
        if num%i == 0:
            return False
        else:
            return True
print(isPrime(num))

# Ejercicio 8

from math import sqrt
a = 1
b = 4
c = 3
def solveSecondOrderEquation(a,b,c):
    if not(((b**2)-4*a*c) > 0):
        return None
    else:
        x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)  
        x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)  
        print("Las soluciones de la ecuación son:")
    return x1,x2
print(solveSecondOrderEquation(a, b, c))

  

# Ejercicio 9

num = 24

def getPrimeDivisors (num):
    lista1 = []
    lista2 = []
    if type(num) != int:
        return None 
    for i in range (2,num):
        if num%i == 0:
            lista1.append(i)
    for x in lista1:
        if num % x == 0:
            lista2.append(x)
    return lista2
print(getPrimeDivisors(num))
            
            


    
# Ejercicio 10

num1 = 220
num2 = 284

def IsFriendNumber (num1, num2):
    sumaDiv = 0
    sumaDiv2 = 0
    for i in range(1, num1):
        if num1 % i == 0:
            sumaDiv += i
            
    for i in range(1, num2):
        if num2 % i == 0:
            sumaDiv2 += i
            
    if sumaDiv == num2 and sumaDiv2 == num1:
        return True
    else:
        return False 
print(IsFriendNumber(num1, num2))
    
                
''' 
    
    

                



        


    