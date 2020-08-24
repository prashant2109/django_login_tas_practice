st = 'aaabbccddeeeefg'

idx = 1
res = []
while idx <= len(st):
    vl = st[idx]
    if (idx +1) >= len(st):
        if (st[idx-1]) != vl:
            res.append(idx)
        break
    if (st[idx-1] == vl):
        idx += 1
        continue
    elif (st[idx+1] == vl):
        idx += 2
        continue
    else:
        res.append(idx)
        idx += 1
        #print(idx)
print(st[res[1]])
    

