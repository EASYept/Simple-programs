
def k_i_j(i, j):
    i += 1
    j += 1
    GRID = [[1 for x in range(0, j)] for x in range(0, i)]
    for n in range(1, len(GRID)):
        for k in range(1, len(GRID[0])):
            GRID[n][k] = GRID[n-1][k] + GRID[n][k-1]
    print(GRID[i-1][j-1])

k_i_j(20, 20)


# another answer
from math import factorial
import time


def main():
    """Main Program"""
    start_time = time.time()

    n = 40  # The total number of moves for any one path (right + down)
    r = 20  # The total number of right moves for any one path

    print(factorial(n) / (factorial(r) * factorial(n - r)))
    print("Elapsed Time:", (time.time() - start_time) * 1000, "millisecs")

main()


