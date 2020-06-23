 
print("Launching Gamma Ray Battle Demo")

import pygame, grb, platform, time, season_demo, sys, webbrowser
from obj import *

print(str(grb.gamemode))
try:
    from arcade import *
    print("arcade pack init!")
    arcadeBool = True
except Exception as ex:
    print("no arcade pack detected.")
pygame.init()
# Python programming language
def OpenMenuStart():  
    print("opened menu")
    global gamemode
    global selected
    global menumusic, startCounterVar
    selected.play()
    menumusic.multiplay(-1)
    grb.gamemode = 2.5
    startCounterVar = 0
    print("grb.gamemode is 2.5")

def OpenMenu(): 
    print("opened menusFJsdjk sfjk nlj fdj ffvkgj d f")
    global gamemode
    global selected
    global menumusic                                                                                                  
    pygame.mixer.stop()
    pygame.event.clear()
    grb.gamemode = 3
    print("grb.gamemode is 3")
    selected.play()
    menumusic.multiplay(-1)

arcadeSlctMusic = Sound("arSlMu.ogg", musicchannel)
mainmusic = Sound("8B.ogg", musicchannel)
mainmusic.multiplay(-1)
# main code, gamma ray battle code 3
time.sleep(0.1)

def MakeTextOptions():
    print("make text options")
    
    titletext = Text("Game Selection", hugfont, [255, 255, 0], 150, 50)
    titletext2 = Text("Type_The_Letter_Of_The_Game_Mode_You_Want_To_Play", medfont, [100, 255, 100], 50, 95)
    arcademode = Text("[A] Survival Arcade Mode", bigfont, [255, 255, 255], 100, 185)
    storymode = Text("[M] Story Adventure Mode", bigfont, [200, 255, 200], 100, 125)
    demomode = Text("[T] Tutorial Mode", bigfont, [255, 255, 200], 100, 245)
    settingmode = Text("[S] Settings", bigfont, [180, 180, 180], 100, 305)
    backtotitle = Text("[B] Back To Title Screen", medfont, [255, 255, 255], 50, 650)
def ShowSettings():
    print ("settings show")
    if fpscounter:
        fpsColor = [155, 255, 155]
    else:
        fpsColor = [255, 155, 155]
    TitleSettings = Text("Settings", hugfont, [255, 255, 255], 500, 50)
    #volTitle = Text("Volume Controls", bigfont, [255, 255, 255], 150, 100)
    #volUpShow = Text("Up Arrow Key: Volume Up", medfont, [150, 255, 150], 150, 140)
    #volDownShow = Text("Down Arrow Key: Volume Down", medfont, [255, 150, 150], 150, 240)
    backtomenu = Text("[B] Back To Menu", medfont, [255, 255, 180], 700, 50)
    #volumeShow = Text("Volume: [" + str(int(grb.sfxvolume * 10)) + "] 0 - 10", medfont, [200, 200, 255], 250, 190)
    screensubttl = Text("Screen Controls", bigfont, [255, 255, 200], 200, 150)
    screenChangeInstructions = Text("[TAB] Toggle Screen Size", medfont, [200, 200, 200], 150, 190)
    screenChangeSubtitleIn = Text("Toggle Between 720p Windowed and 720p Fullscreen", smlfont, [200, 200, 200], 115, 210)
    fpsToggleText = Text("[F] Toggle FPS Counter (only active during gameplay)", bigfont, fpsColor, 200, 400)
def SetToSettingMode():
    global gamemode
    global menumusic
    global selected
    menumusic.stop()
    selected.play()
    grb.gamemode = "settings"
    print ("set to setting mode")

def ToggleFPSCounter():
    global fpscounter
    if fpscounter:
        fpscounter = False
    else:
        fpscounter = True

def TurnUpVol():
    global sfxvolume
    global selected
    if grb.sfxvolume < 1:
        grb.sfxvolume += 0.1
        selected.play()

def TurnDownVol():
    global sfxvolume
    global selected
    if grb.sfxvolume > 0:
        grb.sfxvolume -= 0.1
        selected.play()

def SetToTitleScreen():
    global gamemode
    #global selected
    menumusic.stop()
    grb.gamemode = 1
    mainmusic.multiplay(-1)
    #selected.play()

def ChangeToSetArcade():
    global gamemode
    global selected
    grb.gamemode = "settings_arcade"
    menumusic.stop()
    selected.play()
    time.sleep(0.2)
    arcadeSlctMusic.multiplay(-1)

storySlctMusic = Sound("storySlMu.ogg", musicchannel)
def ChangeToSetStory():
    global gamemode
    global selected, storySlctMusic
    grb.gamemode = "story_selection_load"
    menumusic.stop()
    selected.play()

def DetectKeyPressesMenu():
    global modeSelectEvent 
    dtctSettings = KeyUser(pygame.K_s, modeSelectEvent, SetToSettingMode)
    dtctBack = KeyUser(pygame.K_b, modeSelectEvent, SetToTitleScreen)
    dtctArcade = KeyUser(pygame.K_a, modeSelectEvent, ChangeToSetArcade)
    dtctStory = KeyUser(pygame.K_m, modeSelectEvent, ChangeToSetStory)
def DetectKeyPressesSettings():
    

    backToMain = KeyUser(pygame.K_b, modeSettingsEvent, OpenMenu)
    keyVolUp = KeyUser(pygame.K_UP, modeSettingsEvent, TurnUpVol)
    keyVolDown = KeyUser(pygame.K_DOWN, modeSettingsEvent, TurnDownVol)
    toggleFPSCount = KeyUser(pygame.K_f, modeSettingsEvent, ToggleFPSCounter)

    toggleScreenFull = KeyUser(pygame.K_TAB, modeSettingsEvent, ChangeScreenMode)
    
def DrawStorySelectText():
    mainTitle = Text("Story Mode", hugfont, [200, 255, 200], 100, 10)
    howToBack = Text("[B] Back to Menu", medfont, (200, 200, 200), 600, 50)
    StartTextStory = Text("[S] Play Episode", bigfont, [200, 255, 200], 200, 640)

    pygame.time.wait(1)
    #print(str(grb.gamemode))
def CopySiteLink():

    global storySelector, selectxp
    if storySelector.get_selected() == 2:
        selectxp.play()
        infoOn = True
        if platform.platform().find('Darwin') == -1:
            exec('pygame.scrap.put(pygame.SCRAP_TEXT, b"https://swordfishgamescont.wixsite.com/sword-fish-games")')
            showInfoBoard([Text("The link has been copied to the clipboard", medfont, [255, 255, 255], 350, 300)], 250, 100)
            storySelector.centerval = 0
        else:
            showInfoBoard([Text("Sorry, link copying is not available for Mac.", medfont, [255, 255, 255], 350, 250), Text("the pygame framework on Mac ", medfont, [255, 255, 255], 350, 300), Text("doesn't seem to support copying.", medfont, [255, 255, 255], 350, 340)], 250, 100)
            storySelector.centerval = 0
def openSite():

    global storySelector, selectxp
    if storySelector.get_selected() == 2:
        selectxp.play()
        infoOn = True
        webbrowser.open("https://swordfishgamescont.wixsite.com/sword-fish-games")
        storySelector.centerval = 0

def OpenEpisode():
    global storySelector, selected, gamemode
    selected.play()
    if storySelector.get_selected() == 0:
        print("episode1")
        grb.gamemode = "cutscene1"
    elif storySelector.get_selected() == 2:
        print("episode 2")
    else:
        print("no episode")

         


def DetectKeyPressesStorySel():
    global mmodeStorySlctEvent
    backMenu = KeyUser(pygame.K_b, modeStorySlctEvent, OpenMenu)
    siteOpen = KeyUser(pygame.K_c, modeStorySlctEvent, CopySiteLink)
    useEpisode = KeyUser(pygame.K_s, modeStorySlctEvent, OpenEpisode)
    siteDirOpen = KeyUser(pygame.K_o, modeStorySlctEvent, openSite)
def showGameOverText():
    mainGameOver = Text("Game Over", hugfont, [255, 100, 100], 350, 200)
    gameOverSubTitle = Text("Your ship was destroyed", bigfont, [255, 255, 102], 320, 250)
    returnInstructions = Text("[B] Back to Episode Menu", medfont, [200, 255, 200], 200, 600)
def backToEpisodes():
    global gamemode
    grb.gamemode = "story_selection_load"
def DetectKeyPressesGameOver():
    global modeGameOverEvent
    backEpisode = KeyUser(pygame.K_b, modeGameOverEvent, backToEpisodes)

for x in range(0, 10):
    grb.gameClock.tick_busy_loop(30)


while True:
    if grb.gamemode == 1:
        print ("grb.gamemode 1")
        grb.gamemode = 2
        mode1Event = EventHandler()
        mode1Event.key_event_use()    
    elif grb.gamemode == 2:
        print("grb.gamemode 2: titlescreen")
        screen.fill((0, 0, 0))
        mode1Event = EventHandler()
        tooptions = KeyUser(None, mode1Event, OpenMenuStart)
        startLogo = Object("logo.PNG", 25, -25)
        prsToStart = Text("Press Any Key To Start", hugfont, [200, 255, 200], 425, 500)
        prsToQuit = Text("Press DEL to quit game", medfont, [255, 200, 100], 425, 550)
        cpyright = Text("Copyright © 2019-2020 Swordfish Software. All Rights Reserved.", smlfont, [255, 255, 255], 450, 700)
        mode1Event.key_event_use()
        pygame.display.flip()
    elif grb.gamemode == 2.5:
        mainmusic.stop() 

        for startCounterVar in range(0, 40):
            for event in pygame.event.get():
                pass
            screen.fill((startCounterVar * 2, startCounterVar * 2, startCounterVar * 2))
            startLogo.update(startLogo.x - 5, startLogo.y + 30)
            prsToStart.move(prsToStart.x - 30, prsToStart.y - 3)
            prsToQuit.move(prsToQuit.x + 30, prsToQuit.y - 4)
            cpyright.move(cpyright.x + 5, cpyright.y - 30)
            print(startCounterVar)
            pygame.display.flip()
            grb.gameClock.tick(30)
        clr = 80
        for startCo in range(0, 80):
            clr -= 1
            screen.fill([clr, clr, clr])
            print("clr")
            for event in pygame.event.get():
                    pass
            pygame.display.flip()
        grb.gamemode = 3

    elif grb.gamemode == "3change":
        menumusic.multiplay(-1)
        selected.play()
        grb.gamemode = 3


    elif grb.gamemode == 3:
        screen.fill((10, 10, 10))
        MakeTextOptions()
        modeSelectEvent = EventHandler()
        DetectKeyPressesMenu()
        modeSelectEvent.key_event_use()
        pygame.display.flip()  

    elif grb.gamemode == "settings":
        print(str(grb.gamemode))
        screen.fill([80, 80, 80])
        ShowSettings()
        modeSettingsEvent = EventHandler()
        DetectKeyPressesSettings()
        modeSettingsEvent.key_event_use()
        pygame.display.flip()

    elif grb.gamemode == "settings_arcade":
        selectionMode()
        backMenuarc = KeyUser(pygame.K_b, modeArselEvent, OpenMenu)
        pygame.display.flip()
    elif grb.gamemode == "arcade":
        pass
    elif grb.gamemode == "story_selection_load":
        modeStorySlctEvent = EventHandler()
        episodeList = [
        BigText(["A lead pilot finds himself stranded on a barren and desolate planet, ", "with little hope of escape or survival."], bigfont, [200, 255, 255], 175, 200, 30, True, hugfont, [255, 255, 255], heading=u"Episode 1: Gamma Mania"), 
        BigText(["The pilot finds his home star system destroyed, ", "every last man clamoring to grab the ruins of the blast. "], bigfont, [200, 255, 255], 175, 200, 30, True, hugfont, [255, 255, 255], heading=u"Episode 2: G-Blast"), 
        BigText(["This is the demo version of Gamma Ray Battle.", "so keep an eye out for the full version at ", "[https://swordfishgamescont.wixsite.com/sword-fish-games]!", "[C] Copy Link To Clipboard", "[O] Open link directly in web browser"], bigfont, [200, 255, 255], 175, 200, 30, True, hugfont, [255, 255, 255], heading=u"More episodes coming soon!")]
        storySelector = Selector(pygame.K_DOWN, pygame.K_UP, modeStorySlctEvent, episodeList)
        storySlctMusic.multiplay(-1)
        grb.gamemode = "story_selection"
    elif grb.gamemode == "story_selection":
        screen.fill((20, 20, 20))
        DrawStorySelectText()
        DetectKeyPressesStorySel()
        storySelector.blit()
        modeStorySlctEvent.key_event_use()
        pygame.display.flip()
    elif grb.gamemode == "cutscene1":
        print("confirmepi1")
        season_demo.cutscene1()
    elif grb.gamemode == "episode1":
        print("episode 1 mode")
        season_demo.episode1()
    elif grb.gamemode == "gameover":
        screen.fill((0, 0, 0))
        modeGameOverEvent = EventHandler()
        showGameOverText()
        DetectKeyPressesGameOver()
        modeGameOverEvent.key_event_use()
        pygame.display.flip()
    else:
        print("invalid gamemode")
        sys.exit()
    grb.gameClock.tick(30)
