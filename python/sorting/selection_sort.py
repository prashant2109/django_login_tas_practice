def s_s(arr):
    arr_ln = len(arr)
    for i in range(arr_ln):
        min_idx = i
        for j in range(i+1, arr_ln):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    print(arr) 

if __name__ == '__main__':
    arr = [6 ,4, 1, 23, 9]
    s_s(arr)