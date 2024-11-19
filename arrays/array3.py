import numpy as np

# 1. Crear dos matrices de 2x3
matriz_a = np.array([[1, 2, 3], [4, 5, 6]])
matriz_b = np.array([[6, 5, 4], [3, 2, 1]])

print("Matriz A:\n", matriz_a)
print("Matriz B:\n", matriz_b)

# 2. Suma y resta de matrices
suma = matriz_a + matriz_b
print("Suma de A y B:\n", suma)

resta = matriz_a - matriz_b
print("Resta de A y B:\n", resta)

# 3. Multiplicación elemento a elemento
producto_elemento = matriz_a * matriz_b
print("Multiplicación elemento a elemento de A y B:\n", producto_elemento)

# 4. Transponer la matriz A
matriz_a_transpuesta = matriz_a.T
print("Transpuesta de A:\n", matriz_a_transpuesta)

# 5. Producto de matrices (multiplicación de matrices)
matriz_c = np.array([[1, 2], [3, 4], [5, 6]])
producto_matrices = np.dot(matriz_a, matriz_c)
print("Producto de matrices A y C:\n", producto_matrices)