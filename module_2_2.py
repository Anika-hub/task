first = int(input())
second = int(input())
third = int(input())
if first == second == third: #Если все числа равны между собой, вывести 3
    print(3)
elif first == second or second == third or third == first: #Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
    print(2)
else:                            #Если равных чисел среди 3-х вообще нет, то вывести 0
    print(0)












#print(first, second, third)
#Если все числа равны между собой, то вывести 3