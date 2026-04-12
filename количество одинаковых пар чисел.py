s = input()
num = s.split()
total = 0
for i in range(len(num)):
     for k in range(i+1, len(num)):
        if num[int(i)] == num[int(k)]:
            total += 1
print(total)