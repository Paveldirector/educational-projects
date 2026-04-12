a,b,c,d = int(input()),int(input()),int(input()),int(input())
if a+b==c+d:
    print('YES')
elif (a==b and c==d) or (b==c and a==d):
    print('YES')
elif (a!=b and c!=d) and (b==c or a==d):
    print('YES')
else:
    print('NO')