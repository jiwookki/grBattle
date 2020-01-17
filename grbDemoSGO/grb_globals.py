import pygame







ttlIcon = pygame.image.load("scrIcon.PNG")
print("screen init")
pygame.display.set_icon(ttlIcon)
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Gamma Ray Battle Demo")


pygame.mixer.init(frequency=48000 )
pygame.init()
try:
    pygame.scrap.init()
    print("pygame scrap init")
except:
    print("pygame scrap not init")



screenmodevar = "window"
# global variables
def ChangeScreenMode():
    global screen
    global screenmodevar
    if screenmodevar == "window":
        screenmodevar = "fullscreen"
        screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN)
    else:
        screenmodevar = "window"
        screen = pygame.display.set_mode((1280, 720))
hugfont = pygame.font.Font("VT323-Regular.ttf", 50)
bigfont = pygame.font.Font("VT323-Regular.ttf", 35)
medfont = pygame.font.Font("VT323-Regular.ttf", 25)
smlfont = pygame.font.Font("VT323-Regular.ttf", 15)



sfxvolume = 0.5
musicvolume = 0.5

musicchannel = pygame.mixer.Channel(0)
sfxchannel = pygame.mixer.Channel(1)
gamemode = 1
gameClock = pygame.time.Clock()
gameClock.tick(1)




