#Gary Li
#10/19/17
#monkeyBanana.py - best game ever

from ggame import *

if __name__ '__main__':
    
    green = Color(0x006600,1)
    
    jungleBox = RectangeAsset(800,600,LineStyle(1,green),green)
    
    Sprite(jungleBox)
    
    App().run()
