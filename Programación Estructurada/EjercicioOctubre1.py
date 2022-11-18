'''
Created on 4 oct 2022

@author: leonr
'''

# Ejercicio JacaFitness

print("Bienvenido a Jacafitness")
horario = int(input("Por favor indique cual sería su hora de entrenamiento:"))
dia = input("Por último, indique qué dia de la semana vendrá:")
dias = dia.upper()

if (12 <= horario <= 14 or 16 <= horario <= 20 or 20 <= horario <= 22) and (dias == "LUNES" or dias == "MARTES" or dias == "MIÉRCOLES" or dias == "JUEVES" or dias == "VIERNES"):
    
    if 12 <= horario <= 14 and dias == "LUNES" or dias == "MIÉRCOLES" or dias == "VIERNES":
        print("Podrá asistir a la clase de spinning")
    
    elif 16 <= horario <= 20 and dias == "LUNES" or dias == "MIÉRCOLES" or dias == "VIERNES":
        print("Podrá asistir a nuestra clase de yoga")
    
    elif 20 <= horario <= 22 and dias == "LUNES" or dias == "MARTES" or dias == "MIÉRCOLES" or dias == "JUEVES" or dias =="VIERNES":
        print("Podrá asistir a la clase de Body Combat")
    
    elif 12 <= horario <= 14 and dias == "MARTES" or dias == "JUEVES":
        print("Podrá asistir a la clase de yoga")
    
    elif 16 <= horario <= 20 and dias == "MARTES" or dias =="JUEVES":
        print("Podrá asistir a la clase de spinning")
    
else:
    print("Los datos introducidos son erróneos, sentimos las molestias")
        
    
