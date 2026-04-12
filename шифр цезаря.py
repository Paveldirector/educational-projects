def rus_sh(s,k):
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    s_h = ''

    for i in s:
        if i in rus_lower_alphabet:
            ind = rus_lower_alphabet.find(i)
            new_ind = (ind + k) % len(rus_lower_alphabet)
            s_h += rus_lower_alphabet[new_ind]
        elif i in rus_upper_alphabet:
            ind = rus_upper_alphabet.find(i)
            new_ind = (ind + k) % len(rus_upper_alphabet)
            s_h += rus_upper_alphabet[new_ind]
        else:
            s_h += i

    return s_h

def eng_sh(s,k):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s_h = ''

    for i in s:
        if i in eng_lower_alphabet:
            ind = eng_lower_alphabet.find(i)
            new_ind = (ind + k) % len(eng_lower_alphabet)
            s_h += eng_lower_alphabet[new_ind]
        elif i in eng_upper_alphabet:
            ind = eng_upper_alphabet.find(i)
            new_ind = (ind + k) % len(eng_upper_alphabet)
            s_h += eng_upper_alphabet[new_ind]
        else:
            s_h += i

    return s_h

def rus_de_sh(s,k):
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    s_h = ''

    for i in s:
        if i in rus_lower_alphabet:
            ind = rus_lower_alphabet.find(i)
            new_ind = (ind - k) % len(rus_lower_alphabet)
            s_h += rus_lower_alphabet[new_ind]
        elif i in rus_upper_alphabet:
            ind = rus_upper_alphabet.find(i)
            new_ind = (ind - k) % len(rus_upper_alphabet)
            s_h += rus_upper_alphabet[new_ind]
        else:
            s_h += i

    return s_h

def eng_de_sh(s,k):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s_h = ''

    for i in s:
        if i in eng_lower_alphabet:
            ind = eng_lower_alphabet.find(i)
            new_ind = (ind - k) % len(eng_lower_alphabet)
            s_h += eng_lower_alphabet[new_ind]
        elif i in eng_upper_alphabet:
            ind = eng_upper_alphabet.find(i)
            new_ind = (ind - k) % len(eng_upper_alphabet)
            s_h += eng_upper_alphabet[new_ind]
        else:
            s_h += i

    return s_h

s_h = ''
s = input('Введите предложение. ')
k = int(input('Введите шаг. '))
print(eng_de_sh(s,k))