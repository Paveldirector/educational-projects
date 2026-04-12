def is_prime(num):
    if num < 2:
        return False
    t = 0
    for i in range(1, num + 1):
        if num % i == 0:
            t += 1
    return t == 2

def get_next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num

n = int(input())
print(get_next_prime(n))