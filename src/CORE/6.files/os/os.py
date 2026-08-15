import os

# Модуль стандартно библиотеки пайтон
# позволяет работать с ос

cwd = os.getcwd() # узнать текущую директорию
lst = os.listdir()# посмотреть содержимое дтректории
# os.chdir('C:\\Users\\\\Desktop\\Python') # сменить директорию
# print(cwd)
# print(lst)

os.mkdir('abc') # создать дтректорию | если файл существует выдаст ошибку FileExistsError
os.rmdir('abc') # удалить дтректорию (удалит только пустую папку)
# os.makedirs('a/b/c') # создать вложенный каталог папок


open('exa.txt', 'w') # создать фал (если файл создан - FileExistsError)
os.rename('ex.txt', 'example.txt')# переименовать \ переместить файл
os.remove('example.txt') # удалить файл


print(1)





