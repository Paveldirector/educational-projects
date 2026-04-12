n = int(input())
s = []
for _ in range(n):
    sl = input()
    s.append(sl)
k = int(input())
for i in range(len(s)-1, -1, -1):
    if len(s[i]) < k:
        del s [i]
for j in range(len(s)):
    print(s[j][k-1],end='')
