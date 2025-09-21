# циклы

'''
while True: 
    s = input("Введите сообщение: ")  # Считываем ввод от пользователя
    if s == "x":
        break
print('exx')
'''

for x in ["a", "b", "c"]:
    print(x)

for i in range(1, 10): # 10 вкдючено не будет
    print(i)
else:
    print('end')

nums = [3,22,53,434,533]
for i in nums:
    print(i) 
print(nums)


index = 0
while index < len(nums):  
    print(index, nums[index])
    index += 1  

for i in range(len(nums)):
    nums[i] +=1
print (nums)

def multiplication_table():
    for j in range(1, 11):
        for i in range(1, 11):
            print(i * j, end=" ")
        print()  # Переход на новую строку после каждой строки таблицы
