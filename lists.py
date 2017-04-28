items = []
items.append('sugar')
items.append('salt')
items.append('milk')
items.append('flour')
items[0] = 'cows'
print(str(items).title()) # convert list to string to change case

items.insert(0,'bread') # we use insert to add item at any index position of the list
print(items)

del items[4] # use del function without quotes to delete an index from a list.
print(items)

del(items[2]) # you can also use parenthesis although it's not that important. 
print(items)

items.insert(0,'beverage')
print(items)
