
def brute_force_twoSum(A, target):
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == target:
                print(A[i], A[j])
                return True
    return False


def hash_table(A:list, target:int):
    ht = dict()
    for i in range(len(A)):
        if A[i] in ht:
            print(ht[A[i]], A[i])
            return True
        else:
            ht[target - A[i]] = A[i]
    return False


def twoSum(nums, target):

    num_to_index = {}
    print(type(num_to_index))

    for i, num in enumerate(nums):
        print(num_to_index)
        n = target - num

        if n in num_to_index:
            return [num_to_index[target - num], i]

        num_to_index = i

    return []


ar = [1, 5, 4, 8]
twoSum(ar, 6)
