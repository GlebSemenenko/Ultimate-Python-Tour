import random
import time
import pyautogui

# Словарь с координатами (обратите внимание: нет ключа 4)
coordinates = {
    1: [237, 194],
    2: [478, 197],
    3: [614, 201],
    4: [615, 204],
    5: [798, 202],
    6: [881, 191],
    7: [951, 202],
    8: [1211, 200],
    9: [1407, 194],
}

# Создаём список существующих ключей, чтобы не выпадала ошибка при random
valid_keys = list(coordinates.keys())

print("Запуск автоматического кликера. Для остановки нажмите Ctrl+C в терминале.\n")

try:
    while True:
        # Выбираем случайный ключ из существующих (1,2,3,5,6,7,8,9)
        cor = random.choice(valid_keys)
        # Получаем координаты
        x, y = coordinates[cor]  # x = coordinates[cor][0], y = coordinates[cor][1]

        # Печатаем, куда сейчас будем кликать
        print(f"Клик по точке {cor}: X={x}, Y={y}")
        # Выполняем клик (не присваиваем результат, т.к. click() возвращает None)
        pyautogui.click(x, y)

        randomtime = random.randint(4, 58)
        time.sleep(randomtime)

except KeyboardInterrupt:
    print("\nПрограмма остановлена пользователем.")