# Encriptar. Diseñe una función encripta(s, clave), que reciba un string s con un mensaje y un string
# con una clave de codificación, y retorne el mensaje codificado según la clave leída. Los signos de
# puntuación y dígitos que aparecen en el mensaje deben conservarse sin cambios.

import random


def maquina_de_turing(s, clave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_mayusculas = alfabeto.upper()
    resultado = ""

    for i in s:
        if i.isalpha():
            if i.islower():
                indice = (alfabeto.index(i) + int(clave)) % 26
                resultado += alfabeto[indice]
            else:
                indice = (alfabeto_mayusculas.index(i) + int(clave)) % 26
                resultado += alfabeto_mayusculas[indice]
        else:
            resultado += i
    return resultado


r = random.randint(0, 26)
mensaje = "La base de datos 8 ha sido actualizada en base a la normativa 935"
clave = r
Crip = maquina_de_turing(mensaje, clave)
print(Crip)