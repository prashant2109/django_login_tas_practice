def bs(lt):
    n = len(lt)
    for i in range(n):
        for j in range(n-i-1):
            if lt[j] > lt[j+1]:
                lt[j+1], lt[j] = lt[j], lt[j+1]
    return lt
###########################################################################
if __name__ == '__main__':
    lt = [23, 4, 7, 1, 5]
    print(bs(lt))
    
    
