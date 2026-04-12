s = input()
for i in range(len(s)):
    if i==0 or i%2==0:
        print(s[i])



s = input()
for i in range(len(s)):
    print(s[-i-1])



    s = input()
total=0
for i in range (len(s)):
    total+=int(s[i])
print(total)



s = input()
flag = False
for i in range(len(s)):
    if s[i] in '0123456789':
        flag=True
if flag==True:
    print('Цифра')
else:
    print('Цифр нет')


    s = input()
a=0
b=0
for i in range(len(s)):
    if s[i] in '+':
        a+=1
    if s[i] in '*':
        b+=1
print('Символ + встречается', a, 'раз')
print('Символ * встречается', b, 'раз')




s = input()
a=0
b=0
for i in range(len(s)):
    if s[i] == b:
        a+=1
        b=s[i]
    b=s[i]
print(a)



num = int(input())
s=''
while num>0:
    a=num%2
    a=str(a)
    s= a+s
    num//=2
print(s)



s = input()
sl=len(s)
a=0
b=0
sr=0
if sl%2!=0:
    sr=sl//2+1
    a=s[:sr]
    b=s[sr::]
else:
    sr=sl//2
    a=s[:sr]
    b=s[sr::]
print(b,a,sep='')