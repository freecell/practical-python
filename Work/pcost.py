# pcost.py
#
# Exercise 1.27

cost = 0

with open(r'C:\Users\Ohwen\py_projects\learning\practical-python\Work\Data\portfolio.csv', 'rt') as f:
    headers = next(f).split(',')
    for line in f:
        row = line.split(',')
        #print (row[0], row[1], row[2])
        cost = cost + (int(row[1]) * float(row[2]))
    
    print(f'Total cost {round(cost, 2)}')

    