"""A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers
is 9009 = 91 × 99.

Find the largest palindrome made from the product of
two 3-digit numbers."""

LARGEST = 0

for x in range(1000, 100, -1):
    for y in range(1000, 100, -1):
        a = str(x * y)
        if a[0] == a[-1] and a[1] == a[-2] and a[2] == a[-3]:  #FIXME probably can divide in half and then compare
            if x * y > LARGEST:
                LARGEST = x * y

print(LARGEST)
