import pygame
listOfCustomEvents = []

NOTYPE = "notype"
PLAYERMOVEMENT = "enemymovement"
DIRECTIONDOWN = "dir_down"
DIRECTIONUP = "dir_up"
DIRECTIONLEFT = "dir_left"
DIRECTIONRIGHT = "dir_right"
BULLETAPPROACHING = "proj_aprch" 
BULLETIMPACT = "bullet_hit"


ttlIcon = pygame.image.load("scrIcon.PNG")
print("screen init")
pygame.display.set_icon(ttlIcon)
screen = pygame.display.set_mode((1280, 720))
try:
    pygame.scrap.init()
    print("pygame scrap init")
except:
    print("pygame scrap not init")
pygame.display.set_caption("Gamma Ray Battle Demo")


pygame.mixer.init(frequency=48000 )
pygame.init()

class CustomBlankEvent():
    def __init__(self):
        self.key = NOTYPE
        self.type = NOTYPE
        listOfCustomEvents.append(self)
class CustomEnemyEvent(CustomBlankEvent):
    def __init__(self):
        super.__init__()
class CustomCanvasEvent():
    def __init__(self, type_, keyOrDirection, position):
        self.type = type_
        self.key = keyOrDirection
        self.direction = keyOrDirection
        self.pos = position
class BulletIncoming(CustomBlankEvent):
    def __init__(self, bullet_pos):
        self.where = bullet_pos
        self.type = BULLETAPPROACHING
        self.key = NOTYPE
class PlayerMovement(CustomBlankEvent):
    def __init__(self, player_old_pos, player_new_pos):
        self.player_old_pos = player_old_pos
        self.player_new_pos = player_new_pos
        self.player_move_distance = (self.player_old_pos[0] - self.player_new_pos[0]) + (self.player_old_pos[1] - self.player_new_pos[1])
class BulletHit():
    def __init__(self, bulletRect):
        self.type = BULLETHIT
screenmodevar = "fullscreen"
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
gameClock.tick()


