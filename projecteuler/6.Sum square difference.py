list_of_nums = [x for x in range(1, 101)]
list_of_squares = [x**2 for x in range(1, 101)]

print(list_of_nums)
print(list_of_squares)

SQUARE_OF_SUM = 0
sum_of_squares = 0

for n in list_of_nums:
    SQUARE_OF_SUM = SQUARE_OF_SUM + n
SQUARE_OF_SUM = SQUARE_OF_SUM ** 2

for n in list_of_squares:
    sum_of_squares = sum_of_squares + n

print(SQUARE_OF_SUM)
print(sum_of_squares)
result = SQUARE_OF_SUM - sum_of_squares
print(result)
