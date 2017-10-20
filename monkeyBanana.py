#Gary Li
#10/19/17
#monkeyBanana.py - best game ever

from random import randint
from ggame import *

#constants
ROWS = 20
COLS = 40
CELL_SIZE = 20

#moves the monkey right
def moveRight(event):
    if monkey.x<(COLS-1)*CELL_SIZE:
        monkey.x += CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()

#moves the monkey left
def moveLeft(event):
    if monkey.x>0:
        monkey.x -= CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()

#moves the monkey down
def moveDown(event):
    if monkey.y<(ROWS-1)*CELL_SIZE:
        monkey.y += CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()

#moves the monkey up
def moveUp(event):
    if monkey.y>0:
        monkey.y -= CELL_SIZE
        if monkey.x == banana.x and monkey.y == banana.y:
            moveBanana()
            updateScore()

#moves bana to random location
def moveBanana():
    banana.x = randint(0,COLS-1)*CELL_SIZE
    banana.y = randint(0,ROWS-1)*CELL_SIZE
    data['frames'] = 0

#updating score when monkey gets banana
#updates text on screen
def updateScore():
    data['score'] +=10
    data['scoreText'].destroy()
    scoreBox = TextAsset('Score = '+str(data['score']))
    data['scoreText'] = Sprite(scoreBox,(0,ROWS*CELL_SIZE))

#keeps track of how many frames have passed
#moves banana if more than 300 have passed
def step():
    data['frames'] += 1
    if data['frames'] ==300:
        moveBanana()

#runs the game
if __name__ == '__main__':
    
    data = {}
    data['score'] = 0
    data['frames'] = 0
    
    green = Color(0x006600,1)
    brown = Color(0x8B4513,1)
    yellow = Color(0xFFFF00,1)
    
    jungleBox = RectangleAsset(COLS*CELL_SIZE,ROWS*CELL_SIZE,LineStyle(1,green),green)
    monkeyBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown),brown)
    bananaBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,yellow),yellow)
    scoreBox = TextAsset('Score = 0')
    
    Sprite(jungleBox)
    banana = Sprite(bananaBox,(COLS*CELL_SIZE/2,ROWS*CELL_SIZE/2))
    monkey = Sprite(monkeyBox)
    data['scoreText'] = Sprite(scoreBox,(0,ROWS*CELL_SIZE))
    
    App().listenKeyEvent('keydown','right arrow',moveRight)
    App().listenKeyEvent('keydown','left arrow',moveLeft)
    App().listenKeyEvent('keydown','down arrow',moveDown)
    App().listenKeyEvent('keydown','up arrow',moveUp)
    App().run(step)
