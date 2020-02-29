import pygame, grb, random

from obj import *

# homing bullet AI: (self position minus target position) divided by speed. the higher the dividend, the slower the speed.




class TinyFastEnemy():
    def __init__(self, sprite, x, y, projsprite, projbox, sx, sy, gamehandler):
        self.hELTH = 35
        self.sprite = pygame.image.load(sprite)
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.directionRefreshCounter = 0
        self.currentDirection = random.randint(0, 3)
        self.hitbox = pygame.Rect[self.x, self.y, self.sx, self.sy]
        self.living = True
        gamehandler.add_custom_user(self)
    def move_self(self, moved_x, moved_y):
        oldx = self.x
        oldy = self.y
        self.x = oldx + moved_x
        self.y = oldy + moved_y
        return [self.x, self.y]
    def normal_movement(self, player_coor):
        if self.directionRefreshCounter == 15:
            self.directionRefreshCounter = 0
            self.currentDirection = random.randint(0, 3)
        elif self.directionRefreshCounter < 15:
            if self.currentDirection == 0:
                self.x += CalPixelSpeed(10)
                self.y -= CalPixelSpeed(10)
            elif self.currentDirection == 1:
                self.x -= CalPixelSpeed(10)
                self.y -= CalPixelSpeed(10)
            elif self.currentDirection == 2:
                self.x += CalPixelSpeed(10)
                self.y += CalPixelSpeed(8)
            elif self.currentDirection == 3:
                self.x -= CalPixelSpeed(10)
                self.y += CalPixelSpeed(8)
    def player_movement(self, old_pos, new_pos, player_movement):
        self.normal_movement(new_pos)
    def take_damage(self, knockbackVar, amountOfDamage):
        self.hELTH -= amountOfDamage
        self.y += CalPixelSpeed(4)
    def get_destroyed(self, player_coor):
        pass





def delayCutsceneFrame():
    global fastCutscene
    fastCutscene = True
    print("ARMAGEDDON")
def cutscene1():
    global fastCutscene
    fastCutscene = False
    print("epepepepepepepepepepisode1")
    global gamemode
    modeCut1Event = EventHandler()
    grb.screen.fill((20, 20, 20))
    loadText = Text("Loading... Please wait.", grb.hugfont, [200, 255, 200], 200, 300)
    loadTextTip = Text("Press the RETURN key to skip the cutscene", grb.bigfont, [255, 255, 255], 200, 450)
    modeCut1Event.key_event_use()
    cut1File = open("cutscene1Text.txt", "r").read()
    cutsceneRawText = cut1File[cut1File.find("(((") + 3:cut1File.find(")))")]
    cutsceneTextList = []
    cutscene1Text = []
    for EachLine in cutsceneRawText.split("\n"):  
        cutsceneTextList.append(EachLine)
    for eachVar in cutsceneTextList:
        if fastCutscene == False:
            cutscene1Text.append(AnimText(eachVar, grb.bigfont, [255, 255, 255], 100, 250, 1))
    for currentcutText in cutscene1Text:
        if fastCutscene == False:
            cutsceneWait = 0
            for current_length in range(0, currentcutText.gtLen()):
                delayAmountMeasurer = KeyUser(pygame.K_RETURN, modeCut1Event, delayCutsceneFrame)
                grb.screen.fill((0, 0, 0))
                if fastCutscene == False:
                    currentcutText.animate_blit()
                else:
                    break
                    print("cheese")

            modeCut1Event.key_event_use()
            pygame.display.flip()
        if fastCutscene == False:
            if fastCutscene == False:
                for wait in range(0, 35):
                    grb.gameClock.tick_busy_loop(10)
                    cutsceneWait += 1
                    modeCut1Event.key_event_use()
                    pygame.display.flip()   
                    grb.gamemode = "episode1"




def episode1():
    global scrollVar, subScrollVar, playerShip
    scrollVar = 720
    subScrollVar = 0
    def drawScrollingBackground(): 
        global scrollVar, subScrollVar
        backgroundSprite = TempObject("backdrop.jpg", 200, scrollVar)
        foregroundSprite = TempObject("subbackdrop.jpg", 200, subScrollVar)
        if subScrollVar >= 720:
            subScrollVar = -720
        elif scrollVar >= 720:
            scrollVar = -720
        backgroundSprite.blit()
        foregroundSprite.blit()
        movementVar = 10#CalPixelSpeed(-10)
        scrollVar += movementVar
        subScrollVar += movementVar

        
    modeEpi1Event = GameHandler()
    playerShip = Ship([pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_SPACE], "delta1.GIF", modeEpi1Event, 4, 600, 600, 80, 80, "up", "blastershot.PNG", [600, 100, 24, 32], 15, 7, 500)
    episode1On = True
    episodePhaseVar = 0
    frameType = 'normal'
    while episode1On:
        grb.screen.fill((0, 0, 0))
        drawScrollingBackground()
        
        if frameType == 'normal':
            modeEpi1Event.all_event_use()
            playerShip.blit()
        elif frameType == 'spawn':
            pass
        pygame.display.flip()
        grb.gameClock.tick_busy_loop(15)










def episode2():
    pass

