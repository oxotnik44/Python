from watchdog.events import FileSystemEventHandler

class FileShedule(FileSystemEventHandler):
    def on_created(self, event):
        print(event.src_path.split('.')[-1])
