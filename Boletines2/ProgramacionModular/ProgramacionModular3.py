'''
# Ejercicio 1

character = "Esternocleidomastoideo".upper()
z = input("Insert a letter:").upper()

def charactersInString (character, z):
    times = 0
    for x in character:
        if x == z:
            times += 1
    return times
print(charactersInString(character, z))
# Ejercicio 2

parameter = "INfOrMAtiCa"

def lowCaseInString (parameter):
    times = 0
    for x in parameter:
        if str.islower(x):
            times+=1
    return times 
print(lowCaseInString(parameter))
            

  

# Ejercicio 3

parameter = "INfOrMAtiCa"

def upperCaseInString (parameter):
    times = 0
    for x in parameter:
        if str.isupper(x):
            times+=1
    return times 
print(upperCaseInString(parameter))


# Ejercicio 4 

parameter = "RM1902"

def numberInString (parameter):
    times = 0
    for i in parameter:
        for x in range(0,10):
            x = str(x)
            if i == x:
                times+=1
    return times 
print(numberInString(parameter))




# Ejercicio 5 

parameter = "Anilinas".upper()

def palindrome (parameter):
    reverse = ""
    for x in parameter:
        reverse = x + reverse
    if reverse == parameter:
        return True 
    else:
        return False 
print(palindrome(parameter))

     

# Ejercicio 6

palabra = "shybaoxlna"
a_buscar = "hola"

def buscarPalabra (palabra, a_buscar):
    for x in palabra:
        if x in a_buscar:
            return True 
        else:
            return False 
print(buscarPalabra(palabra, a_buscar))


# Ejercicio 7

frase1 = "Mi nombre es Godofredo"
frase2 = "Godofredo"
frase3 = "Álvaro"
nuevaFrase = ""

def cambiarElementos (frase1,frase2,frase3):
    if frase2 in frase1:
        nuevaFrase = frase1[0:5]
    return nuevaFrase 
print(cambiarElementos(frase1, frase2, frase3))
    
        




# Ejercicio 8 

element = "Aterrizaje".lower()
vocales = ["a", "e", "i", "o", "u"]

def contarVocales (element):
    times = 0
    listaVocales = []
    for x in element:
        if x in vocales and x not in listaVocales:
            times+=1
            listaVocales.append(x)
    return times
print(contarVocales(element)) 


# Ejercicio 9

element = "Jugador de baloncesto".lower()
vocales = ["a", "e", "i", "o", "u"]
consonantes = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "ñ", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

def devolverCadena (element):
    nuevoElemento = ""
    for x in element:
        if x in consonantes:
            nuevoElemento += x
    for i in element:
        if i in vocales:
            nuevoElemento += i
    return nuevoElemento 
print(devolverCadena(element))
            


# Ejercicio 10

frase = "España ganará el mundial "
def contarPalabras (frase):
    palabras = 0
    for x in (frase):
        if x == " ":
            palabras+=1
    return palabras
print(contarPalabras(frase))
    
'''    
    
    


            
    