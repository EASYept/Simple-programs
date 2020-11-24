"""so there is a trik/theorem to fast way to find how many divisors
1. find prime factors
2. add to powers +1
3. multiply powers = answer
"""

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
def return_factors(n, my_list):
    prime_factors(n)
    x = my_list.copy()
    factors.clear()
    return x



def prime_factors(n):
    flag = True
    if n > 1:
        while flag:
            for i in range(1, round(n+1)):
                if is_prime(i):
                    if n % i == 0:
                        factors.append(i)
                        flag = False
                        break
        n = n / factors[-1]
        prime_factors(n)
    return factors


def unique(list1):
    # insert the list to the set
    list_set = set(list1)
    # convert the set to the list
    return list(list_set)



def how_many_divisors(n):
    count = 1
    count_list = list(return_factors(n, factors))
    for i in unique(count_list):
        inside_count = 0
        for k in count_list:
            if i == k:
                inside_count += 1
        inside_count += 1
        count *= inside_count
    return count

def n_triangle_num(n):
    return sum(range(1, n+1))

def more_then_N_divisors(N):
    flag = True
    num = 2
    while flag:
        num += 1
        k = n_triangle_num(num)
        divisors = how_many_divisors(k)
        print(divisors)
        if divisors > N:
            flag = False
            print(k)

#print(prime_factors(7564))

print(how_many_divisors(76576500))
#print(how_many_divisors(45))
#print(more_then_N_divisors(500))

