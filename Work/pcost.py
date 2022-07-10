# pcost.py
#
# Exercise 1.27

# cost = 0

# with open('invalid_file.csv', 'rt') as f:
#     headers = next(f).split(',')
#     for line in f:
#         row = line.split(',')
#         #print (row[0], row[1], row[2])
#         cost = cost + (int(row[1]) * float(row[2]))
    
#     print(f'Total cost {round(cost, 2)}')

import csv
from multiprocessing.sharedctypes import Value
import sys 

def portfolio_cost(filename):
    'Calculates the cost of a portfolio'
    #cost = 0
    
    with open(filename, 'rt') as f:
        rows=csv.reader(f)
        headers = next(f).split(',')
        headers[4] = headers[4].strip()
        
        total_cost = 0.0
        for rowno, row in enumerate(rows, start=1):
            list(map(str.strip,row))
            record = dict(zip(headers, row))
            try:
                #vals = line.split(',')
                #print (row[0], row[1], row[2])
                #cost = cost + (int(row[1]) * float(row[2]))
                print(record)
                nshares = int(record['shares'])
                price = float(record['price'])
                total_cost += nshares * price
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
        #print(f'Total cost {round(cost, 2)}')

    return(total_cost)
    #print(f'Total cost {round(cost, 2)}')

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = r'C:\Users\Ohwen\py_projects\learning\practical-python\Work\Data\portfoliodate.csv'
cost = portfolio_cost(filename)
print('Total cost:', cost)