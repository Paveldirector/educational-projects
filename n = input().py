n = input()
s = n
for i in range(0,len(n),3):
    s = s.replace(i,'')
print(s)
