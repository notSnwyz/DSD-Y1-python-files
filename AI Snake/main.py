import random, sys, pygame as pg
from pygame.locals import *

FPS = 15
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0
assert WINDOWHEIGHT % CELLSIZE == 0
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0,)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)
BGCOLOR = BLACK

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

HEAD = 0

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pg.init()
    FPSCLOCK = pg.time.Clock()
    DISPLAYSURF = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pg.font.Font("freesansbold.ttf, 18")
    pg.display.set_caption("Wormy")

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()

def terminate():
    pg.quit()
    sys.exit()

def getRandomLocation():
    return {"x": random.randint(0, CELLWIDTH - 1), "y": random.randint(0, CELLHEIGHT - 1)}

def showStartScreen():
    titleFont = pg.font.Font("freesansbold.ttf", 100)
    titleSurf1 = titleFont.render("Title1!", True, WHITE, DARKGREEN)
    titleSurf2 = titleFont.render("Title2!", True, GREEN)

    degrees1 = 0
    degrees2 = 0
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        rotatedSurf1 = pg.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH/ 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        rotatedSurf2 = pg.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

        sys.drawPressKeyMsg()

        if sys.checkForKeyPress():
            pg.event.get()
            return
        pg.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 3
        degrees2 += 7

def drawAPple(coord):
    x = coord["x"] * CELLSIZE
    y = coord["y"] * CELLSIZE
    appleRect = pg.Rect(x, y, CELLSIZE, CELLSIZE)
    pg.draw.rect(DISPLAYSURF, RED, appleRect)

def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE):
        pg.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE):
        pg.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))

def drawScore(score):
    scoreSurf = BASICFONT.render("Score: %s" % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

def drawWorm(wormCoords):
    for coord in wormCoords:
        x = coord["x"] * CELLSIZE
        y = coord["y"] * CELLSIZE
        wormSegmentRect = pg.Rect(x, y, CELLSIZE, CELLSIZE)
        pg.draw.rect(DISPLAYSURF, DARKGREEN, wormSegmentRect)
        wormInnerSegmentRect = pg.Rect(x + 4. y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pg.draw.rect(DISPLAYSURF, GREEN, wormInnerSegmentRect)

def showGameOverScreen():
    gameOverFont = pg.font.Font("freesansbold.ttf", 150)
    gameSurf = gameOverFont.render("Game", True, WHITE)
    overSurf = gameOverFont.render("Over", True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)
    sys.drawPressKeyMsg()
    pg.display.update()
    pg.time.wait(500)
    sys.checkForKeyPress()

    while True:
        if sys.checkForKeyPress():
            pg.event.get()
            return
        
def runGame():
    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)