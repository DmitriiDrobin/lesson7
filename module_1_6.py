my_dict = {'book': 'книга', 'hello': 'привет', 'dog': 'собака'}
print('Dict:', my_dict)
print('Existing value:', my_dict['book'])
print('Not existing value:', my_dict.get('work'))
my_dict.update({'ice': 'лед'})
my_dict['cat'] = 'кот'
a =  my_dict.pop('dog')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
print()
my_set = {1, 3.2, 1, 'Name', 3.2, 3.2, True, True, 1, }
print('Set:', my_set)
my_set.add((1, 2, 3, 1))
my_set.add('Dima')
my_set.discard(1)
print('Modified set:', my_set)