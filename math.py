x1,y1,x2,y2 = float(input()),float(input()),float(input()),float(input())
from math import *
p = sqrt(pow((x1-x2),2)+pow((y1-y2),2))
print(p)



R = float(input())
from math import *
S = pi*R**2
C = 2*pi*R
print(S, C, sep='\n')



a,b = float(input()),float(input())
from math import *
sr1 = (a+b)/2
sr2 = sqrt(a*b)
sr3 = 2*a*b/(a+b)
sr4 = sqrt((a**2+b**2)/2)
print(sr1, sr2, sr3, sr4, sep='\n')



x = float(input())
from math import *
x = radians(x)
a = sin(x)+cos(x)+tan(x)**2
print(a)



x = float(input())
from math import *
a = floor(x)+ceil(x)
print(a)



a,b,c = float(input()),float(input()),float(input())
from math import *
d = b**2-4*a*c
if d==0:
    x1 = -b/(2*a)
    print(x1)
elif d>0:
    x1 = (-b-sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b+sqrt(b**2-4*a*c))/(2*a)
    print(min(x1,x2), max(x1,x2), sep='\n')
else:
    print('Нет корней')



n,a = int(input()),float(input())
from math import *
S = n*a**2/(4*tan(pi/n))
print(S)