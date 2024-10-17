immutable_var = 1, 2.2, 3 ,4, 5, 'telephone', 'true'
print(immutable_var)
#immutable_var[2] = 8
#print(immutable_var)  - выдаёт ошибку, так как кортеж не подлежит изменению, за исключением части кортежа в виде списка (см.ниже)
immutable_var = (1, 2.2, [3 ,4], 5, 'telephone', 'true')
immutable_var[2][1] = 8
print(immutable_var)

mutable_list = [1, 2.2, 3 ,4, 5, 'telephone', 'true']
print(mutable_list)
mutable_list[0] = 7
mutable_list.append('object')
mutable_list.extend('work')
mutable_list.remove('telephone')
print(mutable_list)

