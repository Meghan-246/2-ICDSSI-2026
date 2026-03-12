"""
Fecha   :10/04/26
Grupo   :2I
Nombre  :Meghan lopez peña

Encontrar que elementos de una lista suman cero
"""

# clase de numeros que sumen ceros

class SumaCero:

    def encontrar(self, lista):
        for i in range(len(lista)):
            for j in range(i+1, len(lista)):
                for k in range(j+1, len(lista)):
                    if lista[i] + lista[j] + lista[k] == 0:
                        return lista[i], lista[j], lista[k]

# Ejemplo
numeros = [2, -3, 1, 4, -1]

obj = SumaCero()
resultado = obj.encontrar(numeros)

print("Numeros que suman 0:", resultado)