try:
    import httpx, requests, os, sys, threading, random, user_agent
    from pystyle import *
except Exception as e:
    print(f'Missing Imports, Or Error: [{e}]')
views = 0

headers = {
            'authority': 'camo.githubusercontent.com',
            'method': 'GET',
            'path': '/12df27140682753703f98aa63ea1afe69472864e061805883667dc107d86efcb/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d52656446757272466f78',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9,my;q=0.8',
            'cache-control': 'max-age=0',
            'dnt': '1',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'User-Agent': user_agent.generate_user_agent()
        }

banner = """V3

|        #
|        
|####    |
|    #   |
|    #   |                        
"""
os.system(f'title GVB ^| Status: ^| loading.. ^| V3')
Anime.Fade(Center.Center(banner), Colors.blue_to_red, Colorate.Vertical, interval=0.01, time=6)


os.system(f'title GVB ^| Status: ^| loaded! ^| V3')
user = input(Colorate.Horizontal(Colors.blue_to_purple, 'User?: '))

url = input(Colorate.Horizontal(Colors.blue_to_purple, 'Url?: '))

threads = input(Colorate.Horizontal(Colors.blue_to_purple, 'Threads?: '))

os.system(f'title GVB ^| Botting ^| ' + user + ' ^| github/x8g ^| V3')
def view():
 global views
 while True:
   r = requests.get(url, headers=headers)
   if r.status_code == 200:
    views +=1
    print(Colorate.Horizontal(Colors.blue_to_purple, f'viewed profile! | V3 | Views: {views}'))
   else:
    print(Colorate.Horizontal(Colors.blue_to_purple, 'Error viewing profile | V3'))
    



while True:
        if threading.active_count() < int(threads):
            threading.Thread(target=view).start()
