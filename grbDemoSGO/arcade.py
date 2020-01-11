
from obj import *
from grb_globals import *

modeArselEvent = EventHandler()
listOfSprites = [TempObject("deltaShow.PNG", 6, 100), 
TempObject("ktxShow.PNG", 6, 100), 
TempObject("galactShow.PNG", 6, 100), 
TempObject("soloroShow.PNG", 6, 100)]
shipSelector = Selector(pygame.K_LEFT, pygame.K_RIGHT, modeArselEvent, listOfSprites)

    # arcade mode
def drawShipSelector():
    global shipSelector
    shipSlctVal = shipSelector.get_selected()
    if shipSlctVal == 0:
        shipText = "The Delta 1. While it's not the fastest, nor the strongest,  "
        shipText2 = "it is well-balanced and a good choice if you don't know what  "
        shipText3 = "ship to use. It's main weapon is a mid-speed, mid-damage blaster "
        shipText4 = "gun with a fair amount of ammo. However, it has no special abillity, "
        shipText5 = "so it may be a little bit weaker than the others. "
        shipText6 = "<<<Recommended for beginners.>>>"
    elif shipSlctVal == 1:
        shipText = "The KRX Tracker. A unique, tough but slow ship with slow but damaging "
        shipText2 = "cannons. It is good for those who prefer to take some hits  "
        shipText3 = "and throw more out. It's engines aren't fast, due to the ship's "
        shipText4 = "heavy weight, which in turn gives more HP than the "
        shipText5 = "rest. It's special abillity allows the ship to automatically move "
        shipText6 = "to the closest target, making fighting with this ship quite easy."
    elif shipSlctVal == 2:
        shipText = "The Galactica 42. It is another balanced ship, albeit slightly more "
        shipText2 = "powerful than the Delta 1. It has miniguns for weapons, however they "
        shipText3 = "take 4 seconds to charge, making it neccesary to be more cautious when "
        shipText4 = "piloting this ship. It's special abillty grants the Galactica 5 seconds "
        shipText5 = "improved damage and speed, for moments  when you are in a tight spot."
        shipText6 = "<<<Recommended for experienced pilots.>>>"
    elif shipSlctVal == 3:
        shipText = "The Soloro X. This is a fairly light ship, with improved speed and firepower. "
        shipText2 = "It has lasers which will go through a maximum of 3 targets. Since it has "
        shipText3 = "less HP, you will need to utillise it's fast speed to outrun enemy attacks. "
        shipText4 = "It's laser also can fry enemies quite quickly. It's special abillity charges "
        shipText5 = " the laser with ion plasma, making it thicker and deal more damage, "
        shipText6 = " and also spawns a shield, at the cost of reduced speed for 5 seconds."
    textShow1 = Text(shipText, medfont, (255, 255, 255), 520, 200)
    textShow2 = Text(shipText2, medfont, (255, 255, 255), 520, 230)
    textShow3 = Text(shipText3, medfont, (255, 255, 255), 520, 260)
    textShow4 = Text(shipText4, medfont, (255, 255, 255), 520, 290)
    textShow5 = Text(shipText5, medfont, (255, 255, 255), 520, 320)
    textShow6 = Text(shipText6, medfont, (255, 255, 255), 520, 350)
    shipSelector.blit()


def drawSelectText():
        titleArcade = Text("Arcade Mode Selection", hugfont, (255, 255, 255), 100, 5)
        shipchoosetitle = Text("Choose Your Ship:", bigfont, (255, 255, 0), 200, 60)
        shipmoveInst = Text("Use the left and right arrow keys to select a ship.", medfont, (255, 255, 100), 100, 95)
        continueText = Text("[S] Start battle with selected items", bigfont, (255, 100, 100), 400, 650)
        backText = Text("[B] Back to Options Menu", medfont, (200, 200, 200), 600, 50)
        startWarn = Text("Be warned: once you type S there is no confirmation, so be ready!", medfont, (255, 255, 255), 300, 680)





def selectionMode():
    global gamemode, modeArselEvent, arcadeSlctMusic
    print(str(grb_globals.gamemode))
    screen.fill((0, 0, 0))
    drawShipSelector()
    drawSelectText()

 



    modeArselEvent.event_use()



