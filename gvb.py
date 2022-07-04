try:
    import requests, os, sys, threading
    from pystyle import *
except Exception as e:
    print(f'Missing Imports, Or Error: [{e}]')

# don't skid!
headers = {
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "en-US,en;q=0.9",
"cache-control": "max-age=0",
"sec-ch-ua-mobile": "?0",adwadwawd
"sec-ch-ua-platform": "Windows",
"sec-fetch-dest": "document",
"sec-fetch-mode": "navigate",
"sec-fetch-site": "cross-site",
"sec-fetch-user": "?1",
"upgrade-insecure-requests": "1",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
}

banner = """
                                .:                           :.         thanks                
                              !?.            :   ~            ^J^             for          
                            ?B!             G5   &&7            YG^              the       
                          ?&G.      :^    .#@5   &@@&?  .^.      ^&#~               banner    
                        J@@!      ~5~    :&@@5   &@@@Y    ?Y.      5@#~  xtekky               
                        5@@7    !#G..Y~ ~@@@@5   &@@?      ~#G:    P@@!        I         
                         ^&@B:7&@!.Y@@@B@@@@@5   &@@!        P@B^~&@G.          love        
                           5@@@B^J@@@@@@@&&@@5   &@@!         ~&@@@!                you!    
                           5@@@5^@@@5.G@&:G@@5   &@@!       ...&@@@!      from              
                         ~&@B:5@P:#@&  !. G@@5   &@@!      ??^&@!~&@B.        zt#7380          
                        P@@7   ^&P.G@?    G@@5   &@@!    J&?:&B.   P@@7              aka   
                        J&@!     PP J&    G@@5   &@@!  ?@@^.B7     5@#~                 github.com/x8g
                          ?&G.    ~? !!   B@@5   &@@?7&@&..Y.    ~&#^                   
                            7B!    .^     J@@5   &@@@@@G  ^    .YG^                     
                              !?.          &@5   &@@@@J       :?^                       
                                :.         ~@5   &@@@~       ..                         
                                            BP   &@&:                                   
                                            ^Y   &B.                                    
                                             :   7                                      
"""
os.system(f'title GVB ^| Status: ^| loading..')
Anime.Fade(Center.Center(banner), Colors.blue_to_red, Colorate.Vertical, interval=0.01, time=6)
Anime.Fade(Center.Center("Github View Botter"), Colors.blue_to_red, Colorate.Vertical, interval=0.01, time=2)
Anime.Fade(Center.Center("By zt#7380"), Colors.blue_to_red, Colorate.Vertical, interval=0.01, time=3)
Anime.Fade(Center.Center("uhh bot views on github?"), Colors.blue_to_red, Colorate.Vertical, interval=0.01, time=5)

os.system(f'title GVB ^| Status: ^| loaded!')
user = input(Colorate.Horizontal(Colors.blue_to_purple, 'User?: '))

url = input(Colorate.Horizontal(Colors.blue_to_purple, 'Url?: '))

threads = input(Colorate.Horizontal(Colors.blue_to_purple, 'Threads?: '))

os.system(f'title GVB ^| Botting ^| ' + user + ' ^| github/x8g')
def view():
 while True:
   response = requests.get(url, headers=headers)
   if response.status_code == 200:
    print(Colorate.Horizontal(Colors.blue_to_purple, f'viewed profile! | user: ' + user))
   else:
    print(Colorate.Horizontal(Colors.blue_to_purple, 'Error viewing ' + user + ' profile'))
    sys.exit()

# I know its still slow even with the threads don't bully me :(    

while True:
        if threading.active_count() < int(threads):
            threading.Thread(target=view).start()
