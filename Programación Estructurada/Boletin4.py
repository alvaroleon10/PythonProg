'''
Created on 26 sept 2022

@author: leonr
'''
'''
# Ejercicio 1

cateto1 = 4
cateto2 = 3
hipotenusa = ((cateto1 ** 2)+(cateto2 ** 2))**(1/2)

print(hipotenusa)

print("----------")
# Ejercicio 2

gradosF = int(input("¿A cuántos grados Farenheit se encuentra?:"))
gradosC = ((gradosF - 32) * 5 / 9)

print("Son " + str(gradosC) + " grados Celsius")

print("----------")

# Ejercicio 3

num1 = int(input("Introduzca un número:"))
num2 = int(input("Introduzca un segundo número:"))
num3 = int(input("Tercer y último número:"))

print((num1 + num2 + num3)/3)

print("--------------")

# Ejercicio 4

totalcompra = int(input("¿Cual ha sido el precio total de su compra?:"))

print(totalcompra - ((totalcompra * 15)/100))



print("-------------")

# Ejercicio 5

num1 = int(input("Introduzca un número:"))
num2 = int(input("Introduzca otro número:"))

distancia = num1 - num2

print(abs(distancia))


print("----------")

# Ejercicio 6

x1 = int(input("Introduzca un número:"))
y1 = int(input("Introduzca un número:"))
x2 = int(input("Introduzca un número:"))
y2 = int(input("Introduzca un número:"))

distancia = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

print(distancia)


print("------------")
# Ejercicio 7

numero = int(input("Introduzca un número:"))
             
raizCuadrada = numero**(1/2)
raizCubica = numero** (1/3)

print("La raíz cuadrada de su número es " + str(raizCuadrada) + " y la cúbica es " + str(raizCubica))


print("----------")
# Ejercicio 8

dosEuros = int(input("¿Cuántas monedas de 2 euros tiene?:")) * 2
unEuro = int(input("¿Cuántas monedas de 1 euro tiene?:"))
cincuentacent = int(input("Cuántas monedas de 50 céntimos tiene?:")) *(1/2)
veintecent = int(input("Cuántas monedas de 20 céntimos tiene?:")) *(1/5)
diezcent = int(input("¿Cuántas monedas de 10 céntimos tiene?:")) *(1/10)

total = dosEuros + unEuro + cincuentacent + veintecent + diezcent
euros = int(total)
centimos = (total - euros) * 100
print("Tiene " + str(euros) + " euros y " + str(int(centimos)) + " centimos") 


print("----------")
# Ejercicio 9

base = int(input("Inserte un número:"))
exponente = int(input("Inserte otro número:"))
potencia = base ** abs(exponente)

if exponente > 0:
    print(potencia)
    
elif exponente == 0:
    print("El resultado es 1")
    
else:
    print(1/potencia)


print("---------")

# Ejercicio 10
ladoA = int(input("Introduzca un número:"))
ladoB = int(input("Introduzca un número:"))
ladoC = int(input("Introduzca un número:"))

pitagoras = (ladoA**2 + ladoB**2) == ladoC**2
isosceles = ladoA == ladoB or ladoB == ladoC or ladoA == ladoC
equilatero = ladoA == ladoB == ladoC

if pitagoras:
    print("Es un triángulo rectángulo")
    
elif isosceles:
    print("Es un triángulo isósceles")
    
elif equilatero:
    print("Es un triángulo equilátero")

else:
    print("Es un triángulo escaleno")


print("-------")

# Ejercicio 11

año = int(input("Escriba un año:"))
bisiesto = año%4 == 0 and año%400

if bisiesto:
    print("Es un año bisiesto")
else: 
    print("No es un año bisiesto")

print("------")

# Ejercicio 12

tipo = input("¿De qué tipo es la uva?:")
tipomayus = tipo.upper()
tamaño = int(input("¿Qué tamaño tiene?:"))


if tipo == "A" and tamaño == 1:
    print("Se le añaden 20 céntimos al precio inicial")

elif tipomayus == "A" and tamaño == 2:
    print("Se le añaden 30 céntimos al precio inicial")

elif tipomayus == "B" and tamaño == 1:
    print("Se rebajan 30 céntimos al precio inicial")
    
else:
    print("Se rebajan 50 céntimos al precio inicial")
    

print("--------")

# Ejercicio 13

alumnos = int(input("¿Cuántos alumnos asistirán al viaje?:"))

if alumnos > 100:
    print("El precio por alumno es de 65 euros")
    
elif 50 <= alumnos <= 99:
    print("El precio por alumno es de 70 euros")        

elif 30 <= alumnos <= 49:
    print("El precio por alumno es de 95 euros")
    
elif 30 < alumnos >= 1:
    print("El costo de la renta del autobús es de 4000 euros")

else:
    print("Número de alumnos erróneo")   
    

print("-----------")

# Ejercicio 14

minuto = int(input("¿Cuánto ha durado la llamada?:"))
dia1 = input("¿Qué día es?:")
dia = dia1.upper()
#turno = input("¿Es por la mañana o de tarde?:")
restante = minuto - 5
restante1 = restante - 3
restante2 = restante1 - 2

if minuto < 5:
    print(minuto*1)
    
elif 5 < minuto < 9:
    print((5 * 1) + (restante * 0.80))
    
elif 8 < minuto < 11:
    print((5 * 1) + (3 * 0.80) + (restante1 * 0.70))
    
elif 10 < minuto:
    print((5 * 1) + (3 * 0.80) + (2 * 0.70) + (restante2 * 0.50))
    
else:
    print("ERROR")
    

print("---------")

# Ejercicio 15

dia = int(input("Número de un día de la semana:"))

if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miércoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sábado")
elif dia == 7:
    print("Domingo")
else:
    print("ERROR")   

print("----------")

# Ejercicio 16

mes = int(input("Número de un mes del año:"))

if mes == 1:
    print("Enero")
elif mes== 2:
    print("Febrero")
elif mes == 3:
    print("Marzo")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Mayo")
elif mes == 6:
    print("Junio")
elif mes == 7:
    print("Julio")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Septiembre")
elif mes == 10:
    print("Octubre")
elif mes == 11:
    print("Noviembre")
elif mes == 12:
    print("Diciembre")
else:
    print("ERROR")
    


print("----------")

'''  