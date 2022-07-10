# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=['name', 'shares', 'price'], types=[str, int, float]):
    '''
    Parse a CSV file into a list of records
    '''

    with open(filename) as f:
        rows = csv.reader(f)

        #read the file headers
        headers=next(rows)
        

        if select:
            indices = [headers.index(colname) for colname in select]
            headers=select
            
        else:
            indices = []

        records = []
        for row in rows:
            if not row:     #skip rows with no data
                continue
            if indices:
                row = [ row[index] for index in indices]
            if types:
                row = [func(val) for func, val in zip(types, row) ]
            record = dict(zip(headers,row))
            records.append(record)

    return records

portfolio=parse_csv(r'C:\Users\Ohwen\py_projects\learning\practical-python\Work\Data\portfolio.csv', select=['shares', 'price'], types=[int, float])

print(portfolio)