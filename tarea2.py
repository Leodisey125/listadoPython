# Definir la cadena larga
cadenaLarga = """
Hola Alan Leonides Canul
"""

# Dividir la cadena en párrafos
parrafos = cadenaLarga.split("\n\n")

# Inicializar variables para el total
total_caracteres = 0
total_letras = 0
total_vocales = 0
total_vocales_a = 0
total_vocales_e = 0
total_vocales_i = 0
total_vocales_o = 0
total_vocales_u = 0
total_espacios = 0
total_comas = 0
total_palabras = 0

# Recorrer cada párrafo
for parrafo in parrafos:
    # Contar caracteres
    total_caracteres += len(parrafo)
    
    # Contar letras y vocales
    for letra in parrafo:
        if letra.isalpha():
            total_letras += 1
            if letra.lower() in "aeiou":
                total_vocales += 1
                if letra.lower() == "a":
                    total_vocales_a += 1
                elif letra.lower() == "e":
                    total_vocales_e += 1
                elif letra.lower() == "i":
                    total_vocales_i += 1
                elif letra.lower() == "o":
                    total_vocales_o += 1
                elif letra.lower() == "u":
                    total_vocales_u += 1
                    
    # Contar espacios y comas
    total_espacios += parrafo.count(" ")
    total_comas += parrafo.count(",")
    
    # Contar palabras
    palabras = parrafo.split()
    total_palabras += len(palabras)

# Imprimir resumen de estadísticas
print("Resumen de estadisticas de los parrafos:")
print(f"Total de caracteres: {total_caracteres}")
print(f"Total de letras (incluyendo vocales): {total_letras}")
print(f"Total de vocales: {total_vocales}")
print(f"Total de vocales a: {total_vocales_a}")
print(f"Total de vocales e: {total_vocales_e}")
print(f"Total de vocales i: {total_vocales_i}")
print(f"Total de vocales o: {total_vocales_o}")
print(f"Total de vocales u: {total_vocales_u}")
print(f"Total de espacios: {total_espacios}")
print(f"Total de comas: {total_comas}")
print(f"Total de palabras: {total_palabras}")
