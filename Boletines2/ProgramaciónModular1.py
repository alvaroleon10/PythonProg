'''
Created on 4 nov 2022

@author: leonr
'''


'''
# Ejercicio 1

from random import randint
lista = []
for i in range(10):    
    lista.append(randint(0,1000))
print(lista)

#A)
    
def obtenerMayor (lista):
    mayor = lista [0]
    for x in range(len(lista)):
        if lista[x] > mayor:
            mayor = lista[x]
    return mayor


#B)  
def obtenerMenor (lista):
    menor = lista [0]
    for x in range(len(lista)):
        if lista[x] < menor:
            menor = lista[x]
    return menor
         

#C)
def obtenerSuma (lista):
    suma = 0
    for x in range(len(lista)):
        suma += lista[x]
    return suma
#D)
def obtenerMedia (lista):
    suma = 0
    for x in range(len(lista)):
        suma += lista[x]
        media = suma/len(lista)
    return media

#E)
ns = int(input("Introduce un número a sustituir:"))
vc = int(input("Introduce un número para cambiar por el anterior:"))
def sustituirElemento (lista, ns, vc):
    for i in range(len(lista)):
        if ns == lista[i]:
            lista[i] = vc
    return lista

#F)
print(obtenerMayor(lista))
print(obtenerMenor(lista))
print(obtenerSuma(lista))
print (obtenerMedia(lista))
print (sustituirElemento(lista, ns, vc))

print("---------")

# Ejercicio 2

lista = [1, 3, 5, 7]

def desplazar (lista):
    escribe = lista[0]
    guarda = 0
    for i in range(len(lista)):
        if i == len(lista)-1:
            lista[0] = escribe
        else:
            guarda = lista[(i+1)]
            lista[(i+1)] = escribe
            escribe = guarda       
    return (lista)

print(desplazar(lista))



# Ejercicio 3

dd, mm, yyyy = 1, 1, 2022

def es_bisiesto (year):
    bisiesto = year % 4 == 0 and (year % 100 != 0 or year % 4 == 0)
    return (bisiesto)
def transformar_formato_largo (dd, mm, yyyy):
    
    nombre_meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    dias_maximo_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    
    if 1 <= mm <= 12 and((1<= dd <= dias_maximo_meses[mm-1]) or (es_bisiesto (yyyy) and 1<= dd <= 29 and mm == 2)):
        
        mensaje = f'{dd} de {nombre_meses[mm-1]} de {yyyy}'
    
    else:
        mensaje = "La fecha introducida no es válida."
    
    return mensaje

day = int(input("Introduce el día:"))
month = int(input("Introduce el mes:"))
year = int(input("Introduce el año:"))

while day >= 0:
    print(transformar_formato_largo(day, month, year))
    
    day = int(input("Introduce el día:"))
    month = int(input("Introduce el mes:"))
    year = int(input("Introduce el año:"))

   
# Ejercicio 4

lista = []

numero = int(input("Introduce un número (negativo para finalizar):"))
mayor = numero  
while numero > 0:
    if numero % 2 == 0:
        lista.append(numero)
    if numero > mayor:
        mayor = numero
    numero = int(input("Introduce un número (negativo para finalizar):"))
def calcularPares (lista):
    return lista
def mostrarMayor (numero):
    return mayor            
  

print(calcularPares(lista))
print(mostrarMayor(numero))

# Ejercicio 5

lista = ['Di', 'buen', 'día', 'a', 'papá']
def reverse (lista):
    x = 0
    while x < len(lista):
        lista2 = []
        lista2.append(len(lista[x] - 1))
        x += 1
        return lista2
print(reverse(lista))
    


 
# Ejercicio 6
lista = [1, 4, 8, 12, 19]

def estaOrdenada (lista):
    esta_ordenado = True
    for x in range (len(lista)-1):
        if not (lista[x] <= lista [x+1]):
            esta_ordenado = False
    return esta_ordenado
print(estaOrdenada(lista))
            
        
    

# Ejercicio 7

fichas1 = [3,4]
fichas2 =[2,5]

def encajan (fichas1, fichas2):
    mensaje = "No es correcto"
    if fichas1[0] == fichas2[0] or fichas1[0] == fichas2[1] or fichas1[1] == fichas2[0] or fichas1[1] == fichas2[1]:
        mensaje == "Es correcto"
    return mensaje
print (encajan(fichas1, fichas2))    



# Ejercicio 8
def es_numero_primo (n):
    es_primo = True 
    
    for i in range (2,n):
        if n%i==0:
            es_primo = False 
    return es_primo

lista = [2, 4, 6, 11, 13, 5, 14]
primos = []
for elemento in lista:
    if es_numero_primo(elemento):
        primos.append(elemento)
        
print(primos)
    

# Ejercicio 9

lista = [1, 6, 19, 23, 9, 14]
k = 10
def devolverMenores (lista):
    x = 0
    listaMenores = []
    while x < len(lista):
        if lista[x] < k:
            listaMenores.append(lista[x])
        x += 1
    return listaMenores
print(devolverMenores(lista))

def devolverMayores (lista):
    x = 0
    listaMayores = []
    while x < len(lista):
        if lista[x] > k:
            listaMayores.append(lista[x])
        x += 1
    return listaMayores
print(devolverMayores(lista))

def devolverMultiplos (lista):
    x = 0
    listaMultiplos = []
    while x < len(lista):
        if lista[x] % k == 0:
            listaMultiplos.append(lista[x])
        x += 1
    return listaMultiplos
print(devolverMultiplos(lista))

# Ejercicio 10

numero = "101101B"

def conversor(numero):
    lista2 = []
    if numero[-1] == "B":
        numero = numero[0:len(numero)-1]
        for i in numero:
            if int(i) > 1:
                assert Exception("Los numeros binarios no son mayores que 1")
        n = 0
        for n in numero:
            lista2.append(n)
        x = 0
        y = len(lista2)-1
        producto = 0
        while x < len(lista2):
            producto += int(lista2[x]) * (2 ** y)
            x += 1
            y -= 1
        return producto
    if numero [-1] == "D":
        numero = numero[0:len(numero)-1]
        for i in numero:
            if not (0<=int(i)<9):
                assert Exception("La base decimal debe ser entre 0 y 9")
        numero = int(numero)
        binario = 0
        multiplicador = 1
        while numero != 0:
            binario += numero%2 * multiplicador
            numero //= 2
            multiplicador *= 10
        return binario
print (conversor(numero))

# Ejercicio 11

lista1 = [1, 4, 9, 1, 16]
lista2 = [6, 8, 4, 9, 1]

def intersect (lista1, lista2):
    nuevaLista = []
    for i in lista1:
        if i in lista2:
            nuevaLista.append(i)
    return nuevaLista
       
print(intersect(lista1, lista2))
# Ejercicio 12

lista1 = [3, 7, 9, 12, 19]
lista2 = [5, 3, 6, 12, 8]

def unionListas (lista1, lista2):
    nuevaLista = []
    for i in lista2:
        nuevaLista.append(i)
    for i in lista1:
        if i not in lista2:
            nuevaLista.append(i)
        
    return nuevaLista
            
print(unionListas(lista1, lista2))


# Ejercicio 13
listaNombres = ['Mario', 'Alejandro', 'Álvaro', 'José', 'Marta']
letra = 'M'

def devolverNombres (listaNombres):
    nuevaLista = []
    for i in listaNombres:
        if i[0]== letra:
            nuevaLista.append(i)
    return nuevaLista
            
print (devolverNombres(listaNombres))

    

# Ejercicio 14

lista1 = [2, 4, 5, 7, 8, 10]
lista2 = [5, 19, 6, 38]
lista3 = [5, 0, 12, 52, 67, 33, 10]

def medirCadena (lista1, lista2, lista3):
    x = 0
    while x < len(lista1) and x < len(lista2) and x < len(lista3):
        if len(lista2) < len(lista1) > len(lista3):
            print("Lista 1 es la cadena más larga")
        elif len(lista1) < len(lista2) > len(lista3):
            print("Lista 2 es la cadena más larga")
        else:
            print("Lista 3 es la cadena más larga")
        x += 1
        
'''           
            
        
        
    


    

