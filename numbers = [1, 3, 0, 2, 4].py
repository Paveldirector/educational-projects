n = int(input())
x = []

for _ in range(n):
    num = int(input())
    x.append(num)
    
mi = x.index(min(x))
del x[mi]

ma = x.index(max(x))
del x[ma]

print(*x, sep = '\n')