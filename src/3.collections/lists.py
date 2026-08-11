my_list1 = [1,2,3]
my_list2 = [1,2,3]
my_list3 = [1,4,3]

name = "Python"
str_to_char_list = list(name)
print(str_to_char_list)

nums = 1231412424 # но если захочу из числа создать лист цифр его нужно сначала перевести в строку
#nums_list = list(nums) # TypeError: 'int' object is not iterable ! С помощью конструктора лист мы создаем список только из iterable объектов
digits = [int(digit) for digit in str(nums)]
print(nums)

len(my_list1) # размер списка
print(my_list1 in my_list2) # вернет True только если объекты равны
print(my_list1 == my_list2) # сравниваем списки

# Оператор in
print("In operator")
list_in = [1,2,3]
list_in2 = [1,2,3]
list_in3 = list_in.copy()
print(1 in list_in) # оператор in проверяет вхождение
print(list_in in list_in2, "list_in in list_in2")
print(list_in2 in list_in2)
print("---------------------------")


# Добавление элементов
my_list = [1, 2, 3, 4]       # Создаем начальный список с элементами 1, 2 и 3
my_list.insert(0,99)         # Вставка по индексу, теперь список: [99, 1, 2, 3, 4]
my_list.extend([5, 6])       # Добавляем элементы 5 и 6 из другого списка, теперь список: [99, 1, 2, 3, 4, 5, 6]


# Удаление элементов
my_list.pop()                # Удаляем и возвращаем последний элемент, теперь список: [99, 1, 2, 3, 4, 5]
my_list.pop(1)               # Удаляем и возвращаем элемент с индексом 0, теперь список: [99, 2, 3, 4, 5]
del my_list[0]               # Удаление по индексу, теперь список: [2, 3, 4, 5]
my_list.remove(3)            # Удаляем первый элемент со значением 3 УДАЛЕНИЕ ПО ЗНАЧЕНИЮ, теперь список: [2, 4, 5]


# Сортировка
my_list.sort(reverse=True)   # Сортируем в обратном порядке, теперь список:[5,4,3,2,1,0]
my_list.sort()               # Сортируем элементы списка на месте, теперь список: [0, 1, 2, 4, 5]
my_list.copy()               # Создаем поверхностную копию списка, new_list: [0, 1, 2, 4, 5]
my_list.reverse()            # разворачиваем список


a = my_list[0] # можно получить элемент по индексу
my_list[0] = 100 # меняем элемент
print(a, "a")
aa = my_list[1::] # работают слайсы
slice_with_step = my_list[0:10:2]
# print(l[-12]) # ошибка


# Копирование
l = [1,2,3]
l2 = l # так у нас 2 переменные ссылаются на один список и при изменении списка обе переменные поменяются
l2.pop()
print(l, "l")
print(l2, "l2")

l = [1,2,3]
l3 = l.copy()
l3.pop()
print(l2) # l2 тоже
print(l3) # а так нет

lister1 = [1,2,3]
lister2 = lister1.copy()
lister2.append(4)
print(lister1 == lister2)
print(lister1, lister2)

l = [1,2,3]
l2 = l.copy()
print(l in l2)


