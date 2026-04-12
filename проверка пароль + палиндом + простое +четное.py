def is_palindrome(text):
    return text == text[::-1]

def is_prime(num):
    num = int(num)
    if num < 2:
        return False
    t = 0
    for i in range(1, num + 1):
        if num % i == 0:
            t += 1
    return t == 2

def is_valid_password(password):
    s = password.split(':')
    if len(s) != 3:
        return False
    if not is_prime(s[1]):
        return False
    if not is_palindrome(s[0]):
        return False
    if int(s[2]) % 2 == 0:
        return True
    return False