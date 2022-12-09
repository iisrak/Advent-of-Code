import string

lst = open("3/list.txt", "r").read().split("\n")
x, y = 0, 0

for line in lst:
    for char in line[:int(len(line)/2)]:
        if char in line[int(len(line)/2):]:
            x += string.ascii_letters.index(char)+1   
            break

for n in range(3, len(lst)+1, 3):
    l1, l2, l3 = lst[n-1], lst[n-2], lst[n-3]
    for char in l1: 
        if char in l2 and char in l3:
            y += string.ascii_letters.index(char)+1 
            break  

# Part 1
print(x)
# Part 2
print(y)
