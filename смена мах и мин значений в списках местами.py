num = input()
w = [int(x) for x in num.split()]

ma = max(w)
mi = min(w)

i_ma = w.index(ma)
i_mi = w.index(mi)

w[i_ma], w[i_mi] = w[i_mi], w[i_ma]

print(*w)