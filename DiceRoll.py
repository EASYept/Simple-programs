import random


def dice_roll(player_count: int, sides=6):
    """roll dice for every player, if some of them have same highest number
    -> reroll only for them. And will do the same until ONLY ONE winner"""

    if player_count < 1:
        return print('wrong players number')
    if sides < 2:
        return print('should be more sides on dice')

    list_of_num = [0] * player_count
    index_of_max = [i for i, j in enumerate(list_of_num)]
    not_max = []
    rounds = 0

    while len(index_of_max) != 1:  #

        for i in range(0, len(not_max)):
            list_of_num[not_max[i]] = 0
        for i in range(0, len(index_of_max)):
            list_of_num[index_of_max[i]] = random.randint(1, sides)

        rounds += 1
        max_value = max(list_of_num)
        index_of_max = [i for i, j in enumerate(list_of_num) if j == max_value]
        not_max = [i for i, j in enumerate(list_of_num) if j != max_value]

    winner = 1 + index_of_max[0]

    print('Winner: Player № ' + str(winner))
    print('Rounds: ' + str(rounds))



