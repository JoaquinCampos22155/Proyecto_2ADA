import time
import matplotlib.pyplot as plt

# Lista de arreglos predefinidos
arrays_20 = [
    [2, 10, 18, 4, 11, 0, 19, 7, 1, 3, 12, 13, 6, 15, 8, 20, 14, 16, 5, 9],
    [0, 5, 17, 3, 8, 12, 14, 6, 1, 19, 11, 10, 2, 20, 7, 18, 15, 4, 13, 16],
    [7, 8, 20, 5, 11, 14, 2, 6, 10, 13, 4, 0, 3, 15, 1, 9, 18, 17, 12, 16],
    [10, 12, 2, 14, 5, 7, 8, 6, 0, 20, 19, 13, 1, 11, 18, 3, 4, 16, 15, 9],
    [3, 1, 6, 8, 17, 11, 19, 0, 2, 10, 5, 15, 12, 13, 14, 7, 4, 18, 16, 20],
    [4, 20, 2, 13, 10, 5, 8, 6, 11, 14, 17, 3, 7, 0, 12, 9, 15, 1, 19, 16],
    [18, 7, 11, 9, 2, 13, 16, 12, 0, 5, 6, 1, 4, 10, 8, 14, 15, 17, 3, 20],
    [6, 3, 15, 11, 14, 0, 4, 18, 9, 13, 8, 12, 7, 1, 5, 2, 10, 20, 17, 16],
    [5, 13, 3, 17, 0, 6, 11, 19, 9, 15, 2, 8, 10, 1, 4, 14, 12, 7, 20, 16],
    [1, 0, 3, 6, 2, 7, 9, 5, 10, 13, 4, 11, 8, 12, 15, 14, 20, 16, 17, 18],
    [7, 2, 8, 0, 10, 3, 12, 4, 14, 1, 9, 6, 5, 13, 11, 15, 17, 18, 20, 16],
    [11, 9, 13, 10, 12, 8, 7, 3, 6, 1, 2, 0, 4, 5, 14, 15, 20, 18, 17, 16],
    [6, 2, 0, 10, 1, 4, 5, 7, 12, 13, 9, 8, 3, 11, 14, 20, 19, 15, 16, 17],
    [9, 1, 4, 7, 2, 3, 0, 6, 10, 13, 11, 12, 8, 5, 14, 15, 19, 17, 16, 20],
    [5, 6, 1, 4, 0, 2, 8, 3, 7, 9, 10, 11, 12, 13, 14, 17, 16, 18, 20, 15],
    [3, 0, 1, 2, 6, 8, 4, 7, 5, 9, 11, 10, 12, 14, 13, 15, 16, 19, 18, 20],
    [2, 1, 0, 3, 4, 6, 5, 8, 7, 9, 10, 12, 11, 13, 14, 17, 16, 15, 18, 20],
    [0, 2, 1, 4, 3, 5, 6, 9, 7, 8, 10, 11, 12, 14, 13, 15, 17, 18, 16, 20],
    [1, 3, 2, 0, 4, 5, 6, 8, 9, 7, 10, 11, 13, 12, 14, 15, 17, 16, 18, 20],
    [4, 2, 0, 1, 3, 5, 6, 7, 9, 8, 10, 11, 13, 12, 14, 16, 15, 18, 17, 20],
    [0, 1, 2, 3, 5, 4, 6, 8, 7, 9, 10, 11, 12, 13, 14, 15, 17, 16, 19, 20],
    [1, 0, 2, 3, 5, 4, 6, 8, 7, 10, 9, 11, 12, 13, 15, 14, 17, 16, 18, 20],
    [3, 2, 1, 0, 4, 5, 6, 8, 7, 9, 10, 11, 13, 12, 14, 16, 15, 18, 17, 20],
    [2, 3, 0, 1, 4, 6, 5, 7, 9, 8, 10, 11, 13, 12, 14, 15, 17, 16, 18, 20],
    [1, 2, 3, 0, 4, 5, 6, 8, 7, 9, 10, 11, 13, 12, 14, 15, 17, 16, 18, 20],
    [4, 5, 6, 7, 8, 9, 10, 11, 13, 12, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3],
    [6, 5, 4, 7, 8, 9, 10, 11, 13, 12, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
    [10, 12, 14, 16, 18, 20, 0, 2, 4, 6, 8, 1, 3, 5, 7, 9, 11, 13, 15, 17]
]

# Algoritmo Subset Sum con memoización
def subset_sum_memo(arr, T):
    memo = {}
    def dp(i, target):
        if target == 0:
            return True
        if i < 0 or target < 0:
            return False
        if (i, target) in memo:
            return memo[(i, target)]
        include = dp(i - 1, target - arr[i]) if arr[i] <= target else False
        exclude = dp(i - 1, target)
        memo[(i, target)] = include or exclude
        return memo[(i, target)]
    return dp(len(arr) - 1, T)

# T fijo
T = 195

execution_times_ms = []
theoretical_O = []

print("Índice\tTiempo (ms)\tO(n*T)")
for idx, arr in enumerate(arrays_20, 1):
    start = time.perf_counter()
    subset_sum_memo(arr, T)
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    execution_times_ms.append(elapsed_ms)
    n = len(arr)
    cost = n * T
    theoretical_O.append(cost)
    print(f"{idx}\t{elapsed_ms:.3f}\t\t{cost}")

# --------- PRIMERA GRÁFICA: SOLO TIEMPO ---------
plt.figure(figsize=(10, 5))
plt.plot(range(1, 31), execution_times_ms, marker='o', color='blue')
plt.xlabel('Número de arreglo')
plt.ylabel('Tiempo de ejecución (milisegundos)')
plt.title(f'Subset Sum con memoización - T = {T}')
plt.grid(True)
plt.tight_layout()
plt.show()

# --------- SEGUNDA GRÁFICA: TIEMPO vs O(n*T) ---------
plt.figure(figsize=(10, 5))
plt.plot(range(1, 31), execution_times_ms, marker='o', label='Tiempo real (ms)')
plt.plot(range(1, 31), theoretical_O, marker='x', linestyle='--', label='O(n*T)')
plt.xlabel('Número de arreglo')
plt.ylabel('Tiempo / Costo Teórico')
plt.title(f'Subset Sum - Tiempo real vs O(n*T) - T = {T}')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
