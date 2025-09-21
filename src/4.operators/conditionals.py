a = 11

is_empty_string = bool('')
print(is_empty_string) # можно проверить значение переменной -> пустая строка / 0 выдаст F

if (a % 2 == 0):
    print("четное") 
elif (a % 2 != 0):
    print("не четное")    
else:
    print("не понятное") 

# тернарный оператор 
rs = "совершеннолетний" if age >= 18 else "несовершеннолетний"


# Чтение входных данных
score = int(input())
# Ваш код здесь
if score <= 100 and score >= 90:
    grade = 'A'
elif score <= 89 and score >= 80:
    grade = 'B'
elif score <= 79 and score >= 70:
    grade = 'C'
elif score <= 69 and score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Вывод результата
print(grade)



