s = input().split('-')
flag = True
for j in s:
    if not j.isdigit():
        flag = False
        break
if flag:
    if len(s) == 4:
        if not (s[0] == '7' and len(s[1]) == 3 and len(s[2]) == 3 and len(s[3]) == 4):
            flag = False
    elif len(s) == 3:
        if not (len(s[0]) == 3 and len(s[1]) == 3 and len(s[2]) == 4):
            flag = False
    else:
        flag = False         
if flag == True:
    print('YES')
else:
    print('NO')
