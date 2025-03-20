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

# Ejemplo de uso
arr = [3, 34, 4, 12, 5, 2]
T = 9

print("Memoización:", subset_sum_memo(arr, T))
