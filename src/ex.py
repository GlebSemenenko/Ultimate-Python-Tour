def arr_input(input):
    input.append("a")
    return input

def int_input(input):
    input += 1
    return input

arr = [1,2,3,4,5]
a = 10

r = arr_input(arr)
#print(r)
#print(arr) # исходный список был изменен

r2 = int_input(a)
#print(r2)
#print(a) # исходное число не было изменено тк инт передается по значению (инт неизменяемый)


# API map
# добавить элемент / изменить
# удалить элемент
# пройтись по элемнтам

m = {1:2,2:2,3:3}
del m[1]
print(m)




