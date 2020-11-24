NUM = 600851475143

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

factors = []


def prime_factors(n, div=1):
    flag = True
    if n > 1:
        while flag:
            for i in range(div, round(n/div+1)):
                print(i)
                if is_prime(i):
                    print(i)
                    if n % i == 0:
                        print(str(i) + ' Found IT')
                        factors.append(i)
                        flag = False
                        break
        n = n/factors[-1]
        prime_factors(n)
    else:
        print(factors)

print(prime_factors(NUM))

