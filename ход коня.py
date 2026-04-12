x1,y1,x2,y2 = int(input()),int(input()),int(input()),int(input())
if x1-x2==1 and y1-y2==2:
    print('YES')
elif x1-x2==2 and y1-y2==1:
    print('YES')
elif x1-x2==-1 and y1-y2==-2:
    print('YES')
elif x1-x2==-2 and y1-y2==-1:
    print('YES')
elif x1-x2==-1 and y1-y2==2:
    print('YES')
elif x1-x2==-2 and y1-y2==1:
    print('YES')
elif x1-x2==1 and y1-y2==-2:
    print('YES')
elif x1-x2==2 and y1-y2==-1:
    print('YES')
else:
    print('NO')