a = int(input())
a1 = a%100//10
a2 = a%10
if a1==0 and a2==0:
    print('YES')
else:
    print('NO')