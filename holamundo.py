# Esta es mi primera aplicación en python
print ("Hola mundo")
print("Bienvenido a Python")
print("------------------------")
print("Variables en Python")

# Tipos de datos en variablen
nombre = "Esdras"  # Cadena
edad = 24          # Numérico entero
correo = "esdras@uob.edu.mx" # Cadena
promedio = 8.7     # Numérico de punto flotante
beca = False       # Booleano

print("Nombre :",nombre)
print("Tipo de dato de la variable Nombre",type(nombre))

print("Edad :",edad)
print("Tipo de dato de la variable edad",type(edad))

print("Correo :",correo)
print("Tipo de dato de la variable correo",type(correo))

print("Promedio :",promedio)
print("Beca :",beca)


#Operadores: +, -, *, /, %(residuo), // (division entera), ** (exponente)

potencia2 = 2**10
residuo = 105 % 3
print(potencia2)
print(residuo)



edad = 14          # Numérico entero


#condiciones if-else (operadores ==, >, <, >=, <=, !)

if edad >= 18:
    print("Puede votar")
    print("Espero verte este 6 de junio")
else:
    print("No puede votar")
    print("Tan pronto tengas la edad; solicita tu INE")
    
    

# Lista en python
# Es un arreglo de elementos del cual la lista puede ser actualizada

alumnos = ["Valentin", "Rosendo", "Valentin2", "Lilia", "Dani", "Alan", "Jonathan"]
print(type(alumnos))
print(alumnos)




#Imprimir elementos individuales, con el indice iniciando desde 0
print(alumnos[0])
print(alumnos[3])
print(alumnos[4])
print(alumnos[5])
print("--------------------------------------")

#Imprimir los elementos en un ciclo, recorrer la lista


for elemento in alumnos:
    print(elemento)
    
    
print("--------------------------------------")

#Imprimir los elementos en un ciclo, recorrer la lista

i = 0
for elemento in alumnos:
    print(i, ":", elemento)
    i=i+1
    
    
print("--------------------------------------")

#Imprimir los elementos en un ciclo, recorrer la lista


for i in range(100,110, 2):
    print(i)
   

#Traer el juego del gato en python, usando una lista para almacenar las posiciones de los jugadores
#version 1 : 2 jugadores
#version 2 : Jugador vs maquina


#While

print("While")
print("Elementos de la lista2")
lista2=["pantalla","teclado", "bocinas", "mouse", "usb", "cd", "quemador", "impresora", "microfono", "webcan"]
print(lista2)
i=0

while i<len(lista2):
    print(i, ":", lista2[i])
    i=i+1
    
    
# Acceder a los elementos de la lista2 por medio de indices
print("La lista2 tiene ", len(lista2), "elementos")

print("Todos los elementos 0-9", lista2[0:10])
print("Elementos del 2-6", lista2[2:7])
print("Elementos desde el 5-6", lista2[5:])
print("Elementos desde el 5-6", lista2[:3])


# Realizar los siguientes ejercicios
# 1. Extraer 'mouse', 'usb', 'cd', 'quemador', 'impresora' con indices
# 2. extraer   'mouse', 'usb', 'cd', 'quemador', 'impresora', 'microfono', 'webcam'
# 3. extraer 'pantalla', 'teclado', 'bocinas', 'mouse', 'usb', 'cd', 'quemador', 'impresora'
# 4. Programar para extraer 'pantalla', 'bocinas',  'usb', 'quemador', 'microfono'

# 5. Programar para extrar de la lista2, la sublista equipo = ["mouse", "cd", "microfono", "cargador"], que aparezca su numero de indice

#   Resultado esperado:
#   Indice 3 : mouse
#   Indice 5 : cd
#   Indice 8 : microfono
#   Cargador NO encontrado en lista2



print("\n")
print("\n")

print("1", lista2[3:8])
print("_________________________________")
print("2", lista2[3:])
print("_________________________________")
print("3", lista2[0:8])
print("_________________________________")
i=0
print("4 =")
while i<len(lista2):
    print(lista2[i],end=",  ")
    i=i+2
print("\n")



lista2=["pantalla","teclado", "bocinas", "mouse", "usb", "cd", "quemador", "impresora", "microfono", "webcan"]
equipo = ["mouse", "cd", "microfono", "cargador"]


print("5")
print("_________________________________")
equipo = ["mouse", "cd", "microfono", "cargador"]
for producto in equipo:
    if producto in lista2:
        print(f"Indice {lista2.index(producto)}: {producto}")
    else:
        print(f"{producto} NO encontrado en lista2")




