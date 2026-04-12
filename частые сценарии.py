a,b = int(input()),int(input())
total = 0
for i in range(a,b+1):
    if i**3%10==4 or i**3%10==9:
        total += 1
print(total)


n = int(input())
total = 0
for i in range(n):
    n = int(input())
    total += n
print(total)



n = int(input())
total = 0
from math import *
for i in range(1,n+1):
    total += 1/i
total -= log(n)
print(total)



n = int(input())
total = 0
for i in range(1,n+1):
    if i**2%10==2 or i**2%10==5 or i**2%10==8:
        total += i
print(total)


n = int(input())
total = 1
for i in range(1,n+1):
        total *= i
print(total)




total = 1
for i in range(10):
    n = int(input())
    if n!=0: 
        total *= n
print(total)



n = int(input())
total = 0
for i in range(1,n+1):
    if n%i==0:
        total += i
print(total)


n = int(input())
total = 0
for i in range(1,n+1):
    if i%2==0:
        total -= i
    else:
        total += i
print(total)



n = int(input())
mx1 = 0
mx2 = 0
for i in range(1,n+1):
    a = int(input())
    if a>mx1:
        mx2 = mx1
        mx1 = a
    elif a>mx2:
        mx2 = a
print(mx1)
print(mx2)



flag = 10
for i in range(10):
    a = int(input())
    if a%2==0:
        flag -=1    
    else:
        flag +=1 
if flag == 0:
    print('YES')
else:
    print('NO')


n = int(input())
f1 = 0
f2 = 1
for i in range(1,n+1):
    f1,f2=f2,f1+f2
    print(f1, end=' ')