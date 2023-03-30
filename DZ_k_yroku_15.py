# Условия задач:
# 1. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
# 2. Сжать массив, удалив из него все элементы, величина которых находится
# в интервале [а, b]. Освободившиеся в конце массива элементы заполнить нулями.

import random # Импортируем библиотеку рандом
rand_list = random.sample(range(1, 11), 10) # Генерируем случайный массив от 1 до 10, кол-во чисел = 50
print("Одномерный массив целых чисел: ", rand_list)
l1 = sorted(rand_list) # сортируем наш список
print("наименьшие два числа из массива : ", (l1[0]),",", (l1[1]))
print("Сократим массив, удалив все числа в интервале")
a1 = int(input("от: "))
b1 = int(input("до: "))
for q in rand_list[0::]:
        if q >= a1 and q <= b1:
                rand_list.remove(q)
                rand_list.append(0)
print("Сжатый массив: ", rand_list)
