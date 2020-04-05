
import pygame, sys
import grb

# objects and classes, gamma ray battle code 3

#print("objects and classes init")

def getCustomEvents():
    global listOfCustomEvents
    listOfOut = []
    for eve in grb.listOfCustomEvents:
        listOfOut.append(eve)
    return listOfOut
def getAllEvents():
    global listOfCustomEvents
    listOfEventsOut = []
    for event in pygame.event.get():
        listOfEventsOut.append(event)  
    for ev2 in grb.listOfCustomEvents:
        listOfEventsOut.append(ev2)
    grb.lisOfCustomEvents = []
    return listOfEventsOut



def CalPixelSpeed(px):
    global gameClock
    fps = grb.gameClock.get_time()
    TTrueSpeed = px / fps * 100
    #TTrueSpeed = truespeed - truespeed * 2
    return TTrueSpeed



class Sound():
    def __init__(self, filename, channel):
        self.sound = pygame.mixer.Sound(filename)
        if channel == grb.sfxchannel:
            self.volvar = "sfx"
            self.sound.set_volume(grb.sfxvolume)
        elif channel == grb.musicchannel:
            self.volvar = "music"
            self.sound.set_volume(grb.musicvolume)
        self.channel = channel
    def play(self):
        if self.volvar == "sfx":
            self.channel.set_volume(grb.sfxvolume)    
        else:
            self.channel.set_volume(grb.musicvolume)
        self.sound.play()
        if self.volvar == "sfx":
            self.channel.set_volume(grb.sfxvolume)
        else:
            self.channel.set_volume(grb.musicvolume)
    def stop(self):
        self.sound.stop()
    def multiplay(self, parameter):
        self.sound.play(parameter)

class Nothing:
    def __init__(self):
        pass
    def blit(self):
        print("nothing is blit")




selected = Sound("select.wav", grb.sfxchannel)
selectxp = Sound("selectxp.ogg", grb.sfxchannel)
menumusic = Sound("menumusic.ogg", grb.musicchannel)

class Object():
    def __init__(self, image, x, y):
        self.sprite = pygame.image.load(image)
        self.x = x
        self.y = y
        grb.screen.blit(self.sprite, [self.x, self.y])
    def update(self, nex, ney):
        moveX = self.x - nex
        moveY = self.y - ney
        trueMoveX = CalPixelSpeed(moveX)
        trueMoveY = CalPixelSpeed(moveY)
        newX = self.x + trueMoveX
        newY = self.y + trueMoveY
        self.x = newX
        self.y = newY
        grb.screen.blit(self.sprite, [self.x, self.y])
    def move(self, nx, ny):
        trueMoveX = CalPixelSpeed(nx)
        trueMoveY = CalPixelSpeed(ny)
        newX = self.x + trueMoveX
        newY = self.y + trueMoveY
        self.x = newX
        self.y = newY
        grb.screen.blit(self.sprite, [self.x, self.y])
    def change_pos(self, x, y):
        self.x = x
        self.y = y
        grb.screen.blit(self.sprite, [self.x, self.y])

 
class TempObject():
    # Temporary object that doesn't grb.screen blit when instance is called
    def __init__(self, image, x, y):
        self.sprite = pygame.image.load(image)
        self.x = x
        self.y = y
    def blit(self):
        grb.screen.blit(self.sprite, [self.x, self.y])
    def update(self, x, y):
        grb.screen.blit(self.sprite, [self.x, self.y])


class Text():
    def __init__(self, text, font, color, x, y):
        self.x = x
        self.y = y
        self.text = text
        self.sprite = font.render(self.text, True, color)
        grb.screen.blit(self.sprite, [self.x, self.y])
    def update(self, text, font, color):
        self.text = text
        self.x = x
        self.y = y
        self.sprite = font.render(self.text, True, color)
        grb.screen.blit(self.sprite, [self.x, self.y])
    def move(self, nex, ney):
        moveX = self.x - nex
        moveY = self.y - ney
        trueMoveX = CalPixelSpeed(moveX)
        trueMoveY = CalPixelSpeed(moveY)
        newX = self.x + trueMoveX
        newY = self.y + trueMoveY
        self.x = newX
        self.y = newY
        grb.screen.blit(self.sprite, [self.x, self.y])
    def blit(self):
        grb.screen.blit(self.sprite, [self.x, self.y])

class EventHandler():
    def __init__(self):
        self.keyobjectslist = []
    def add_key_user(self, user):
        self.keyobjectslist.append(user)
    def key_event_use(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key  == pygame.K_ESCAPE:
                    sys.exit()
                for objects in self.keyobjectslist:
                    objects.use_down_event(event)
            if event.type == pygame.KEYUP:
                for objects in self.keyobjectslist:
                    objects.use_up_event(event)
            if event.type == pygame.QUIT:
                #print("pygame.quit")
                sys.exit()
class GameHandler(EventHandler):
    def __init__(self):
        super().__init__()
        self.EnemiesList = []

    def key_event_use(self):
        super().key_event_use()
        self.playerShip.every_frame_event()

    def add_custom_user(self, user):
        self.EnemiesList.append(user)

    def addShip(self, newship):
        self.playerShip = newship

    def get_custom_objects(self):
        return self.EnemiesList

    def custom_event_use(self):
        self.playerShip.every_frame_event()
        #print("eveyrframe")
        for objects in self.EnemiesList:
            objects.every_frame_event()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key  == pygame.K_ESCAPE:
                    sys.exit()
                for objects in self.keyobjectslist:
                    objects.use_up_event(event)
            if event.type == pygame.KEYUP:
                for objects in self.keyobjectslist:
                    objects.use_down_event(event)
            elif event.type == pygame.QUIT:
                #print("pygame.quit")
                sys.exit()
            for objects in self.EnemiesList:
                if pygame.Rect.colliderect(self.playerShip.hitbox, objects.hitbox) == True:
                    if objects.friendly == False:
                        self.playership.take_damage(objects.damage)
                        objects.collision_player(self.playerShip.get_pos())
                for bullet in self.playerShip.get_bullets():
                    if pygame.Rect.colliderect(bullet.hitbox. objects.hitbox):
                        objects.take_damage(self.playerShip.get_knockback(), self.playership.get_damage())
                for bullet in objects.bulletlist:
                    if pygame.Rect.colliderect(bullet.hitbox, self.playerShip.hitbox):
                        self.playerShip.take_damage(objects.damage)
                if objects.hELTH <= 0:
                    objects.get_destroyed()

        



class GameObject(Object):
    def __init__(self, x, y, sizex, sizey, imgfilename):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(imgfilename)
        self.hitbox = pygame.Rect(self.x, self.y, sizex, sizey)
        grb.screen.blit(self.sprite, [self.x, self.y])
    def move(self, x, y):
        self.x = x
        self.y = y
        self.hitbox.move_ip(self.x, self.y)
        grb.screen.blit(self.sprite, [self.x, self.y])
    def test_collision(self, rectOrGameobj, object):
        if rectOrGameobj == "rect":
            if self.hitbox.colliderect(object) == True:
                return True
            else:
                return False
        elif rectOrGameobj == "gameobj" or rectOrGameobj == "gameobject":
            if self.hitbox.colliderect(object.hitbox) == True:
                return True
            else:
                return False
    def blit(self):
        grb.screen.blit(self.sprite, [self.x, self.y])
                
class KeyUser():
    def __init__(self, key, eventhandler, function):
        self.func = function
        self.key = key
        self.eventhandler = eventhandler
        self.eventhandler.add_key_user(self)
    def use_down_event(self, event):
        if bool(self.key) == True:
                if event.key == self.key:
                    self.func()
        else:
                self.func()
    def use_up_event(self, event):
        pass 




class Ship(GameObject):
    def __init__(self, keylist, filename, eventhandler, speedPerFrame, x, y, sizex, sizey, orient, bulletsprite, bulletrect, bulletspeed, bulletrate, bulletrange, bulletdmg, ammocapacity, reloadtime, auto, shootSound, reloadSound, reloadStartSound, damagedSound, hitpoints):
        # the keylist should go up, down, left, right, same as most
        # early home computer's cursor keys.
        self.handler = eventhandler
        self.handler.addShip(self)
        self.handler.add_key_user(self)
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(filename)
        self.size_x = sizex
        self.size_y = sizey
        self.hitbox = pygame.Rect(x, y, sizex, sizey)
        self.keyup = keylist[0]
        self.keydown = keylist[1]
        self.keyleft = keylist[2]
        self.keyright = keylist[3]
        self.keyshoot = keylist[4]
        self.speed = speedPerFrame
        shootsound = Sound(shootSound, grb.sfxchannel)
        reloadsound = Sound(reloadSound, grb.sfxchannel)
        reloadstartsound = Sound(reloadStartSound, grb.sfxchannel)
        self.damagedSound = Sound(damagedSound, grb.sfxchannel)
        self.gun = Gun(self.keyshoot, self.handler, bulletsprite, bulletrect, orient, bulletspeed, bulletrate, self, [self.x, self.y], bulletrange, ammocapacity, reloadtime, auto, shootsound, reloadsound, reloadstartsound, bulletdmg)
        self.orient = orient
        self.usualspeed = speedPerFrame
        self.dx = 0
        self.dy = 0
        self.hp = hitpoints
        self.movedThisFrame = False
    def use_down_event(self, event):
        if event.key == self.keydown:
            #print("down downkey")
            self.dy = CalPixelSpeed(self.usualspeed)
            self.movedThisFrame = True
        elif event.key == self.keyup:
            #print("up downkey")
            self.dy = CalPixelSpeed(self.usualspeed - self.usualspeed * 2)
            self.movedThisFrame = True
        if event.key == self.keyright:
            #print("right downkey")
            self.dx = CalPixelSpeed(self.usualspeed)
            self.movedThisFrame = True
        elif event.key == self.keyleft:
            #print("left downkey")
            self.dx = CalPixelSpeed(self.usualspeed - self.usualspeed * 2)
            self.movedThisFrame = True
    def use_up_event(self, event):
        if event.key == self.keyup or event.key == self.keydown:
            self.dy = 0
        if event.key == self.keyleft or event.key == self.keyright:
            self.dx = 0
    def every_frame_event(self):
        self.movedThisFrame = False
        #print("player every frame")
        if self.x < 800 and self.x > 230:
            self.x += self.dx
        elif self.x >= 800:
            self.x = 780
        elif self.x < 230:
            self.x = 250
        else:
            raise ValueError("Ship out of bounds")

        if self.y < 700 and self.y > 50:
            self.y += self.dy
        elif self.y >= 700:
            self.y = 680
        elif self.y <= 50:
            self.y = 70
        else:
            raise ValueError("Ship out of bounds")

        self.gun.every_frame_event()
    def shoot(self):
        self.gun.shoot()
    def take_damage(self, amount_of_damage):
        self.hp -= amount_of_damage
        self.damagedSound.play()
    def get_pos(self):
        return [self.x, self.y]
    def get_bullets(self):
        return self.gun.bulletlist
    def get_knockback(self):
        return self.gun.bulletvelospeed / (self.gun.cooltime / 2)
    def get_damage(self):
        return self.gun.amountOfDamage
    def moved(self):
        return self.movedThisFrame


class Bullet(GameObject):
    def __init__(self, sprite, sizex, sizey, horizOrVerti, x, y, gunparent):
        self.sprite = pygame.image.load(sprite)
        self.x = x
        self.y = y
        self.hitbox = pygame.Rect(self.x, self.y, sizex, sizey)
        self.direction = horizOrVerti
        self.gun = gunparent
        self.shootcounter = 0
        self.range = self.gun.range
        self.shot = False
        #self.shot is the variable that tells if the bullet still exists in the map or not.
    def go_fire(self):
        print(self.shootcounter)
        self.shootcounter += 1
        print("gofire")
        if self.shootcounter <= self.range:
            if self.shot == False:
                self.shot = True
            if self.direction == "up":
                self.y -= CalPixelSpeed(self.gun.speed)
            elif self.direction == "down":
                self.y += CalPixelSpeed(self.gun.speed)
            elif self.direction == "left":
                self.x -= CalPixelSpeed(self.gun.speed)
            elif self.direction == "right":
                self.x += CalPixelSpeed(self.gun.speed)
            else:
                raise ValueError("Custom error: ship's direction (horizOrVerti) var set to wrong value")
            print("shotmov")
            grb.screen.blit(self.sprite, [self.x, self.y])
        else:
            self.shot = "spent"
            self.gun.bulletlist.remove(self)
            print("spent")
    def shot(self):
        return self.shot
class Gun():
    def __init__(self, shootkey, eventhandler, bulletsprite, bulletX_Y_Sx_Sy, horizOrVerti, speed, firespeed, parent_ship, pos, rangegun, magSize, reloadTime, automatic, shootsound, reloadsound, reloadstartsound, bulletdamage):
        eventhandler.add_key_user(self)
        self.auto = automatic
        self.shootkey = shootkey
        self.parentship = parent_ship
        self.bulletvelospeed = speed
        self.firespeed = firespeed
        self.bulletlist = []
        self.bulletsprite = bulletsprite
        self.bulletRectPara = bulletX_Y_Sx_Sy
        self.direction = horizOrVerti
        self.range = rangegun
        self.speed = speed
        self.cooltime = firespeed
        self.autoshooting = None
        self.currentcooldown = 0
        self.coolbool = False
        self.magSize = magSize
        self.magVar = self.magSize
        self.reloading = False
        self.currentReloadTime = 0
        self.reloadtime = reloadTime
        self.shootsound = shootsound
        self.reloadsound = reloadsound
        self.reloadstartsound = reloadstartsound
        self.amountOfDamage = bulletdamage
        print("autofalse init")
    def shoot(self):
        if self.coolbool == False and self.reloading == False:
            newbullet = Bullet(self.bulletsprite, self.bulletRectPara[0], self.bulletRectPara[1], self.direction, self.bulletRectPara[2], self.bulletRectPara[3], self)
            if bool(self.shootsound) == True:
                self.shootsound.play()
            newbullet.change_pos(self.parentship.x + self.parentship.size_x / 3, self.parentship.y)
            self.magVar -= 1
            self.bulletlist.append(newbullet)
            newbullet.go_fire()
            self.coolbool = True

    def reload(self):
        self.reloading = True
        self.reloadstartsound.play()

    def use_down_event(self, event):
        if self.auto == True:
            print("auto")
            if event.key == self.shootkey:
                print("autoed")
                self.autoshooting = True
                print(str(self.autoshooting) + "beg")

        else:
            print("manual")
            if event.key == self.shootkey and self.magVar > 0 and self.coolbool == False:
                self.shoot()
                self.coolbool = True
            elif self.magVar <= 0:
                print("empty clip")
            elif self.coolbool == True:
                print("still cooling")
    def every_frame_event(self):
        print(str(self.autoshooting))
        for bullet in self.bulletlist:
            bullet.go_fire()
        if self.coolbool == True:

            if self.currentcooldown < self.cooltime:
                self.currentcooldown += 1

            elif self.currentcooldown >= self.cooltime:
                self.coolbool = False
                self.currentcooldown = 0

        if self.reloading == True:

            if self.currentReloadTime < self.reloadtime:
                self.currentReloadTime += 1

            elif self.currentReloadTime >= self.reloadtime:

                self.currentReloadTime = 0
                self.reloading = False
                self.magVar = self.magSize
                self.reloadsound.play()
        else:
            if self.magVar <= 0:
                self.reload()

        if self.autoshooting == 1:
            print("autotriggered")
            if self.magVar > 0 and self.coolbool == False:
                self.shoot()


    def get_ammo_left(self):
        return self.magVar

    def get_cooldown(self):
        return self.coolbool

    def use_up_event(self, event):
        if self.auto == True and event.key == self.shootkey:
            print("upkey")
            self.autoshooting = False
        
class TempText(Text):
    def __init__(self, text, font, color, x, y):
    # Temporary text that doesn't grb.screen blit when instance is called
        self.x = x
        self.y = y
        self.text = text
        self.sprite = font.render(self.text, True, color)
    def blit(self):
        grb.screen.blit(self.sprite, [self.x, self.y])


class BigText():
    def __init__(self, textlist, font, color, x, y, linespace, temp, headFont, headColor, heading):
        self.textspritelist = []
        #print(heading)
        self.headtext = heading
        if type(self.headtext) is str:
            #print("heading str")
            if temp == False:
                self.heading = Text(heading, headFont, headColor, x, y + 15)
            elif temp == True:
                self.heading = TempText(heading, headFont,headColor, x, y - 40)
        else:
            #print("heading not str")
            self.heading = Nothing()
        crntTextLen = 0
        for textnew_ in textlist:
            if temp == False:
                self.textspritelist.append(Text(textnew_, font, color, x, y + linespace * crntTextLen))
            elif temp == True:
                self.textspritelist.append(TempText(textnew_, font, color, x, y + linespace * crntTextLen))
            crntTextLen += 1
    def blit(self):
        self.heading.blit()
        for textbl in self.textspritelist:
            textbl.blit()

class Selector():
    def __init__(self, keyback, keyforth, eventhandler, itemList):
        self.list_of_items = itemList
        self.centerval = 0 
        self.keyback = keyback
        self.keyforth = keyforth
        self.handler = eventhandler
        self.handler.add_key_user(self)
    def add_item(self, objectNew):
        self.list_of_items.append(objectNew)
    def blit(self):
        self.list_of_items[self.centerval].blit()
    def use_down_event(self, event):
        #print(self.centerval)
        if event.key == self.keyback:
            selected.play()
            if self.centerval > 0: 
                self.centerval -= 1
            else:
                self.centerval = len(self.list_of_items) - 1
        elif event.key == self.keyforth:
            selected.play()
            if self.centerval < len(self.list_of_items) - 1:
                self.centerval += 1
            else:
                self.centerval = 0 
    def get_selected(self):
        return self.centerval
    def use_up_event(self, event):
        pass



class AnimText():
    def __init__(self, text, font, color, x, y, animSpd):
        self.text = text
        self.color = color
        self.font = font
        self.x = x
        self.y = y
        self.animSpd = animSpd
        self.characterCurrent = 0
        self.frameCounter = 0
    def animate_blit(self):
        self.frameCounter += 1
        if self.characterCurrent < len(self.text) and self.frameCounter == self.animSpd:
            self.characterCurrent += 1
            self.frameCounter = 0
            self.sprite = self.font.render(self.text[0:self.characterCurrent], True, self.color)
            grb.screen.blit(self.sprite, [self.x, self.y])
    def blit(self):
        self.sprite = font.render(self.text, True, self.color)
        super.blit()
    def gtLen(self):
        return len(self.text)
    def resetAnim():
        self.characterCurrent = 0

def showInfoBoard(list_of_things_to_blit, x, y):
    global infoOn, medfont
    def closeBoard():
        global infoOn
        infoOn = False
    infoBoard = pygame.image.load("infoIMG.PNG")
    infoOn = True
    modeInfoEvent = EventHandler()
    while infoOn:
        keyBackUser = KeyUser(pygame.K_b, modeInfoEvent, closeBoard)
        grb.screen.blit(infoBoard, [x, y])
        for obje in list_of_things_to_blit:
            obje.blit()
        backText = Text("[B] Ok", grb.medfont, [75, 255, 255], x + 100, y + 350)
        modeInfoEvent.key_event_use()
        pygame.display.flip()



def OpenMenu():
    #print("opened menu")
    global gamemode
    global selected
    global menumusic
    pygame.mixer.stop()
    selected.play()
    menumusic.multiplay(-1)
    grb.gamemode = 3
    #print("grb.gamemode is 3")






















#print("objects")

