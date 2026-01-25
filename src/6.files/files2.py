# Самый простой способ работать с файлом - создать объект типа file
# создаст файл если не енайдет его
def read_from_file_ex_txt():
    f = open("ex.txt", 'r' , encoding='utf-8') # имя файла/путь, режим работы с фалойм, кодировка
    for line in f:
        print(line)
    f.close() # обязательно закрой ресурс !

def small_read():
    with open("ex.txt", 'r', encoding='utf-8') as f:
        print(f.read())

def write_in_file():
    with open("tz_from_book.txt", 'w', encoding='utf-8') as f: # записываем строки в файл
        for l in range(10):
            f.write("hello " + str(l) + "\n")

def replace_srt_in_file(old_srt, new_str):
    with open("tz_from_book.txt", 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for l in lines:
            if l == old_srt:
                l.replace(old_srt, new_str)
                print(l)
        f.writelines(lines)

write_in_file()
replace_srt_in_file("hello", "bye")

