import time
start = time.time()

with open('67.txt') as f:
    num = f.read()


num = num.split('\n')

k = []

for i in num:
    k.append(i.split(' '))

for listt in k:
    for item in listt:
        i = k.index(listt)
        j = k[i].index(item)
        k[i][j] = int(k[i][j])

k.reverse()

for row_index in range(1, len(k)):
    for item_index in range(0, len(k[row_index])):
        PLUS = max(k[row_index-1][item_index], k[row_index-1][item_index+1])
        k[row_index][item_index] += PLUS

print(k[-1])
print(f"it took {time.time() - start}s")