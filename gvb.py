try:
    import httpx, requests, os, sys, threading
    from pystyle import *
except Exception as e:
    print(f'Missing Imports, Or Error: [{e}]')


banner = """ No Banner Retard
Github Views """
os.system(f'title GVB ^| Status: ^| loading.. ^| V2')
Anime.Fade(Center.Center(banner), Colors.blue_to_red, Colorate.Vertical, interval=0.01, time=6)


os.system(f'title GVB ^| Status: ^| loaded! ^| V2')
user = input(Colorate.Horizontal(Colors.blue_to_purple, 'User?: '))

url = input(Colorate.Horizontal(Colors.blue_to_purple, 'Url?: '))

threads = input(Colorate.Horizontal(Colors.blue_to_purple, 'Threads?: '))

os.system(f'title GVB ^| Botting ^| ' + user + ' ^| github/x8g ^| V2')
def view():
 while True:
   h = httpx.get(url)
   r = requests.get(url)
   if r.status_code == 200:
    print(Colorate.Horizontal(Colors.blue_to_purple, f'viewed profile! | V2'))
   else:
    print(Colorate.Horizontal(Colors.blue_to_purple, 'Error viewing profile | V2'))
   if h.status_code == 200:
    print(Colorate.Horizontal(Colors.blue_to_purple, f'viewed profile! | HTTPX | V2'))
   else:
    print(Colorate.Horizontal(Colors.blue_to_purple, 'Error viewing profile | V2'))
    



while True:
        if threading.active_count() < int(threads):
            threading.Thread(target=view).start()
