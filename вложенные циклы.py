n = int(input())
sr=n//2+1
k = 0
for i in range (1,n+1):
    print('*')
    if i<sr:
        k+=1
    else:
        k-=1
    for j in range (k):
        print('*',end='')




        n = int(input())
total = 1
for i in range(1,n+1):
    print()
    for k in range(1,i+1):
        print (total, end=' ')
        total +=1



        n = int(input())
for i in range (1,n+1):
    print()
    for k in range (1,i):
        print (k, end='')
    for j in range (i,0,-1):
        print(j,end='')


        a,b = int(input()),int(input())
max_x = 0
max_count = 0
count = 0
for x in range (a,b+1):
    count = 0
    for i in range (1,x+1):
        if x % i == 0:
            count += i
            if count >= max_count:
                max_count = count
                max_x = x
print(max_x,max_count)




n=int(input())
while n>9:
    t=0
    while n>0:
        ld=n%10
        t+=ld
        n//=10
    n=t
print(n)



n=int(input())
t=0
for i in range (1,n+1):
    c=1
    for k in range(1,i+1):
        c*=k
    t+=c
print(t)



a,b=int(input()),int(input())
for x in range(a,b+1):
    c=0
    for i in range(1,x+1):
        if x%i==0:
            c+=1
    if c==2:
        print(x)



n = int(input())
res = 1
i = 2
while i <= n:
    res *= i
    i += 1
print(res)



# num = x**3 + y**3 = a**3 + b**3
for a in range(1,33):
    for c in range (1,a):
        for d in range (1,c):
            for b in range (1,d):
                if a**3 + b**3 == c**3 + d**3:
                    print(a**3 + b**3)