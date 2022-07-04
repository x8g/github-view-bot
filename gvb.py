try:
    import requests, os, sys, threading
    from pystyle import *
    import psutil
    import Util.main2
    import Util.test2
except Exception as e:
    print(f'Missing Imports, Or Error: [{e}]')

# don't skid!
menu = 'blue & purple theme (1) or red and white (2) (1 / 2)'
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
# ---
Anime.Fade(Center.Center(banner), Colors.blue_to_red, Colorate.Vertical, interval=0.01, time=4)
Anime.Fade(Center.Center("Github View Botter"), Colors.blue_to_red, Colorate.Vertical, interval=0.01, time=2)
Anime.Fade(Center.Center("By zt#7380"), Colors.blue_to_red, Colorate.Vertical, interval=0.01, time=3)
Anime.Fade(Center.Center("most overkill github view botter you've seen LOL."), Colors.blue_to_red, Colorate.Vertical, interval=0.01, time=5)

os.system(f'title GVB ^| Status: ^| loaded!')
# ---
def menu():
  while True:
   print('')
print(f'blue & purple theme (1) or red and white (2) | (1 / 2)')
option = input('What theme would you like?: ')

if(option == "1"):
 print('')
 print('')
 print('')
 print('')
 Util.main2.theme1()
if(option == "2"):
 print('')
 print('')
 print('')
 print('')
 Util.test2.theme2()
   


