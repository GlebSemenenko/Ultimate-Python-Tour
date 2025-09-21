'''
логические операторы 
not - самый высокий приоритет
and
or - самый низкий приоритет
'''

b1 = 2 == 32
print(b1)

warm = True
sunny = False

print(f'Тепло {warm}, Солнечно {sunny}')
going_to_the_beach = warm and sunny
print(f"Едем на пляж ? {going_to_the_beach}")

string_bool_1 = ''
print(bool(string_bool_1)) # можно проверить массив/переменную и тд если пустая или значение по умолчанию = F

res = (False or True) and not (False and True or True)
print(res) 

