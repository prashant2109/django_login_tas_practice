lt = [23, 4, 7, 1, 5]
n = len(lt)
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if lt[min_idx] > lt[j]:
            min_idx = j
    lt[min_idx], lt[i] = lt[i], lt[min_idx]
print(lt)