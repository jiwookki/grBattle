import pygame, grb_globals

from obj import *


def cutscene1():
    modeCut1Event = EventHandler()
    cutText1_1 = AnimText("In the star system of Sirius, a war rages, between 2 races, each one", bigfont, [255, 255, 255], 350, 250, 1)
    cutText1_2 = AnimText("hoping to obtain superior control over the other. ", bigfont, [255, 255, 255], 350, 300, 1)
    cutText2_1 = AnimText("The war had flared over a dispute relating to the recent theft of water supply", bigfont, [255, 255, 255], 350, 250, 1)
    cutText2_2 = AnimText("from the Dri Republic, and the Imperium was convicted of stealing the water supply.", bigfont, [255, 255, 255], 350, 300, 1)
    cutText3_1 = AnimText("The Imperium denied any responsibillity of stealing the water supply, and began to open fire." bigfont, [255, 255, 255], 350, 250, 1)
    cutText3_2 = AnimText("The General sent 3 squads to lead the fleet, Alpha, Bravo and Delta.", bigfont, [255, 255, 255], 350, 300, 1)
    cutText4_1 = AnimText("This is your 3rd week of being in Delta Squad, and you board your ship, the Delta 1", bigfont, [255, 255, 255], 350, 250, 1)
    cutText4_2 = AnimText("and take off, heading for several key Dri Republic outposts.", bigfont, [255, 255, 255], 350, 300, 1)
    cutText5_1 = AnimText("But as you reach the dry, desolate plains of Krenthos, you hear an explosion.", bigfont, [255, 255, 255], 350, 250, 1)
    cutText5_2 = AnimText("The last thing you remember is your ship tilting toward a beige plain below...", bigfont, [255, 255, 255], 350, 300, 1)

def episode1():
    modeEpi1Event = EventHandler()
    playerShip = Ship([pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d], "delta1.GIF", modeEpi1Event, 4, 600, 200, 80, 80, "up", "blastershot.PNG", )






def episode2():
    pass

