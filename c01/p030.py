price = 24
item = 'banana'

print('The %s costs %d cents.' % (item, price))
print('The %+10s costs %5.2f cents.' % (item, price))
print('The %+10s costs %10.2f cents.' % (item, price))

itemdict = {'item': 'banana', 'cost': 24}
print('The %(item)s costs %(cost)7.1f cents.' % itemdict)

"""
The banana costs 24 cents.
The     banana costs 24.00 cents.
The     banana costs      24.00 cents.
The banana costs    24.0 cents.
"""
