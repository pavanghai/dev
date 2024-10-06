# list are mutable
l1 = [22,33,44,55,'trading', 55]
print('list indexing', l1[0])
print('list slicing', l1[-3:-1])

# strings are immutable
s1 = 'hello'
print('string indexing', s1[0])
print('string slicing', s1[2:4])

# Change value at index
l1[1]=99
print('list replace/changevalue at index', l1)

# adding new element in list
l1.append(87)
print('list append', l1)

l1.insert(1,77)
print('list insert at indexing', l1)

# remove element from list
l1.remove(55)
print('list remove first accurence', l1)

l1.pop(2)
print('list remove last element', l1)

l2 = [22,33,44,55,'trading', 55]
print('New list l2', l2)

el = l2.pop(0)
l2.append(el)
print('list remove element and add at the end', el, l2)

# replace element in a list eg replace 'trading' with 0
l1 = [22,33,44,55,'trading', 55]
print(l1)
l1[l1.index('trading')] = 'Trade'
print('list find index and replace', l1)

sl = 'fessorPro'
a=sl.index('s')
print('string indexing', a)
b=sl.upper()
print('string change to upper', b)
print(sl)
print('string show lower case', sl.lower())
print('string ends with ', sl.endswith('rr'))
print('string find char', sl.find('e'))


stocks = ['a','b','v']
print('list join as string ', '-'.join(stocks))

stl='alsdjf tajsdf j 1k'
print('string show split in list', stl.split(' '))

string3='python'
a=string3.replace('0','a')
print('string replace with new char', a)

st5='    fsdfsd   '
print('string strip', st5.strip())

hedge_fund_portfolio = {
    "fund_name": "Alpha Investments",
    "portfolio_value": 50000000,
    "investments": [

        {
            "type": "Equity",
            "holdings": [
                {"ticker": "AAPL", "quantity": 10000, "average_buy_price": 120},
                {"ticker": "TSLA", "quantity": 5000, "average_buy_price": 600}
            ]
        },

        {
            "type": "Fixed Income",
            "holdings": [
                {"bond_issue": "US Treasuries", "amount": 10000000, "yield": 1.5}
            ]
        },

        {
            "type": "Derivatives",
            "holdings": [
                {"instrument": "Options", "details": {"underlying": "GOOGL", "type": "Call", "strike_price": 1500}}
            ]
        }

    ],
    "performance_metrics": {
        "year_to_date_return": 5.2,
        "five_year_annualized_return": 7.1
    }
}
print(
    hedge_fund_portfolio.get('investments', 'Not Found')[2]
    .get('holdings', 'Not Found')[0].get('details', 'Not Found').get('strike_price', 'Not Found')
)
