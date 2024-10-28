my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]  # список чисел
index = 0  # начальное значение
while index < len(my_list):  # сравниваем индекс с длиной списка
    number = my_list[index]  # задаём число из списка
    index = index + 1  # включаем счётчик
    if number < 0:  # если число отрицательное, цикл прервать
        break
    elif number == 0:  # 0 пропустить
        continue
    else:
        print(number)
