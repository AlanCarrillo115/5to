#Duplicados. 
#Dada una lista de números enteros, retorna True si al menos un valor aparece dos veces, y Falso si todos los elementos son distintos.

def repetidos(lista):
    Nd = set(lista)
    if len(Nd) != len(lista):
        return True
    else:
        return False

S1 = [9, 3, 5, 1, 1, 5]
print("Estado de duplicados en la lista: ",repetidos(S1))

S2 = [50,70,82,54,74,96]
print("Estado de duplicados en la lista: ",repetidos(S2))

#Carrillo Peña Alan Alberto 
#Grupo 952
#16/08/2023
