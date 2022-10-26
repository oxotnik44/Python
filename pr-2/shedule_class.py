from watchdog.events import FileSystemEventHandler
znach: list = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'a', 'e', 'i', 'o', 'u', 'y']

class FileShedule(FileSystemEventHandler):
    def on_created(self, event):
        file_name: str = event.src_path.split("/")
        name: str = file_name[-1].split(".")
        name_second: str = name[0]
        name_second.lower()
        for w in name_second:
            if w in znach:
                print(w.lower())
            else:
                print(w.upper())