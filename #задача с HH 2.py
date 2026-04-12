#задача с HH 2
#Острова в космосе расположены в ряд. Передвигаться можно двумя способами:
#Магические паромы — между соседними островами (с i на i-1 или i+1).
#Порталы — телепортация между любыми островами, которые когда-то были на одном материке (имеют одинаковый номер в массиве).
#Нужно найти минимальное количество перемещений от первого острова до последнего.

s = '3 5 2 2 5'
sp = [int(i) for i in s.split()]
n = len(sp)
start = 0
end = n-1 

r1 = {0: [1]}                                   # первый остров
r2 = {i: [i-1, i+1] for i in range(1, n-1)}     # средние острова
r3 = {n-1: [n-2]}                               # последний остров

row = r1|r2|r3                                  #{0: [1], 1: [0, 2], 2: [1, 3], 3: [2, 4], 4: [3]}

port ={}                                        #{3: [0], 5: [1, 4], 2: [2, 3]}

for i, m in enumerate(sp):
    if m not in port:
        port[m] = []
    port[m].append(i)

dist = [-1] * n        # расстояния: [-1, -1, -1, -1, -1]
dist[start] = 0        # dist[0] = 0
queue = [start]        # queue = [0]
head = 0               # указатель на начало очереди
used_materics = set()  # пустое множество

while head<len(queue):

    v = queue[head]        # v = 0
    head += 1              # head = 1

    if v == end:
        print(dist[v])
        break

    for u in row[v]:    # обычные шаги, соседи из row
        if dist[u] == -1:
            dist[u] = dist[v] + 1
            queue.append(u)
    
    m = sp[v]   # материк текущего острова
    if m not in used_materics:
        used_materics.add(m)
        for u in port[m]:
            if dist[u] == -1:
                dist[u] = dist[v] + 1
                queue.append(u)

