'''
Функция — это именованный блок кода, 
который выполняет определенную задачу и может быть вызван из других частей программы.

Функции помогают:
- Организовать код в логические блоки
- Избежать повторения кода
- Сделать программу более читаемой
- Упростить отладку и поддержку
'''

# функции определяются с помощью ключевого слова def
def sum(a, b):
    return a + b # если в функции нет return, то возвращаемое значение - none

print(sum(1, 2)) # вызов функции 

def count_of_vowels(input_text: str) -> int: # нельзя ничего добавить кроме str
    count = 0
    letters = ['a','e','y','u','i','o']    
    char_list = list(input_text.lower())
    for ch in char_list:
        if ch in letters:
            count += 1
    print(count)
    return count

count_of_vowels("Kafka")
count_of_vowels(1)

# Значение аргументов по умолчанию
def arg_fn(a1, a2 = "A2", a3: str = "A3"):
    print("First arg is ", a1)
    print("Second arg is ", a2)
    print("Seard arg is ", a3)

arg_fn(1, 3)
arg_fn(a1=1, a2=2, a3=3) # Можно так передавать арргументы в функцию
arg_fn(a3=3, a2=2, a1=1) # Сохранится порядок

# Передача аргументов в функцию
def prim_fn(input):
    input += 10

input_int = 10 # Примитивы в функцию передаются по значению
prim_fn(input_int)
print(input_int) # Значение не изменилось 

def sl_fn(input):
    input.append(10)

input_arr = [1,2,3]
sl_fn(input_arr) # А ссылочные типы данных передаются уже по ссылке
print(input_arr) # Значение изменилось 


sl_fn(input_arr[:]) # Так мы передадим копию
print(input_arr) # Значение не изменилось 


def format_date(*, day: int, month: str): # * означает что при вызове функции надо именовать каждый аргумент
    print(day, " of ", month)

format_date(day=1, month="October")
# format_date(1, "October") # ОШИБКА ПРИ ЗАПУСКЕ  


