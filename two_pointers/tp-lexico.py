#FIND THE NEXT LEXICOGRAPHICAL STRING ABC --> ACB >> BAC ...
#1234321 --> SIGUIENTE NUM ES 1241233 --> 1241323
#1234321 --> 1 2 3 4 3 2 1
#           SI SI SI NO NO 
#METODO MATEO PERSONAL NOOB


def ordenar(cadena):
    numCambiable = None
    siguiente = None

    
    for r in range(len(cadena)-1):
        if cadena[r] < cadena[r + 1]:
            numCambiable = r  

    if numCambiable is None:  # Si no encontramos un número intercambiable
        reversed_s = "".join(reversed(cadena))
        return reversed_s  # La cadena ya está en su mayor orden y la devolvemos del reves

    # Crear una lista de caracteres para modificar la cadena
    cadena = list(cadena)

    # Buscar el siguiente número más grande que el numCambiable .. como sabemos que el la string de la dcha no es incrementada, recorremos de dcha a izq y buscamos al primer caracter mayor que el pivote
    for r in range(len(cadena)-1,numCambiable+1,-1):
        if cadena[r]>cadena[numCambiable]:
            cadena[numCambiable],cadena[r]=cadena[r],cadena[numCambiable]
            break

    cadena[numCambiable + 1:] = sorted(cadena[numCambiable + 1:])    
    return "".join(cadena)  # Convertir lista de vuelta a string



# Ejemplo de uso



cadena = "abcedda"
print(ordenar(cadena)) 

