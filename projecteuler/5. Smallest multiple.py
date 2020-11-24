"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

list_of_num = [x for x in range(1, 21)]

Did_i_find = False
for i in range(2520, 10**9, 2520):
    count = 0
    for num in list_of_num:
        if i % num == 0:
            count += 1
            if count == 20:
                Did_i_find = True
                print(i)
        else:
            count = 0
