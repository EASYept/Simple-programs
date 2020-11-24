from math import sqrt


def is_prime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True


list_of_primes = []


def add_prime_below_n(n):  # starting from 2
    sum_of_primes = 2
    for i in range(3, n, 2):
        if is_prime(i):
            sum_of_primes += i
            print(i)
    return sum_of_primes




print(add_prime_below_n(2000000))

