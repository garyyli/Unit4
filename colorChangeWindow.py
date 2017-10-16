#Gary Li
#10/16/17
#colorChangeWindow.py

from math import randint
from ggame import *

def mouseClick(event):
    red = Color(0xFF0000,1)
    green = Color(0x00FF00,1)
    blue = Color(0x0000FF,1)
    black = Color(0x000000,1)
    blackOutline = LineStyle(1,black)

    Sprite(Rectangle)

mouseClick(event)
App().listenMouseEvent('click',mouseClick)
App.run()