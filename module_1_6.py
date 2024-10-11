my_dict = {'Lera': 1998,'Max': 2001, 'Sasha': 2005}
print(my_dict)
print(my_dict['Sasha'])
print(my_dict.get('Osmond', 1998))
my_dict.update({'Blake': 2010,
                'Sybil':1992})
print(my_dict)
my_dict.pop('Lera')
print(my_dict)
#print(my_dist['Lera'])
my_set = {1, 2, 2, 3, 4, 4, 5, 'a', 'a', 'b', 'c', 'c', 1.5, 1.5, True, False, True}
print(my_set)
my_set.add(83)
my_set.remove(1.5)
print(my_set)
