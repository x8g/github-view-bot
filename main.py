import threading
import requests
from pystyle import Colorate, Colors
import os; os.system("cls||clear"); os.system(f"title github/x8g"); os.system("mode con:cols=60 lines=26")

url = 'https://camo.githubusercontent.com/d07c880342f0935b11b282178f79c6808f97c662cc9d193859ec79cee9af26bf/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d62366d'


def do_request():
 while True:
   response = requests.get(url)
   if response.status_code == 200:
    print(Colorate.Horizontal(Colors.red_to_purple, "viewed profile!"))

threads = []

for i in range(500):
    t = threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(500):
    threads[i].start()

for i in range(500):
    threads[i].join()
