a = [  [12, 7, 3], 
       [4, 5, 6], 
       [7, 8, 9]   ]

b = [  [5, 8, 1, 2], 
       [6, 7, 3, 0], 
       [4, 5, 9, 1]  ]

mat_mul = []
for i in range(len(a)):    
    row_lst = []
    for j in range(len(b[0])):
        cell_val = 0
        for k in range(len(b)):
            cell_val += a[i][k] * b[k][j]
        row_lst.append(cell_val)
    mat_mul.append(row_lst)
print(mat_mul)