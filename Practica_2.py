#Suma de dos números. Dado una lista de números enteros y un valor entero (target),
#retorna el índice de los dos números que sumados sean igual al target. Debe asumir
#que existe siempre una única solución, y que los elementos no se pueden usar dos veces.
#Debes retornar una tupla con los índices.

import random

def sum(n, target):
    indices = {}
    for i, num in enumerate(n):
        complemento = target - num
        if complemento in indices:
            return (indices[complemento], i)
        indices[num] = i
    return ("Sin complemento")

r1 = random.randint(1, 15)
r2 = random.randint(1, 15)
r3 = random.randint(1, 15)
r4 = random.randint(1, 15)
print ("Numeros: ", r1,r2,r3,r4)
n = [r1, r2, r3, r4]
target = 9
print("Indices: ", sum(n, target))

#Carrillo Peña Alan Alberto
#Grupo 952
#16/08/2023