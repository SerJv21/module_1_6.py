my_dict = {'Denis' : 2000, 'Max' : 2001, 'Alex' : 2002 }
print(my_dict)
print(my_dict['Denis'])
print(my_dict.get('Andrey'))
my_dict.update({'Lena' : 2010, 'Vera' : 2020})
print(my_dict)
b = my_dict.pop('Max')
print(my_dict)
print(b)
#Работа с множествами:
my_set = {3, 4, 5, 6, 3, 4, 5, 'String', True, 'String', True, (1, 2, 1, 2)}
print(my_set)
my_set.add(7)
my_set.add(101.321)
print(my_set)
my_set.remove(True)
print(my_set)

