import random
import matplotlib.pyplot as plt

plt.style.use("ggplot") # визуальный стиль графика.
# Доступны: default \ bmh \ fast \ grayscale \ ggplot \ fivethirtyeight


def simplest_grpf():
    squares = [1,3,3,4,6,6,7,3,6,-10] # список данный для отображения
    fix, ax = plt.subplots()

    ax.set_title('Simple Group Four') # заголовок графика
    ax.set_xlabel('X line') # именуем ось x
    ax.set_ylabel('Y line') # именуем ось y

    ax.scatter(1,2, s=10) # наносим точку на график

    x_corr = [1,2,3,4,5]
    y_corr = [1,2,3,4,5]
    ax.scatter(x_corr,y_corr) # вносим серию точек на график

    ax.plot(squares) # вызов линии на граике
    plt.show() # отображаем график


def kv_func(i): # рисуем квадратичную функцию
    x_values = range(1,i)
    print(x_values)
    y_values = [x**2 for x in x_values]
    _, ax = plt.subplots()
    ax.scatter(x_values,y_values)
    plt.show()


def random_points(input):
    _, ax = plt.subplots()
    x_values = []
    y_values = []
    for _ in range(1, input+1):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        x_values.append(x)
        y_values.append(y)

    ax.scatter(x_values, y_values)
    plt.show()


def simple_gist():
    data = {"Saryman": 1, "Frodo": 22, "Gimly": 134, "Bilbo": 109}

    # Извлекаем ключи и значения
    names = list(data.keys())
    values = list(data.values())

    # Создаем столбчатую диаграмму
    plt.bar(names, values, color='skyblue', edgecolor='black')

    # Добавляем значения над столбцами
    for i, (name, value) in enumerate(data.items()):
        plt.text(i, value + 2, str(value), ha='center', fontweight='bold')

    # Настройки графика
    plt.title("Количество чего-то у персонажей")
    plt.xlabel("Персонажи")
    plt.ylabel("Количество")
    plt.xticks(rotation=45)  # Поворачиваем подписи для удобства

    plt.tight_layout()  # Автоматическая подгонка
    plt.show()

simple_gist()







