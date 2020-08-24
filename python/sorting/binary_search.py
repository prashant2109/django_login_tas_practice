def iterative(arr, s_ele):
    least = 0
    largest = len(arr)-1
    while least <= largest:
        mid = (least + largest) // 2
        if arr[mid] < s_ele:
            least = mid + 1
        elif arr[mid] > s_ele:
            largest = mid - 1
        elif arr[mid] == s_ele:
            return mid
    return None

def recursive(arr, least, largest, s_ele):
    if largest >= least:
        mid = (least + largest) // 2
        if arr[mid] > s_ele:
            largest = mid - 1
            return recursive(arr, least, largest, s_ele)
        elif arr[mid] < s_ele:
            least = mid + 1
            return recursive(arr, least, largest, s_ele)
        if arr[mid] == s_ele:
            return mid
    return None
        
if __name__ == '__main__':
    arr = [1, 4, 6, 9, 23]
    s_ele = 231
    # des_index = iterative(arr, s_ele)
    # print(des_index)
    ############ recursive ##############
    least = 0
    largest = len(arr) - 1
    des_index = recursive(arr, least, largest, s_ele)
    print(des_index)
