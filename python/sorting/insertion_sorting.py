def i_s(arr):
    arr_ln = len(arr)
    for i in range(1, arr_ln):
        key = arr[i]
        j = i-1
        while j>=0 and key<=arr[j]:
            arr[j+1]  = arr[j]
            j -= 1
        arr[j+1] = key
    print(arr)

if __name__ == '__main__':
    arr = [6, 4, 1, 23, 9]
    i_s(arr)    
