def sum_dig_pow(a, b):
    ans = []
    for i in range(a, b+1):
        d = 0
        for c, k in enumerate(str(i), 1):
            d += int(k) ** c
        if d == i:
            ans.append(i)
    return ans


print(sum_dig_pow(1, 100))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]
