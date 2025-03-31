import time
import matplotlib.pyplot as plt

# Arreglo fijo
array = [5, 13, 3, 17, 0, 6, 11, 19, 9, 15, 2, 8, 10, 1, 4, 14, 12, 7, 20, 16]
n = len(array)

# Lista de 30 valores T
targets_T = [
    132, 87, 104, 196, 71, 120, 158, 143, 99, 183,
    65, 178, 110, 77, 91, 149, 102, 170, 137, 81,
    160, 116, 98, 190, 123, 56, 107, 199, 140, 68
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

# Medición de tiempos y cálculos teóricos
execution_times_ms = []
theoretical_O = []

print("Índice\tT\tTiempo (ms)\tO(n*T)")
for idx, T in enumerate(targets_T, 1):
    start = time.time()
    subset_sum_memo(array, T)
    end = time.time()
    elapsed_ms = (end - start) * 1000
    execution_times_ms.append(elapsed_ms)
    theoretical_cost = n * T
    theoretical_O.append(theoretical_cost)
    print(f"{idx}\t{T}\t{elapsed_ms:.3f}\t\t{theoretical_cost}")

# --------- PRIMERA GRÁFICA: SOLO TIEMPO ---------
plt.figure(figsize=(10, 5))
plt.plot(range(1, 31), execution_times_ms, marker='o', color='blue')
plt.xlabel('Índice del valor T')
plt.ylabel('Tiempo de ejecución (milisegundos)')
plt.title('Subset Sum con memoización - T variable, arreglo fijo')
plt.grid(True)
plt.tight_layout()
plt.show()

# --------- SEGUNDA GRÁFICA: TIEMPO vs O(n*T) ---------
plt.figure(figsize=(10, 5))
plt.plot(range(1, 31), execution_times_ms, marker='o', label='Tiempo real (ms)')
plt.plot(range(1, 31), theoretical_O, marker='x', linestyle='--', label='O(n*T)')
plt.xlabel('Índice del valor T')
plt.ylabel('Tiempo / Costo Teórico')
plt.title('Subset Sum - Tiempo real vs O(n*T)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
