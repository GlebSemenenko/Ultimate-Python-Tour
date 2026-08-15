import pyautogui
import random
import time


def click_center_random_interval():
    """
    Бесконечно кликает в центр экрана со случайным интервалом от 10 до 100 секунд.
    Для остановки нажмите Ctrl+C в терминале.
    """
    print("Программа запущена. Для остановки нажмите Ctrl+C.")

    # Получаем размер экрана
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2

    print(f"Размер экрана: {screen_width}x{screen_height}")
    print(f"Центр экрана: ({center_x}, {center_y})")

    try:
        while True:
            # Генерируем случайный интервал от 10 до 100 секунд
            interval = random.uniform(10, 100)
            print(f"Ожидание {interval:.2f} секунд до следующего клика...")
            time.sleep(interval)

            # Кликаем в центр экрана
            pyautogui.click(center_x, center_y)
            print(f"Клик в центре экрана ({center_x}, {center_y}) выполнен.")

    except KeyboardInterrupt:
        print("\nПрограмма остановлена пользователем.")


if __name__ == "__main__":
    # Небольшая задержка перед запуском, чтобы успеть переключиться в нужное окно
    print("Программа запустится через 3 секунды. Переключитесь в нужное окно.")
    time.sleep(3)
    click_center_random_interval()