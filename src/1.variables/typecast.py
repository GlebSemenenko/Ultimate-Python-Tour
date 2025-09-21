# type cast

i = 50
f = 55.5
s = "12qwerty"
si = "123"

new_float = float(f)
new_int = int(new_float)
print(new_int) 

# конвертируем float to int
f = int(f) # будет отброшена дробная часть
print(f)

# делаем из строки число 
i = str(i) 
print(type(i))

# из числа строку
# new_float = float(s) # ошибка так делать нельзя

si = int(si)
print(si) 