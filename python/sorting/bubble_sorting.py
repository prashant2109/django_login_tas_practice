def b_s(arr):
    arr_ln = len(arr)
    for i in range(arr_ln):
        for j in range(arr_ln-i-1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print('ARRAY', arr)

if __name__ == '__main__':
    arr = [6, 4, 1, 23, 9]
    b_s(arr)
    