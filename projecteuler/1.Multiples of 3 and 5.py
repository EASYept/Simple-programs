SUM = 0
number = 1000
multi = (3, 5)
nums_list = []

for n in range(number):
    if n % multi[0] == 0 or n % multi[1] == 0:
        nums_list.append(n)

print(sum(nums_list))