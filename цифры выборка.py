a = int(input())
a1 = a%2
if not a1==0 and not 2<=a<=5:
    print('YES')
elif not a1==0 and 2<=a<=5:
    print('YES')
elif a1==0 and 2<=a<=5:
    print('NO')
elif a1==0 and 6<=a<=20:
    print('YES')
else:
    print('NO')