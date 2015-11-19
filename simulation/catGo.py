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

def updateDisplay(state):
    dw.fill(dw.purple)
    dw.draw(myimage, state)
    dw.draw(pondimage, [200, 400, 0, 0])
    dw.draw(dogimage, [500, 80, 0, 0])


# We'll update the stnte on each tick by incrementing the x stateinate
def updateState(state):
    return(state)

# We'll terminate when the x stateinate reaches the screen edge


def endState(state):
    if (state[0] >= width) or (state[0] < 0) or (state[1] > height) or (state[1] < 0):
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
            newstate = (state[0] - 10,state[1])
            return (newstate)
        if (event.key == pg.K_RIGHT):
            newstate = (state [0] + 10, state[1])
            return (newstate)
        if (event.key == pg.K_UP):
            newstate = (state [0], state [1] - 10)
            return (newstate)
        if (event.key == pg.K_DOWN):
            newstate = (state [0], state [1] + 10)
            return (newstate)
    else:
        return state
        
# Off we go! Start the cat at the left edge, and try for 30 FPS
frameRate = 60
initState = (0,0)
# debug()
rw.runWorld(initState, updateDisplay, updateState, handleEvent,
            endState, frameRate)


