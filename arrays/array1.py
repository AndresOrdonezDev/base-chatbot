import numpy as np

# Crear un array de números del 1 al 10
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Array original:", arr)

# Sumar 5 a cada elemento
arr_plus_5 = arr + 5
print("Array después de sumar 5 a cada elemento:", arr_plus_5)

# Calcular el cuadrado de cada elemento
arr_squared = arr ** 2
print("Array con cada elemento al cuadrado:", arr_squared)

# Sumar todos los elementos
suma_total = arr.sum()
print("Suma de todos los elementos:", suma_total)

# Calcular el promedio
promedio = arr.mean()
print("Promedio de los elementos:", promedio)

