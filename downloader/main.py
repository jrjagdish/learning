import threading
from downloaders import ImageDownloader,TextDownloader

tasks = [
    ImageDownloader("https://picsum.photos/200", "image1.jpg"),
    TextDownloader("https://www.w3.org/TR/PNG/iso_8859-1.txt", "textfile.txt")
]

def run_task(task):
    print(task)
    task.download()

threads = []

for t in tasks:
    thread = threading.Thread(target=run_task,args=(t,))
    threads.append(thread)
    thread.start()

for t in threads:
    t.join()

print("All downloades completed")        