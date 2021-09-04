my_list = ['This price list is constantly updated as new publications',
           'if the price goes up or down by a large amount',
           'The company decided to focus entirely on price business users',
           'Getting lost in books: the language of reading'
           'greater than the average size or amount']
newlist = [x.upper() for x in my_list if "price" in x]
print(newlist)
