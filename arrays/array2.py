import numpy as np
# Crear un array de 20 números aleatorios entre 1 y 100
random_array = np.random.randint(1, 101, 20)
print("Array de números aleatorios:", random_array)

# Calcular el máximo, mínimo y promedio
max_value = random_array.max()
min_value = random_array.min()
average = random_array.mean()
print("Valor máximo:", max_value)
print("Valor mínimo:", min_value)
print("Promedio:", average)

# Multiplicar cada elemento por 2
doubled_array = random_array * 2
print("Array con cada elemento multiplicado por 2:", doubled_array)
