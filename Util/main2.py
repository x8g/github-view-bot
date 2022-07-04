try:
       import requests, os, threading
       from pystyle import Colorate, Colors
except Exception as e:
       print(f'Missing Imports, Or Error: [{e}]')

def theme1():
 threads = 50
 url = input(Colorate.Horizontal(Colors.blue_to_purple, 'Url?: '))
 response = requests.get(url)
 os.system(f'title GVB ^| Botting ^| github/x8g')
 if response.status_code == 200:
        print(Colorate.Horizontal(Colors.blue_to_purple, f'viewed profile! | github/x8g'))
 else:
        print(Colorate.Horizontal(Colors.blue_to_purple, 'Error viewing | profile'))
        if threading.active_count() < int(threads):
            threading.Thread(target=theme1).start()