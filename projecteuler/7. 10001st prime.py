import math

def is_prime(n:int):
    if n > 1:
        for i in range(2, round(n/2)):
            if (n % i) == 0:
                return False
        else:
            return True


def n_prime_num(n):
    count = 1  # because 2 is prime but i'm skipping it
    needed_count = n

    for i in range(3, 10**8, 2):
        if is_prime(i):
            count += 1
            if count == needed_count:
                print(i)
                break

    return print('i did it')

n_prime_num(10001)