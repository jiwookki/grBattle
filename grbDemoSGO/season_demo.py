import pygame, grb, random

from obj import *

# homing bullet AI: (self position minus target position) divided by speed. the higher the dividend, the slower the speed.




class TinyFastEnemy():
    def __init__(self, sprite, x, y, projsprite, sx, sy, gamehandler):
        self.hELTH = 35
        self.sprite = pygame.image.load(sprite)
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        print(self.x)
        print(self.y)
        print(self.sx)
        print(self.sy)
        self.directionRefreshCounter = 0
        self.currentDirection = random.randint(0, 3)
        self.hitbox = pygame.Rect(self.x, self.y, self.sx, self.sy)
        self.living = True
        self.friendly = False
        self.damage = 35
        self.bulletlist = []
        self.gamehandler = gamehandler
        self.gamehandler.add_custom_user(self)
    def move_self(self, moved_x, moved_y):
        oldx = self.x
        oldy = self.y
        self.x = oldx + moved_x
        self.y = oldy + moved_y
        return [self.x, self.y]
    def normal_AI(self, player_coor):
        if self.directionRefreshCounter >= 15:
            self.directionRefreshCounter = 0
            self.currentDirection = random.randint(0, 5)
        elif self.directionRefreshCounter < 15:
            if self.currentDirection == 0:
                self.x += CalPixelSpeed(2)
                self.y += CalPixelSpeed(8)
            elif self.currentDirection == 1:
                self.x -= CalPixelSpeed(2)
                self.y += CalPixelSpeed(8)
            elif self.currentDirection == 2:
                self.x += CalPixelSpeed(6)
                self.y += CalPixelSpeed(4)
            elif self.currentDirection == 3: 
                self.x -= CalPixelSpeed(6)
                self.y -= CalPixelSpeed(14)
            elif self.currentDirection == 4:
                self.x += CalPixelSpeed(8)
                self.y -= CalPixelSpeed(8)
            elif self.currentDirection == 5:
                self.x -= CalPixelSpeed(8)
                self.y -= CalPixelSpeed(8)
            self.directionRefreshCounter += 1
        if self.y >= 680:                       
            self.y = 60

        if bool(checkInBoundsX(self.x)):
            self.x = checkInBoundsX(self.x)
        if bool(checkInBoundsY(self.y)):
            self.y = checkInBoundsY(self.y)
        self.hitbox = pygame.Rect(self.x, self.y, self.sx, self.sy)
        grb.screen.blit(self.sprite, [self.x, self.y])
    def player_movement(self, new_pos):
        self.normal_AI(new_pos)
    def take_damage(self, knockbackVar, amountOfDamage):
        print("boom")
        self.hELTH -= amountOfDamage
        self.y -= CalPixelSpeed(knockbackVar)
    def get_destroyed(self, player_coor):
        print("destroyed")
        if self.living == False:
            self.living = False
        self.gamehandler.remove(self)
    def collision_player(self, player_coor):
        self.get_destroyed(player_coor)
    def every_frame_event(self):
        pass
    def bullet_incoming(self, x, y):
        if random.randint(0, 2) == 1:
            self.directionRefreshCounter = 15
        self.normal_AI([x, y])



class SmallLongShooter():
    def __init__(self, sprite, x, y, projsprite, sx, sy, gamehandler, projbox):
        self.x = x
        self.y = y
        self.size_x = sx
        self.size_y = sy
        self.hitbox = pygame.Rect(self.x, self.y, self.size_x, self.size_y)
        self.sprite = pygame.image.load(sprite)
        self.hELTH = 50
        self.damage = 30
        self.bulletlist = []
        self.living = False
        self.friendly = False
        self.knock = True
        self.amtKnock = 0
        self.gamehandler = gamehandler
        self.gamehandler.add_custom_user(self)
        self.gun = Gun("smallLongBullet.png", [self.x, self.y, projbox[0], projbox[1]], "down", 8, 4, self, [self.x, self.y], 20, 10, 0, False, None, None, None, 60, 1)
        self.dirMode = 0
    def normal_AI(self, player_pos):
        if self.dirMode >= 0 and self.dirMode <= 24:
            if self.x >= player_pos[0]:
                print("x>")
                self.x -= random.randint(5, 17)
            elif self.x < player_pos[0]:
                self.x += random.randint(5, 17)
                print("x<")
            if self.y < player_pos[1] + 200:
                self.y += random.randint(3, 12)
                print("ranged")
            elif self.y >= player_pos[1] + 200:
                self.y -= random.randint(0, 8)
                print("unranged")
            self.dirMode += 1
        elif self.dirMode >= 28 and self.dirMode <= 34:
            self.x += random.randint(-17, 17)
            self.y += random.randint(-3, 3)
            self.dirMode += 1
        else:
            self.dirMode = 1

        if bool(checkInBoundsY(self.y)) == True:
            self.y = checkInBoundsY(self.y)

    def player_movement(self, player_pos):
        self.normal_AI(player_pos)
    def take_damage(self, knockback, damage):
        self.hELTH -= damage
        self.y -= knockback + knockback / 2
    def get_destroyed(self, player_coor):
        print("destroyed")
        if self.living == False:
            self.living = False
        self.gamehandler.remove(self)
    def collision_player(self, player_coor):
        self.knock = True
        self.hELTH - 25
    def every_frame_event(self):
        if random.randint(0, 25) == 13:
            self.gun.shoot()
        self.gun.every_frame_event()
        grb.screen.blit(self.sprite, [self.x, self.y])
        self.hitbox = pygame.Rect(self.x, self.y, self.size_x, self.size_y)
        self.bulletlist = self.gun.get_bullets()
        if self.amtKnock < 11 and self.knock:
            self.y -= 8
        elif amtKnock >= 11:
            self.knock = False
            self.amtKnock = 0
    def bullet_incoming(self, bx, by):
        if self.x > bx:
            self.x -= random.randint(1, 15)
        elif self.x < bx:
            self.x += random.randint(1, 15)
        else:
            self.x += random.randint(-13, 15)


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
        print("append cutscene text")  
        cutsceneTextList.append(EachLine)
    for eachVar in cutsceneTextList:
        if fastCutscene == False:
            print("creating sprites")
            cutscene1Text.append(AnimText(eachVar, grb.bigfont, [255, 255, 255], 100, 250, 1))
    for currentcutText in cutscene1Text:
        print(fastCutscene)
        if fastCutscene == False:
            cutsceneWait = 0
            for current_length in range(0, currentcutText.gtLen()):
                delayAmountMeasurer = KeyUser(pygame.K_RETURN, modeCut1Event, delayCutsceneFrame)
                grb.screen.fill((0, 0, 0))
                if fastCutscene == False:
                    print("animating")
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
    episode1()

def drawScrollingBackground(): 
        global scrollVar, subScrollVar, ScrollIMPF
        backgroundSprite = TempObject("backdrop.jpg", 50, scrollVar)
        foregroundSprite = TempObject("subbackdrop.jpg", 50, subScrollVar)
        movementVar = int(CalPixelSpeed(10))
        scrollVar += movementVar
        subScrollVar += movementVar
        if subScrollVar >= 720:
            subScrollVar = -720
            scrollVar = 0

            
        elif scrollVar >= 720:
            scrollVar = -720
            subScrollVar = 0


        backgroundSprite.blit()
        foregroundSprite.blit()


def spawnEnemyRoutines():
    global waveMode, waveFrameCounter, modeEpi1Event

    if waveMode == 0:
        waveFrameCounter += 1
        if waveFrameCounter == 150:
            waveFrameCounter = 0
        waveMode = 1
        
        waveMode = 1
    elif waveMode == 1:
        for x in range(0, 6):
            newEnemy = TinyFastEnemy("tinyfast-ep1.png", random.randint(310, 620), 60, None, 64, 64, modeEpi1Event)
        waveMode = 2
    elif waveMode == 2:
        if bool(modeEpi1Event.get_custom_objects()) == False:
            waveMode = 3
            print("wavemode3")
    elif waveMode == 3:
        for x in range(0, 2):
            newEnemy = SmallLongShooter("smalllongshoot.png", random.randint(130, 700), 620, "smallLongBullet.png", 66, 72, modeEpi1Event, [32, 32])
        for x in range(0, 3):
            newEnemy = TinyFastEnemy("tinyfast-ep1.png", random.randint(310, 620), 60, None, 64, 64, modeEpi1Event)
        waveMode = 4
    elif waveMode == 4:
        if bool(modeEpi1Event.get_custom_objects()) == False:
            waveMode = 0


def episode1():
    global scrollVar, subScrollVar, playerShip, waveMode, waveFrameCounter, modeEpi1Event
    scrollVar = 720
    subScrollVar = 0
    waveMode = 0
    waveFrameCounter = 0
    pygame.mixer.quit()
    pygame.mixer.init(frequency=44100)
        
    modeEpi1Event = GameHandler()
    playerShip = Ship([pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_l], "delta1.GIF", modeEpi1Event, 6, 600, 600, 80, 80, "up", "blastershot.PNG", [600, 100, 24, 32], 20, 8, 14, 50, 12, 60, False, "BlasterShoot.wav", "GunReload.wav", "BulletIn.wav", "damaged.wav", 4000, 1)
    playerHPBar = HPBar("ship-hp-bar.PNG", playerShip.get_hp(), 500, 770, 100, [50, 255, 100], 50, 70)
    epi1Music = Sound("Episode1Music.ogg", grb.musicchannel)
    epi1Music.multiplay(-1)

    episode1On = True
    episodePhaseVar = 0
    frameType = 'normal'
    for x in range(0, 15):
        grb.gameClock.tick(24)
    while episode1On:
        grb.screen.fill((30, 30, 30))
        drawScrollingBackground()
        ammoDisp = Text("Ammo Left: " + str(playerShip.gun.get_ammo_left()), grb.medfont, [255, 255, 255], 800, 350)
        coolDownDisp = Text("Cooling Down: " + str(playerShip.gun.coolbool), grb.medfont, [200, 255, 255], 800, 415)
        playerHPBar.update_hp(playerShip.get_hp())
        modeEpi1Event.custom_event_use()  
        spawnEnemyRoutines()
        playerShip.blit()
        pygame.display.flip()
        grb.gameClock.tick(30)
        if grb.gamemode == "gameover":
            break










def episode2():
    pass



#cutscene1()
#episode1()



