a = int(input())
i = 0
while a>=25:
    i += 1
    a -=25
while a>=10:
    i += 1
    a -=10
while a>=5:
    i += 1
    a -=5
while a>=1:
    i += 1
    a -=1
print(i)



a = int(input())
mx = a%10
mn = a%10
while a!=0:
    i = a%10
    if i > mx:
        mx = i
    elif i < mn:
        mn = i
    a = a//10
print('Максимальная цифра равна', mx)
print('Минимальная цифра равна', mn)



a = int(input())
total = 0
colnum = 0
proiz = 1
srlen = str(a)
sr = len(srlen)
iintsr = int(sr)
sra = total/iintsr
past = a%10
while a!=0:
    i = a%10
    total += i
    colnum += 1
    proiz *= i
    if a<10:
        first = a
    a = a//10
sra = total/iintsr
print(total)
print(colnum)
print(proiz)
print(sra)
print(first)
print(first+past)



n = int(input())
while n>99:
    n //= 10
print(n%10)    



n = int(input())
flag = "YES"
last_digit = n % 10

while n > 0:
    cur_digit = n % 10
    
    if last_digit != cur_digit:
        flag = "NO"

    n //= 10
print(flag)





n = int(input())
flag = "YES"
last_digit = n%10
while n != 0:
    cur_digit = n % 10
    if last_digit <= cur_digit:
        last_digit = cur_digit
    else:
        flag = 'NO'
    n //= 10
print(flag)
