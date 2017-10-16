#Gary Li
#10/16/17
#colorChangeWindow.py

from ggame import *

def mouseClick(event):
    Rectangle = RectangleAsset(200,100)
    Sprite(Rectangle)

App().listenMouseEvent('click',mouseClick)
App.run()