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