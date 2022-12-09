with open('2/list.txt', 'r') as f:
    lst = f.read().split('\n')

reference = {'X': 1, 'Y': 2, 'Z': 3}

reference_wins = ['A Y', 'C X', 'B Z']

reference_draws = ['A X', 'B Y', 'C Z']


def calculate_total(lst):
    total = 0
    for combination in lst:
        if combination in reference_draws:
            total += 3
        elif combination in reference_wins:
            total += 6

        # try:
        total += reference[combination[-1]]
        # except:
        #     continue
    return total


print(f'Total for part 1: {calculate_total(lst)}')

# Part 2

reference_wins_ = {'A': 'Y', 'C': 'X', 'B': 'Z'}

reference_draws_ = {'A': 'X', 'B': 'Y', 'C': 'Z'}

reference_lose_ = {'A': 'Z', 'B': 'X', 'C': 'Y'}

new_combinations = []
for combination in lst:
    if combination[-1] == 'Y':
        move = reference_draws_[combination[0]]
    elif combination[-1] == 'X':
        move = reference_lose_[combination[0]]
    else:
        move = reference_wins_[combination[0]]

    new_combinations.append(f'{combination[0]} {move}')

print(f'Total for part 2: {calculate_total(new_combinations)}')
