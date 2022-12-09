from itertools import groupby

with open('1/list.txt', 'r') as f:
    unsanitary_list = f.readlines()

lines = [i.replace('\n', '') for i in unsanitary_list]
res = [list(sub) for ele, sub in groupby(lines, key = bool) if ele]
largest_lst = []
for i in res:
    largest = sum([int(x) for x in i])
    largest_lst.append(largest)

# Part 1
largest_lst.sort()
print(f'Answer to part 1: {largest_lst[-1]}')

# Part 2
largest_lst.sort()
print(f'Answer to part 2: {sum(largest_lst[-3:])}')