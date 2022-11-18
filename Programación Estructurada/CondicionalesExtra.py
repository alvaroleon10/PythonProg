'''
Created on 10 oct 2022

@author: leonr
'''
'''
# Ejercicio 1

nota = 97

if 0 < nota <= 49:
    print("Está suspenso, esfuércese más")
elif 50 <= nota <= 59:
    print("Su nota es un suficiente aunque puede sacar más")
elif 60 <= nota <= 69:
    print("Tiene un bien, un poco más de trabajo y llegará al notable")
elif 70 <= nota <= 89:
    print("Buen trabajo, obtiene un notable")
elif 90 <= nota <= 100:
    print("¡Enhorabuena, tiene un sobresaliente!")
else:
    print("ERROR")
    
print("------------")
'''
# Ejercicio 2

fecha = input("Introduzca una fecha en formato dd-mm-yyyy: ")
hemisferio = input("¿Hemisferio norte o sur? N/S: ").upper()

dia = int(fecha[0:2])
mes = int(fecha[3:5])
año = int(fecha[6:10])

if (mes==10 or mes==11) or (23<=dia<=31 and mes==9) or (mes==12 and 1<=dia<=21):
    if hemisferio == "NORTE":
        print("Es otoño")
    elif hemisferio == "SUR":
        print("Es primavera")
        
if (mes==1 or mes==2) or (21<=dia<=31 and mes==12) or (mes==3 and 1<=dia<=21):
    if hemisferio == "NORTE":
        print("Es verano")
    elif hemisferio == "SUR":
        print("Es invierno")
     

    
'''    
print("------------")


# Ejercicio 3

diaInicio = 1
mesInicio = 1
diaFinal = 28
mesFinal = 11
año = 2003
bisiesto = año%4 == 0 and año%100 != 0 or año%400 == 0

if bisiesto:
    diasMes = [0,31,29,31,30,31,30,31,31,30,31,30,31]
else:
    diasMes = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    
llevayear = 1
total = 1
i = mesInicio

if i < mesFinal:
    while i < mesFinal:
        llevayear = llevayear + diasMes [i]
        i = i + 1
    total = diaFinal + llevayear - 1
    print(total)
else:
    total = diaFinal - diaInicio
    print(total)



'''


    
        
        
    







