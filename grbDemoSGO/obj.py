
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

def checkInBoundsX(x):
    if x < 750 and x > 80:
        return None
    elif x >= 800:
        return 730
    elif x < 80:
        return 100
def checkInBoundsY(y):
    if y < 700 and y > 50:
        return None
    elif y >= 700:
        return 680
    elif y <= 50:
        return 70
 


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
                    objects.use_down_event(event)
            if event.type == pygame.KEYUP:
                for objects in self.keyobjectslist:
                    objects.use_up_event(event)
            elif event.type == pygame.QUIT:
                #print("pygame.quit")
                sys.exit()

        for objects in self.EnemiesList:
            if self.playerShip.hitbox.colliderect(objects.hitbox) == True:
                if objects.friendly == False:
                    self.playerShip.take_damage(objects.damage)
                    objects.collision_player(self.playerShip.get_pos())
            for bullet in self.playerShip.get_bullets():
                if bullet.hitbox.colliderect(objects.hitbox) == True:
                    objects.take_damage(self.playerShip.get_knockback(), self.playerShip.get_damage())
                    print("bullet collision")
            for bullet in objects.bulletlist:
                if bullet.hitbox.colliderect(self.playerShip.hitbox) == True:
                    self.playerShip.take_damage(objects.damage)
            if self.playerShip.moved():
                objects.player_movement(self.playerShip.get_pos())
            else:
                objects.normal_AI(self.playerShip.get_pos())
            if objects.hELTH <= 0:
                objects.get_destroyed(self.playerShip.get_pos())
        if self.playerShip.hp <= 0:
            grb.gamemode = "gameover"
            
    def remove(self, object__):
        if object__ in self.EnemiesList:
            self.EnemiesList.remove(object__)

        



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
        self.hitbox = pygame.Rect(self.x, self.y, self.size_x, self.size_y)
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
            print("bebebebebbbex")
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

        if bool(checkInBoundsX(self.x)):
            self.x = checkInBoundsX(self.x)
        else:
            self.x += self.dx
        if bool(checkInBoundsY(self.y)):
            self.y = checkInBoundsY(self.y)
        else:
            self.y += self.dy

        self.gun.every_frame_event()
        self.hitbox = pygame.Rect(self.x, self.y, self.size_x, self.size_y)


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
    def get_hp(self):
        return self.hp


class Bullet(GameObject):
    def __init__(self, sprite, x, y, horizOrVerti, sizex, sizey, gunparent):
        self.sprite = pygame.image.load(sprite)
        self.x = x
        self.y = y
        self.size_x = sizex
        self.size_y = sizey
        self.hitbox = pygame.Rect(self.x, self.y, self.size_x, self.size_y)
        self.direction = horizOrVerti
        self.gun = gunparent
        self.shootcounter = 0
        self.range = self.gun.range
        self.shot = False
        #self.shot is the variable that tells if the bullet still exists in the map or not.
    def go_fire(self):
        self.shootcounter += 1
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
            self.hitbox = pygame.Rect(self.x, self.y, self.size_x, self.size_y)
            grb.screen.blit(self.sprite, [self.x, self.y])
        else:
            self.shot = "spent"
            self.gun.bulletlist.remove(self)
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
            if event.key == self.shootkey:
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

class HPBar():
    def __init__(self, sprite, maxHP, spritelength, x, y, colorlist, height, true_height):
        self.sprite = pygame.image.load(sprite)
        self.x = x
        self.y = y
        self.height = height
        self.theight = true_height
        self.maxHP = maxHP
        self.length = spritelength
        self.ratio_hp_length = self.maxHP / self.length
        self.currentHP = self.maxHP
        self.hpBar = None
        self.color = colorlist
        self.normcolor = colorlist
    def blit(self):
        grb.screen.blit(self.sprite, [self.x, self.y])
        if self.currentHP <= self.maxHP / 4.2:
            self.color = [255, 25, 25]
        else:
            self.color = self.normcolor

        pygame.draw.line(grb.screen, self.color, [self.x, self.y + self.theight / 2], [self.x + self.currentHP / self.ratio_hp_length, self.y + self.theight / 2], self.height)
    def update_hp(self, new_hp):
        self.currentHP = new_hp
        self.blit()
        




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

