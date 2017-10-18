#Gary Li
#10/16/17
#colorChangeWindow.py

from random import randint
from ggame import *

def mouseClick(event):
    red = Color(0xFF0000,1)
    green = Color(0x00FF00,1)
    blue = Color(0x0000FF,1)
    black = Color(0x000000,1)
    blackOutline = LineStyle(1,black)
    num = randint(1,4)
    if num == 1:
        color = red
    elif num == 2:
        color = green
    elif num == 3:
        color = blue
    else:
        color = black
    line = LineStyle(3,color)
    square = RectangleAsset(1000,1000,blackOutline,color)
    Sprite(square)

App().listenMouseEvent('click',mouseClick)
App().run()