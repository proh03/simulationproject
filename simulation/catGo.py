 # from trepan.api import debug

# import pdb
# pdb.set_trace()

import runWorld as rw
import drawWorld as dw
import pygame as pg



# Initialize world
name = "Cat Go!"
width = 1000
height = 1000
rw.newDisplay(width, height, name)

# World state will be single x coordinate at left edge of world


# Display the state by drawing a cat at that x coordinate
myimage = dw.loadImage("cat.bmp")
pondimage = dw.loadImage("pond.bmp")
dogimage = dw.loadImage("dog2.bmp")
waterimage = dw.loadImage("water.bmp")
beeimage = dw.loadImage("bee.bmp")
cactusimage = dw.loadImage("cactus.bmp")
faucetimage = dw.loadImage("faucet.bmp")
winimage = dw.loadImage("youwin.bmp")
catfood = dw.loadImage ("catfood.bmp")
instructionimage = dw.loadImage("instructions2.bmp")

def updateDisplay(state):
    dw.fill(dw.sage)
    dw.draw (catfood, [920,0])
    dw.draw(myimage, (state.x, state.y))
    dw.draw(dogimage, [200, 400])
    dw.draw(cactusimage, [580, 120])
    dw.draw(pondimage, [600, 500])
    dw.draw(waterimage, [120, 0])
    dw.draw(beeimage, [850, 300])
    dw.draw(faucetimage, [300, 450])
    if (state.x>=900 and state.y>=0):
        dw.draw(winimage, [250, 10])
    if (state.x<=100 and state.y<=100):
        dw.draw(instructionimage, [200, 10])
        
#code added in class. does it work? Hoo knows?

class State:
    endState = False
    updateDisplay = True    
    def updatePosition(self, x, y):
        self.x = x
        self.y = y
    def updateGameState(self, gameRunning):
        self.isGameRunning = gameRunning
    def goLeft(self):
        self.updatePosition(self.x - 10, self.y)
    def goRight(self):
        self.updatePosition(self.x + 10, self.y)
    def goUp(self):
        self.updatePosition(self.x, self.y - 10)
    def goDown(self):
        self.updatePosition(self.x, self.y +10)
        
   
#see line 103 for initState



        
# We'll update the stnte on each tick by incrementing the x stateinate
def updateState(state):
    return(state)

# We'll terminate when the x stateinate reaches the screen edge


def endState(state):
    if (state.x >= width) or (state.x < 0) or (state.y > height) or (state.y < 0):
        return True
    else:
        return False

    
# For now we'll handle events just logging them to the console
#
#def handleEvent(state, event):
   # return(state)

def handleEvent(state, event):
    if (event.type == pg.KEYDOWN):
        if (event.key == pg.K_LEFT):
            state.goLeft()
        if (event.key == pg.K_RIGHT):
            state.goRight()
        if (event.key == pg.K_UP):
            state.goUp()
        if (event.key == pg.K_DOWN):
            state.goDown()
    return state

# the three modes of this game
gameRunning = 0
destinationReached = 1
gameOver = 2
    
# Off we go! Start the cat at the left edge, and try for 30 FPS
frameRate = 60

initState = State()
initState.updatePosition(0,0)
initState.updateGameState(gameRunning)


# debug()
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)


