import threading
import time
import requests
from pystyle import Colorate, Colors
import os

os.system(f'title github/x8g')

# improved every bit of this code and made it "easier" to use!

print('User: ')
user = input()
print('')

print('URL: ')
url = input()
print('')

print('Thread Amount?: ')
thread = input()
print('')


def view():
 while True:
   response = requests.get(url)
   if response.status_code == 200:
    print(Colorate.Horizontal(Colors.red_to_purple, f'viewed profile! | user: ' + user))
    
    
threads = []

for i in range(int(thread)):
    t = threading.Thread(target=view)
    t.daemon = True
    threads.append(t)

for i in range(int(thread)):
    threads[i].start()

for i in range(int(thread)):
    threads[i].join()
