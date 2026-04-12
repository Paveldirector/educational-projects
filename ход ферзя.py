x1,y1,x2,y2 = int(input()),int(input()),int(input()),int(input())
if (x1==x2 and y1!=y2) or (x1!=x2 and y1==y2):
    print('YES')
elif x1==y1 and x2==y2:
    print('YES')
elif (x1+x2+y1+y2)%2==0 and (abs(x1-x2)==1) and (abs(y1-y2)==1):
    print('YES')
elif (x1+x2+y1+y2)%2==0 and (abs(x1-x2)==2) and (abs(y1-y2)==2):
    print('YES')
elif (x1+x2+y1+y2)%2==0 and (abs(x1-x2)==3) and (abs(y1-y2)==3):
    print('YES')
elif (x1+x2+y1+y2)%2==0 and (abs(x1-x2)==4) and (abs(y1-y2)==4):
    print('YES')
elif (x1+x2+y1+y2)%2==0 and (abs(x1-x2)==5) and (abs(y1-y2)==5):
    print('YES')
elif (x1+x2+y1+y2)%2==0 and (abs(x1-x2)==6) and (abs(y1-y2)==6):
    print('YES')
elif (x1+x2+y1+y2)%2==0 and (abs(x1-x2)==7) and (abs(y1-y2)==7):
    print('YES')
else:
    print('NO')