import numpy as np

lista = [1,2,3,4]
n1 = np.array(lista)
print(n1)
print(type(n1))
print(n1*2)

calificaciones =[[80,90,100],[85,60,78],[50,100,70],[75,85,95]]

cn = np.array(calificaciones)
print(cn.max(axis=1))

print(cn.ndim)
print(cn.shape)
print(cn.size)
print(cn.dtype)

print(cn[0,1])

print(cn.transpose())

"""
    x + 2y = 1
    3x + 5y = 2
"""
ecuaciones = np.array([[1,2],[3,5]])
resultados = np.array([1,2])
res = np.linalg.solve(ecuaciones, resultados)
print(res)