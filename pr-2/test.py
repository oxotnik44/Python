from shedule_class import FileShedule
from watchdog.observers import Observer
try:
    while True:
        print("Введите слово: ")
        true = True
        word: str = input()
        if word.isalpha() and len(word) >= 3:
            file = f"C:/Users/artem/Desktop/Python/pr-2/files/{word}.txt"
            with open (file, "w"):
                print("Успешное создание файла")
            break
        else:
            print("Введите корректно данные")
except Exception:
    print("Произошла ошибка")
except KeyboardInterrupt:
    print("Заверешение работы")
