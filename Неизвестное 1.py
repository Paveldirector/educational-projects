a =input().split()
line = list(map(int, a))
mx0 = max(line)
ind0=line.index(mx0)
line[ind0]=0
mx9 = max(line)
if mx9==0:
    print(0)
else:
    line[ind0]=mx0
    mx1=1
    mx2=0
    ind1=0
    ind2=0
    cnt=0
    smx=max(line)
    s=0
    if len(line)==2:
        smn=min(line)*min(line)
    else:
        smn=min(line)*len(line)
    while mx1!=mx2:
        mx1=max(line)
        cnt=line.count(mx1)
        ind1=line.index(mx1)
        if cnt==2:
            line.remove(mx1)
            mx2=max(line)
            ind2=line.index(mx2)
            if (mx2*((ind2-ind1)+1))>smn:
                s=(mx2*((ind2-ind1)+1))
                if s>smx:
                    print(s)
                else:
                    print(smx)
            else:
                print(smn)
        elif cnt>2:
            line.remove(mx1)
            ind1=line.index(mx1)
            line.remove(mx1)
            line.insert(0, 0)
            line.insert(0, mx1)
            mx1=1
        else:
            line[ind1]=0
            mx2=max(line)