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

count_of_vowels()

# область видимости переменных


# def func_name() -> str 
# 
