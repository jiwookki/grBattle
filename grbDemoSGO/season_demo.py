import pygame, grb_globals

from obj import *




def cutscene1():
    print("epepepepepepepepepepisode1")
    global gamemode
    modeCut1Event = EventHandler()
    cutsene1Text = [
    AnimText("In the star system of Sirius, a war rages, between 2 races, each one", grb_globals.bigfont, [255, 255, 255], 200, 250, 1),
    AnimText("hoping to obtain superior control over the other. ", grb_globals.bigfont, [255, 255, 255], 200, 300, 1),
    AnimText("The war had flared over a dispute relating to the recent theft of water supply", grb_globals.bigfont, [255, 255, 255], 200, 250, 1),
    AnimText("from the Dri Republic, and the Imperium was convicted of stealing the water supply.", grb_globals.bigfont, [255, 255, 255], 200, 300, 1),
    AnimText("The Imperium denied any responsibillity of stealing the water supply, and began to open fire.", grb_globals.bigfont, [255, 255, 255], 200, 250, 1),
    AnimText("The General sent 3 squads to lead the fleet, Alpha, Bravo and Delta.", grb_globals.bigfont, [255, 255, 255], 200, 300, 1),
    AnimText("This is your 3rd week of being in Delta Squad, and you board your ship, the Delta 1", grb_globals.bigfont, [255, 255, 255], 200, 250, 1),
    AnimText("and take off, heading for several key Dri Republic outposts.", grb_globals.bigfont, [255, 255, 255], 200, 300, 1),
    AnimText("But as you reach the dry, desolate plains of Krenthos, you hear an explosion.", grb_globals.bigfont, [255, 255, 255], 200, 250, 1),
    AnimText("The last thing you remember is your ship tilting toward a beige plain below...", grb_globals.bigfont, [255, 255, 255], 200, 300, 1)
    ]
    for currentcutText in cutsene1Text:

        cutsceneWait = 0
        for current_length in range(0, currentcutText.gtLen()):
            grb_globals.gameClock.tick_busy_loop(10)
            grb_globals.screen.fill((0, 0, 0))
            currentcutText.animate_blit()
            modeCut1Event.event_use()
            pygame.display.flip()
        for wait in range(0, 45):
            grb_globals.gameClock.tick_busy_loop(10)
            cutsceneWait += 1
            modeCut1Event.event_use()
            pygame.display.flip()
    grb_globals.gamemode = "story_selection_load"




def episode1():
    modeEpi1Event = EventHandler()
    playerShip = Ship([pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d], "delta1.GIF", modeEpi1Event, 4, 600, 200, 80, 80, "up", "blastershot.PNG", )






def episode2():
    pass

