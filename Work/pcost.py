# pcost.py
#
# Exercise 1.27

with open('Data/portfolio.csv', 'r') as f:
    header = next(f)
    total = 0
    for line in f:
        l = line.split(',')
        total += int(l[1]) * float(l[2])
    print(f'Total cost: {total}')
