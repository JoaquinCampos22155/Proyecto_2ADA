import time
import matplotlib.pyplot as plt

array = [5, 13, 3, 17, 0, 6, 11, 19, 9, 15, 2, 8, 10, 1, 4, 14, 12, 7, 20, 16]

targets_T = [
    132, 87, 104, 196, 71, 120, 158, 143, 99, 183,
    65, 178, 110, 77, 91, 149, 102, 170, 137, 81,
    160, 116, 98, 190, 123, 56, 107, 199, 140, 68
]

def subset_sum_dac(arr, T):
    def dfs(i, target):
        if target == 0:
            return True
        if i < 0 or target < 0:
            return False
        return dfs(i - 1, target - arr[i]) or dfs(i - 1, target)
    return dfs(len(arr) - 1, T)

execution_times_ms = []

for T in targets_T:
    start = time.time()
    subset_sum_dac(array, T)
    end = time.time()
    execution_times_ms.append((end - start) * 1000)

# Graficar
indices_T = list(range(1, 31))
plt.plot(indices_T, execution_times_ms, marker='o')
plt.xlabel('Índice del valor T')
plt.ylabel('Tiempo de ejecución (ms)')
plt.title('Subset Sum con Divide and Conquer - T variable, arreglo fijo')
plt.grid(True)
plt.tight_layout()
plt.show()