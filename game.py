import os

while True:

     game = input ('game \n')
     if game == 'off':
          break
      
     if 'wow' in game:
          os.system ('wow' + game)
          os.startfile('C:\Program Files (x86)\World of Warcraft\_retail_\wow.exe')

