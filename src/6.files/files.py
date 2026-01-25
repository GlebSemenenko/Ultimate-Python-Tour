import json

data = {
    "name": "Alex",
    "age": 33,
    "city": "Moscow",
    "country": "RU",
}

file_object = open("ex.txt", encoding="utf-8")
# file_object = open("ex.txt", "r", encoding="utf-8") можно открывать на чтение \ изменение аргументами "r" \ "w"
print(file_object.read()) # читаем файл
file_object.close() # закрываем поток чтения файла
print(file_object.close())

with open("ex.txt", "r", encoding="utf-8") as f: # лучше открывать файл так

    strings = f.readlines()
    print(f)
    for line in strings:
        print(line)


# Путь к файлам
# Относительный путь "src/6.files/ex.txt"
# Абсолютный путь "C:\Users\user\Documents\Projects\Ultimate-Python-Tour\src\6.files\ex.txt"
