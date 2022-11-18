'''
Created on 21 oct 2022

@author: leonr
'''
peso = int(input("Introduzca su peso:"))
edad = int(input("Inserte su edad:"))
vida = input("¿Qué tipo de vida lleva? (Sedentaria, Activa, Muy activa):").upper

while peso > 500 or 0 > edad > 110  and vida != "SEDENTARIA" and vida != "ACTIVA" and vida != "MUY ACTIVA":
    print("DATOS INCORRECTOS, PRUEBE OTRA VEZ")
    peso = int(input("Introduzca su peso:"))
    edad = int(input("Inserte su edad:"))
    vida = input("¿Qué tipo de vida lleva? (Sedentaria, Activa, Muy activa):").upper
    
if edad > 70 and vida == "Sedentaria":
    print("Se recomienda ir al médico")
elif peso > 100:
    print("Se recomienda ir al médico")
elif peso > 74.4 and edad > 50:
    print("Se recomienda ir al médico")
else:
    print("No es urgente que acuda al médico si no tiene problemas de salud")