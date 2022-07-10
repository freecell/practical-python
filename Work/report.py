# report.py
#
# Exercise 2.4

import csv
import sys
from pprint import pprint

def read_portfolio(filename=r'C:\Users\Ohwen\py_projects\learning\practical-python\Work\Data\portfolio.csv'):
    '''Computes the total cost (shares*price) of a portfolio file'''

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        select = ['name', 'shares', 'price']
        indices = [headers.index(colname) for colname in select]
        #print(indices)
        row = next(rows)
        #print(row)
        record = {colname:row[index] for colname, index in zip(select, indices)}
        #print(record)
        portfolio = [{colname: row[index] for colname,index in zip(select,indices)} for row in rows]
    return portfolio



    # portfolio = []
    # #name, shares, price
    # with open(filename, 'rt') as f:
    #     rows = csv.reader(f)
    #     headers = next(rows)

    #     for rowno, row in enumerate(rows, start=1):
    #         list(map(str.strip,row))
    #         record = dict(zip(headers, row))
    #         stock = {
    #             'name' : record['name'],
    #             'shares' : int(record['shares']),
    #             'price' : float(record['price'])
    #         }
    #         portfolio.append(stock)
        # for row in rows:
        #     #print(row)
        #     dict = {}
        #     dict['name'] = row[0]
        #     dict['shares'] = int(row[1])
        #     dict['price'] = float(row[2])
        #     portfolio.append(dict)
    #return portfolio

def read_prices(filename=r'C:\Users\Ohwen\py_projects\learning\practical-python\Work\Data\prices.csv'):
    dict = {}
    with open(filename ,'rt') as f:
        rows = csv.reader(f)
        
        for row in rows:
            if row:
                dict[row[0]] = float(row[1])
    return dict

def make_report(portfolio, prices):
    table = []
    for row in portfolio:
        name = row['name']
        shares = row['shares']
        price = prices[row['name']]#row['price']
        change = prices[row['name']] - float(row['price'])
        table.append((name, shares, price, change))
    return table
 
def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'{headers[0]:>10s}{headers[1]:>10s}{headers[2]:>10s}{headers[3]:>10s}')
    print(('-'*10+' ')*len(headers))
    for r in report:
        print('%10s %10s %10.2f %10.2f' % r)


print_report(make_report(read_portfolio(), read_prices()))
#prices = read_prices(r'C:\Users\Ohwen\py_projects\learning\practical-python\Work\Data\prices.csv')
#r'C:\Users\Ohwen\py_projects\learning\practical-python\Work\Data\portfolio.csv'
#portfolio = read_portfolio(r'C:\Users\Ohwen\py_projects\learning\practical-python\Work\Data\portfolio.csv')
#print(portfolio)
#pprint(portfolio)

#report = make_report(portfolio, prices)
# for r in report:
#     print('%10s %10d %10.2f %10.2f' % r)
# headers = ('Name', 'Shares', 'Price', 'Change')
# print(f'{headers[0]:>10s}{headers[1]:>10s}{headers[2]:>10s}{headers[3]:>10s}')
# print(('-'*10+' ')*len(headers))
# for name, shares, price, change in report:
#         price='$'+str(round(price,2))
#         print(f'{name:>10s} {shares:>10} {price:>10} {change:>10.2f}')

# current_value = 0.0
# total_cost = 0.0

# for s in portfolio:
#     total_cost += int(s['shares']) * float(s['price'])
#     if s['name'] in prices:
#         #print(prices[s['name']])
#         current_value += float(prices[s['name']]) * int(s['shares'])


# current_portfolio = current_value - total_cost
# print(f'Initial Portfolio value = ${total_cost}')            
# print(f'Value at current prices = ${round(current_value, 2)}')
# print(f'Gain/loss = ${round(current_portfolio, 2)}')

# with open(r'C:\Users\Ohwen\py_projects\learning\practical-python\Work\Data\dowstocks.csv', 'rt') as f:
#     rows = csv.reader(f)
#     headers = next(rows)
#     row = next(rows)
#     types = [str, float, str, str, float, float, float, float, int]
#     converted = [func(val) for func, val in zip(types, row)]
#     print(converted)
#     record = dict(zip(headers, converted))
#     x = (record['date'].split("/"))