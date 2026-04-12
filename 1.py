n = int(input())
old = input()
flag = True
for _ in range(n-1):
    new = input()
    if old[:old.find(' ')] == new[:new.find(' ')]:
        if old[old.find('«')+1:] < new[new.find('«')+1:]:
            old = new
            flag = True
        else:
            flag = False
            break
    elif old[:old.find(' ')] < new[:new.find(' ')]:
        flag = True
        old = new
    else:
        flag = False
        break
if flag == True:
    print('YES')
else:
    print('NO')