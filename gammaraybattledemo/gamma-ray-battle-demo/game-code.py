import sys, time, random
import pygame
global tspeed
tspeed = 0
difsame = 0
fireconfirm = False
bullethitast = False
recoil = True
cooldown = 0
recool = 0
mony = 100
mondir = False
monhere = False
bulletx = 0
enbutime = 0
enbuy = 0
enbux = 0
asthit1 = 0
asthit2 = 0
score = 0
fc = 8008
astfallpoint = None
dmgedmt = False
dmgedmon = False
GAMEMODE_TITLE = 1
GAMEMODE_TUTORIAL = 2
GAMEMODE_LOAD = 3
GAMEMODE_GAME = 4
GAMEMODE_OVER = 5
GAMEMODE_SETTINGS = -1
gamemode = GAMEMODE_TITLE
monhb = None

# don't tinker with this code
pygame.display.init()
pygame.font.init()
pygame.mixer.init(frequency=48000)
text = pygame.font.SysFont(None, 25, bold=False, italic=False)
bigtext = pygame.font.SysFont(None, 45, bold=False, italic=False)
screen = pygame.display.set_mode((1080, 720), pygame.FULLSCREEN)
blk = pygame.mixer.Sound("block.wav")
print ("1080x720 version. Version 1.0 demo, enjoy.")
start = pygame.image.load("startshow.png")
title = pygame.image.load("logo.png")
tutorial = pygame.image.load("htp.png")
startmusic = pygame.mixer.Sound("8B.wav")
startmusic.play()
slct = pygame.mixer.Sound("select.wav")
vend = pygame.image.load("ttlend.png")
ready = pygame.image.load("gready.png")
backdrop = pygame.image.load("backdrop.png")
sparedrop = pygame.image.load("backdrop2.jpg")
atkmusic = pygame.mixer.Sound("invasion-1.wav")
ship = pygame.image.load("ship-active.GIF")
asteroid = pygame.image.load("asteroid.png")
cpr = pygame.image.load("copyright.png")
dmgd = pygame.mixer.Sound("damaged.wav")
hrt1 = pygame.image.load("heart.png")
hrt2 = pygame.image.load("heart.png")
hrt3 = pygame.image.load("heart.png")
warn = pygame.image.load("dying.png")
sett = pygame.image.load("settings.png")
bullet = pygame.image.load("bullet.png")
shootsound = pygame.mixer.Sound("lasershoot.wav")
aln = pygame.image.load("a.png")
enbu = pygame.image.load("enbullet.png")
boom = pygame.mixer.Sound("boom.wav")
togger = pygame.image.load("togglespeed.png")
def speedset():
    global tspeed
    if tspeed == 3:
        tspeed = 1
    else:
        tspeed += 1
   
while True:
    # common processes
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    if gamemode == GAMEMODE_TITLE: 
        screen.fill((0, 0, 0))
        screen.blit(title,[200, 100])
        screen.blit(start,[300, 500])
        screen.blit(cpr, [400, 680])
        screen.blit(sett, [400, 400])
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    gamemode = GAMEMODE_TUTORIAL
                    pygame.mixer.stop()
                    screen.fill((0, 0, 0))
                    slct.play()
                    pygame.display.flip()
                if event.key == pygame.K_q:
                    gamemode = -1



    elif gamemode == GAMEMODE_SETTINGS:
        screen.fill((0, 0, 0))
        if tspeed == 0 or tspeed == 1:
            togsign = 'Default'
        elif tspeed == 2:
            togsign = 'Slow'
        else:
            togsign = 'Very slow'
        togstate = bigtext.render(togsign, False, (255, 255, 255))
        back = bigtext.render('[B] Back', False, (255, 255, 255))
        screen.blit(back, [540, 500])
        screen.blit(togger, [100, 100])
        screen.blit(togstate, [100, 300])
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    speedset()
                    slct.play()
                if event.key == pygame.K_d:
                    if difsame == 0:
                        difsame = 1
                    else:
                        difsame = 0
                if event.key == pygame.K_b:
                    gamemode = 1



    elif gamemode == GAMEMODE_TUTORIAL:
        screen.blit(tutorial,[25, 0])
        screen.blit(vend, [100, 600])
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_v:
                    slct.play()
                    screen.fill((0, 0, 0))
                    pygame.display.flip()
                    gamemode = 4
                    atkmusic.play()
                    global bdpos 
                    bdpos = 0
                    global sdpos
                    sdpos = -720
                    global shippos
                    shippos = 540
                    global asy
                    asy = -100
                    global astfalling
                    astfalling = 0
                    lives = 3
                    bullety = 0
                    monhealth = 3




    elif gamemode == GAMEMODE_GAME: 
        screen.fill((0, 0, 0))
        
        scoretext = str(score)
        scoreboard = text.render(scoretext, False, (255, 255, 255))  
        if lives == 3:
            screen.blit(hrt1, [10, 100])
            screen.blit(hrt2, [10, 175])
            screen.blit(hrt3, [10, 250])
        elif lives == 2:
            screen.blit(hrt1, [10, 100])
            screen.blit(hrt2, [10, 175])
        elif lives == 1:
            screen.blit(hrt1, [10, 100])
        elif lives == 0:
            screen.blit(warn, [10, 100])
        elif lives <= -1:
            gamemode = 5
            pygame.mixer.stop()
        global astchance
        speed = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed = -5
            if event.key == pygame.K_RIGHT:
                speed = 5 
            if event.key == pygame.K_SPACE:
                if fireconfirm == False and recoil == True and cooldown < 8:
                    fireconfirm = True
                    cooldown += 1
                    recoil = False
                    shootsound.play()
                    bulletx = shippos + 25
                    bullety = 600
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                speed = 0
            if event.key == pygame.K_SPACE:
                recoil = True
        if cooldown >= 8:
            recool += 1
        if recool >= 300:
            cooldown = 0
            recool = 0
        if (bool(cooldown)) == True:
            if cooldown >= 8:
                ammoplace = 'Reloading'
            else:
                if cooldown == 0:
                    ammoplace = 8
                if cooldown == 1:
                    ammoplace = 7
                if cooldown == 2:
                    ammoplace = 6
                if cooldown == 3:
                    ammoplace = 5
                if cooldown == 4:
                    ammoplace = 4
                if cooldown == 5:
                    ammoplace = 3
                if cooldown == 6:
                    ammoplace = 2
                if cooldown == 7:
                    ammoplace = 1
            ammofinal = "Ammo left: {}".format(ammoplace)
        else:
            ammoplace = 8
            ammofinal = "Ammo left: {}".format(ammoplace)
        ammoleft = text.render(ammofinal, False, (255, 255, 255))
        screen.blit(ammoleft, [10, 500])
        shippos += speed
        if shippos > 800:
            shippos = 800
        if shippos < 200:
            shippos = 200
        global backdropspeed
        backdropspeed = 5
        bdpos += backdropspeed
        sdpos += backdropspeed
        if bdpos >= 720:
            bdpos = -720
        if sdpos >= 720:
            sdpos = -720
        shiphit1 = shippos + 160
        shiphit2 = shippos - 10
        screen.blit(backdrop, [175, bdpos])
        screen.blit(sparedrop, [175, sdpos])
        screen.blit(ship, [shippos, 600])
        screen.blit(scoreboard, [30, 400])
        shiphb = pygame.Rect(shippos, 600, 80, 80)
        if (bool(asy)) == True and (bool(astfallpoint)) == True:
            asthb = pygame.Rect(astfallpoint, asy, 250, 250)
        if fireconfirm == True:
            fc = 4004
            screen.blit(bullet, [bulletx, bullety])
            bullety -= 20
            bullethb = pygame.Rect(bulletx, bullety, 24, 24)
            if bullety <= 0:
                fireconfirm = False
            if bullethb.colliderect(asthb) == True:
                blk.play()
                bullethitast = True
        if astfalling == 0:
            astchance = random.randint(0, 120)
            astfallpoint = random.randint(200, 800)
        if tspeed == 2 and difsame == 1:
            astfallspeed = random.randint(6, 9)
        if tspeed == 3 and difsame == 1:
            astfallspeed = random.randint(8, 11)
        else:
            astfallspeed = random.randint(4, 7)
        if astchance == 1 or astfalling == 1:
            astfalling = 1
            asy += astfallspeed
            if bullethitast == False or bullethitast == None:
                screen.blit(asteroid, [astfallpoint, asy])
            else:
                asy -= 250
                fireconfirm = False
                bullethitast = False
            if asy >= 720:
                if dmgedmt == False:
                    score += 100
                    asy = -100
                    astfalling = 0
                else:
                    dmgedmt = False
                    asy = -100
                    astfalling = 0
            if shiphb.colliderect(asthb) == True:
                lives -= 1
                dmgedmt = True
                asy = 720
                dmgd.play()
        if monhere == False:
            moncould = random.randint(600, 765)
            monhealth = 3
            monx = random.randint(200, 800)
#easter egg?
        if moncould == 666:
            monhere = True
            screen.blit(aln, [monx, mony])
            monhb = pygame.Rect(monx, mony, 100, 100)
            if random.randint(0, 30) == 1:
                if mondir == False:
                    mondir = True
                else:
                    mondir = False
            if mondir == False:
                if shippos < monx:
                    if fireconfirm == True:
                        monx += 40
                    else:
                        monx -= 4
            else:
                if shippos > monx:
                    if fireconfirm == True:
                        monx -= 15
                    else:
                        monx += 4
            if enbutime <= 80:
                if (bool(monx)) == True:
                    enbux = monx
                    enbuy = mony + 50
                    enbutime += 1
            else:
                screen.blit(enbu, [enbux, enbuy])
                enbuy += 7
                if enbuy >= 720:
                    enbutime = 0
                    enbuy = mony
        if monx > 800:
            monx = 800
        elif monx < 200:
            monx = 200
        if fc == 4004 and (bool(monhb)) == True:
            if bullethb.colliderect(monhb) == True:
                monhealth -= 1
                bullety = 0
                boom.play()
                if monhealth <= 0:
                    monhere = False
                    score += 200
        enbuhb = pygame.Rect(enbux, enbuy, 48, 60)
        if tspeed == 2:
            time.sleep(0.006)
        if tspeed == 3:
            time.sleep(0.01) 
        if shiphb.colliderect(enbuhb) == True:
            dmgedmon = True
            lives -= 1
            enbuy = 720
            dmgd.play()
        pygame.display.flip()



    elif  gamemode == GAMEMODE_OVER: 
        screen.fill((0, 0, 0))
        gameovermsg = bigtext.render('''Game over. Your score is:''', False, (255, 255, 255))
        scoreboard = bigtext.render(scoretext, False, (255, 255, 255))
        nextis = bigtext.render('Retry: R. Quit game: E or the X at top-right.', False, (121, 255, 148))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    lives = 3
                    bdpos = 0
                    sdpos = -720
                    shippos = 540
                    asy = 0
                    score = 0
                    gamemode = GAMEMODE_TUTORIAL
                if event.key == pygame.K_e:
                    sys.exit()
        screen.blit(gameovermsg, [360, 260])
        screen.blit(scoreboard, [460, 360])
        screen.blit(nextis, [360, 460])
        pygame.display.flip()