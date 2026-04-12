def eng_sh(sl):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s_h = ''
    ignore = ' !,.:;"?'
    t = 0
    for i in sl:
        if i in ignore:
            t += 1
        lsl = len(sl) - t
    for i in sl:
        if i in eng_lower_alphabet:
            ind = eng_lower_alphabet.find(i)
            new_ind = (ind + lsl) % len(eng_lower_alphabet)
            s_h += eng_lower_alphabet[new_ind]
        elif i in eng_upper_alphabet:
            ind = eng_upper_alphabet.find(i)
            new_ind = (ind + lsl) % len(eng_upper_alphabet)
            s_h += eng_upper_alphabet[new_ind]
        else:
            s_h += i

    return s_h

s = input()
sp = s.split()
for i in range(len(sp)):
    s_h = eng_sh(sp[i])
    print(s_h,end=' ')