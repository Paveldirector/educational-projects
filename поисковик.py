n = int(input())
s = []
z = []
result = []
for _ in range(n):
    st = input()
    s.append(st)
    
k = int(input())
for _ in range(k):
    zapros = input()
    z.append(zapros)
    
for i in s:
    flag = True
    for j in z:
        if j.lower() not in i.lower():
            flag = False
            break
    if flag == True:
        result.append(i)
print(*result, sep ='\n')