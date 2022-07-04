try:
       import requests, os, threading
       from pystyle import Colorate, Colors
except Exception as e:
       print(f'Missing Imports, Or Error: [{e}]')

def theme2():
 threads = 50
 url = input(Colorate.Horizontal(Colors.red_to_white, 'Url?: '))
 response = requests.get(url)
 os.system(f'title GVB ^| Botting ^| github/x8g')
 if response.status_code == 200:
        print(Colorate.Horizontal(Colors.red_to_white, f'viewed profile! | github/x8g'))
 else:
        print(Colorate.Horizontal(Colors.red_to_white, 'Error viewing | profile'))
        if threading.active_count() < int(threads):
            threading.Thread(target=theme2).start()