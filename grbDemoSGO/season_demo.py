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
        self.hitbox = pygame.Rect[self.x, self.y, sx, sy]
        gamehandler.add_custom_user(self)
    def move_self(self, moved_x, moved_y):
        oldx = self.
        oldy = self.y
        self.x = oldx + moved_x
        self.y = oldy + moved_y
        return [self.x, self.y]
    def normal_movement(self, player_coor):

    def player_movement(self, old_pos, new_pos, player_movement):





def delayCutsceneFrame():
    global fastCutscene
    fastCutscene = True
    print("ARMAGEDDON")
def cutscene1():
    fastCutscene = False
    print("epepepepepepepepepepisode1")
    global gamemode
    modeCut1Event = EventHandler()
    grb.screen.fill((20, 20, 20))
    loadText = Text("Loading... Please wait.", grb.hugfont, [200, 255, 200], 200, 300)
    modeCut1Event.key_event_use()
    cut1File = open("cutscene1Text.txt", "r").read()
    cutsceneRawText = cut1File[cut1File.find("(((") + 3:cut1File.find(")))")]
    cutsceneTextList = []
    cutsene1Text = []
    for EachLine in cutsceneRawText.split("\n"):
        cutsceneTextList.append(EachLine)
    for eachVar in cutsceneTextList:
        cutsene1Text.append(AnimText(eachVar, grb.bigfont, [255, 255, 255], 100, 250, 1))


    #cutsene1Text = [
    #AnimText("In the star system of Sirius, a war rages, between 2 races, each one", grb.bigfont, [255, 255, 255], 100, 250, 1),
    #AnimText("hoping to obtain superior control over the other. ", grb.bigfont, [255, 255, 255], 100, 300, 1),
    #AnimText("The war had flared over a dispute relating to the recent theft of water supply", grb.bigfont, [255, 255, 255], 100, 250, 1),
    #AnimText("from the Dri Republic, and the Imperium was convicted of stealing the water supply.", grb.bigfont, [255, 255, 255], 100, 300, 1),
    #AnimText("The Imperium denied any responsibillity of stealing the water supply, and began to open fire.", grb.bigfont, [255, 255, 255], 100, 250, 1),
    #AnimText("The General sent 3 squads to lead the fleet, Alpha, Bravo and Delta.", grb.bigfont, [255, 255, 255], 100, 300, 1),
    #AnimText("This is your 3rd week of being in Delta Squad, and you board your ship, the Delta 1", grb.bigfont, [255, 255, 255], 100, 250, 1),
    #AnimText("and take off, heading for several key Dri Republic outposts.", grb.bigfont, [255, 255, 255], 100, 300, 1),
    #AnimText("But as you reach the dry, desolate plains of Krenthos, you hear an explosion.", grb.bigfont, [255, 255, 255], 100, 250, 1),
    #AnimText("The last thing you remember is your ship tilting toward a beige plain below...", grb.bigfont, [255, 255, 255], 100, 300, 1)
    #]
    for currentcutText in range(0, len(cutsceneTextList), 2):

        cutsceneWait = 0
        for current_length in range(0, currentcutText.gtLen()):
            delayAmountMeasurer = KeyUser(pygame.K_SPACE, modeCut1Event, delayCutsceneFrame)
            grb.screen.fill((0, 0, 0))
            if fastCutscene == False:
                currentcutText.animate_blit()
            else:
                break
                print("cheese")
            modeCut1Event.key_event_use()
            pygame.display.flip()
        if fastCutscene == False:
            for wait in range(0, 35):
                grb.gameClock.tick_busy_loop(10)
                cutsceneWait += 1
                modeCut1Event.key_event_use()
                pygame.display.flip()
            else:
                fastCutscene = False
    grb.gamemode = "story_selection_load"




def episode1():
    def drawScrollingBackground():
        
    modeEpi1Event = GameHandler()
    playerShip = Ship([pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d], "delta1.GIF", modeEpi1Event, 4, 600, 100, 80, 80, "up", "blastershot.PNG", [600, 100, 24, 32])
    episode1On = True
    episodePhaseVar = 0
    frameType = 'normal'
    while episode1On:

        screen.fill((0, 0, 0))
        modeEpi1Event.all_event_use()
        
        if frameType == 'normal':
            
        elif frameType == 'spawn':
            pass
        pygame.display.flip()










def episode2():
    pass

