import requests
import threading
import os
os.system(f'YT Views | github/x8g')

url = input("YT URL: ")
thread = input("Thread amount: ")

def yt():
    r = requests.get(url)
    if r.status_code == 200:
        print("video was viewed! | github/x8g")
    else:
        print("Error URL invalid or requests wasn't sent! | github/x8g")

threads = []

for i in range(int(thread)):
    t = threading.Thread(target=yt)
    t.daemon = True
    threads.append(t)

for i in range(int(thread)):
    threads[i].start()

for i in range(int(thread)):
    threads[i].join()

