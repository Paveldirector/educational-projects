m,p,n = int(input()),int(input()),int(input())
from math import *
for i in range(n):
    i=i+1
    print(i, m*(pow((1+(p/100)),i-1)))



m,n = int(input()),int(input())
if m%2!=0:
    for i in range(m,n-1,-2):
        print(i)
else:
    for i in range(m-1,n-1,-2):
        print(i)


m,n = int(input()),int(input())
for i in range(m,n+1):
    if i%17==0 or i%10==9 or (i%3==0 and i%5==0):
        print(i)



n = int(input())
for i in range(1,11):
        print(n, 'x', i, '=', n*i)