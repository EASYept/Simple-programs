from math import sqrt

natural_nums = [x for x in range(1,1000)]

for a in range(1,500):
    for b in range(2,1000):
        if a < b:
            c_squared = a**2 + b**2
            c = (sqrt(c_squared))
            if c in natural_nums:
                if a + b + c == 1000:
                    print(a* b* c)

