my_dict = {'Anna':1983, 'Ivan':1975, 'Kirill':1993, 'Olga':1990}
print(my_dict)
print(my_dict['Olga'])
print(my_dict.get('Ivan'))
print(my_dict.get('Oleg')) #print(my_dict.get('Oleg','такого ключа нет')) сместо None появится - такого ключа нет
my_dict.update({'Sasha':1980, 'Karina':1981})
a = my_dict.pop('Anna')
print(a)
print(my_dict)

my_set = {1, 1, 2, 3, 4, 4, 'Anna', 'Anna', 5}
print(my_set)
my_set.update([8, 'home'])
my_set.remove(4)
print(my_set)












