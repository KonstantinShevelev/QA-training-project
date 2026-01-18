lst = ['apple', 'banana', 'kiwi', 'grapefruit', 'orange']
transformed_lst = [x.upper() for x in lst if len(x) >=5]
print(transformed_lst)