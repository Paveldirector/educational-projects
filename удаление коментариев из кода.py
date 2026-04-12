n = input()
n = n[1:]
sk = []
for _ in range(int(n)):
    s = input()
    d = s.find('#')
    if d == -1:
        s = s.rstrip()
        sk.append(s)
    else:
        s = s[:d]
        s = s.rstrip()
        sk.append(s)
print(*sk,sep = '\n')