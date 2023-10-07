import pygame

class GameObject(pygame.sprite.Sprite):
    def __init__(self, img_path):
        super().__init__()
        self.blood = 100
        self.image = img_path
        self.rect = self.image.get_rect()  
        self.ifAttacked = False
    #define attack in parent class so both weapon and monster can use directly
    def attack(self,attackTo):
        if self.rect.colliderect(attackTo.rect) and not self.ifAttacked:
            attackTo.blood -= self.attackPoint
            self.ifAttacked = True
        elif not self.rect.colliderect(attackTo.rect):
            self.ifAttacked = False
        

class Character(GameObject):
    def __init__(self, screen_rect, range_right, x_coor, y_coor, ID, weaponPoint):
        standing = pygame.image.load("CharacterStanding/standing.png")
        super().__init__(standing)
        self.speed = 4
        self.ID = ID
        self.rect.x = x_coor
        self.rect.y = y_coor
        self.range_left = screen_rect.left
        self.range_right = range_right
        self.weaponPoint = weaponPoint
        self.blood = 100

        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True
        
        self.char = pygame.image.load('CharacterStanding/standing.png')

        self.walkLeft = [
            pygame.image.load('CharacterMovingLeft/L1.png'),
            pygame.image.load('CharacterMovingLeft/L2.png'),
            pygame.image.load('CharacterMovingLeft/L3.png'),
            pygame.image.load('CharacterMovingLeft/L4.png'),
            pygame.image.load('CharacterMovingLeft/L5.png'),
            pygame.image.load('CharacterMovingLeft/L6.png'),
            pygame.image.load('CharacterMovingLeft/L7.png'),
            pygame.image.load('CharacterMovingLeft/L8.png'),
            pygame.image.load('CharacterMovingLeft/L9.png')]

        self.walkRight = [
            pygame.image.load('CharacterMovingRight/R1.png'),
            pygame.image.load('CharacterMovingRight/R2.png'),
            pygame.image.load('CharacterMovingRight/R3.png'),
            pygame.image.load('CharacterMovingRight/R4.png'),
            pygame.image.load('CharacterMovingRight/R5.png'),
            pygame.image.load('CharacterMovingRight/R6.png'),
            pygame.image.load('CharacterMovingRight/R7.png'),
            pygame.image.load('CharacterMovingRight/R8.png'),
            pygame.image.load('CharacterMovingRight/R9.png')]

    def redrawGameWindow(self, win):
        if self.walkCount >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(self.walkLeft[self.walkCount // 3], self.rect)
                self.walkCount += 1
            elif self.right:
                win.blit(self.walkRight[self.walkCount // 3], self.rect)
                self.walkCount += 1
        else:
            if self.right:
                win.blit(self.walkRight[0], self.rect)
            elif self.left:
                win.blit(self.walkLeft[0], self.rect)
            else:
                win.blit(self.char, self.rect)
                      
        # Draw blood level bar for character
        pygame.draw.rect(win, (0,128,0), (self.rect.x + 7, self.rect.y - 13, int(self.blood/2), 10))
        #Draw the name on top of the character
        font = pygame.font.Font("font.ttf",15)
        ID_on_top = font.render( self.ID , True,(255,255,255))
        win.blit(ID_on_top, (self.rect.x + 7, self.rect.y - 30, int(self.blood/2), 10))


    def addWeaponPoint(self, fromMonster):
        self.weaponPoint += fromMonster.experiencePoint

    def drawInfo_level1(self, screen, ID, blood):
        #info without exp
        font = pygame.font.Font("font.ttf",15)
        text_image_1 = font.render(("ID: " + ID), True,(0,0,0))
        text_image_2 = font.render(("Blood Level: " + str(blood)), True,(0,0,0))

        text_rect_1 = text_image_1.get_rect()
        text_rect_2 = text_image_2.get_rect()

        text_rect_1.x = 15
        text_rect_1.y = 65

        text_rect_2.x = 15
        text_rect_2.y = 100

        screen.blit(text_image_1,text_rect_1)
        screen.blit(text_image_2,text_rect_2)


    def drawInfo_level2(self, screen, ID, blood, experiencePoint):
        #info with exp
        font = pygame.font.Font("font.ttf",15)
        text_image_1 = font.render(("ID: " + ID), True,(0,0,0))
        text_image_2 = font.render(("Blood Level: " + str(blood)), True,(0,0,0))
        text_image_3 = font.render(("Experience: " + str(experiencePoint)), True,(0,0,0))

        text_rect_1 = text_image_1.get_rect()
        text_rect_2 = text_image_2.get_rect()
        text_rect_3 = text_image_3.get_rect()

        text_rect_1.x = 15
        text_rect_1.y = 50

        text_rect_2.x = 15
        text_rect_2.y = 80

        text_rect_3.x = 15
        text_rect_3.y = 110

        screen.blit(text_image_1,text_rect_1)
        screen.blit(text_image_2,text_rect_2)
        screen.blit(text_image_3,text_rect_3)

class Monster(GameObject):
    def __init__(self,position_x_coor, end,
                 attackPoint, experiencePoint):
        right_1 = pygame.image.load('EnemyMovingRight/R1E.png')
        super().__init__(right_1)
        
        self.rect.x = position_x_coor
        self.rect.y = 600
        self.vel = 4
        self.walkCount = 0
        self.path = [position_x_coor, end]
        self.initialPos = position_x_coor
        self.attackPoint = attackPoint
        self.experiencePoint = experiencePoint

        self.walkRight = [
        pygame.image.load('EnemyMovingRight/R1E.png'), 
        pygame.image.load('EnemyMovingRight/R2E.png'), 
        pygame.image.load('EnemyMovingRight/R3E.png'), 
        pygame.image.load('EnemyMovingRight/R4E.png'), 
        pygame.image.load('EnemyMovingRight/R5E.png'), 
        pygame.image.load('EnemyMovingRight/R6E.png'), 
        pygame.image.load('EnemyMovingRight/R7E.png'), 
        pygame.image.load('EnemyMovingRight/R8E.png'), 
        pygame.image.load('EnemyMovingRight/R9E.png'),
        pygame.image.load('EnemyMovingRight/R10E.png'), 
        pygame.image.load('EnemyMovingRight/R11E.png')]

        self.walkLeft = [
        pygame.image.load('EnemyMovingLeft/L1E.png'), 
        pygame.image.load('EnemyMovingLeft/L2E.png'), 
        pygame.image.load('EnemyMovingLeft/L3E.png'), 
        pygame.image.load('EnemyMovingLeft/L4E.png'), 
        pygame.image.load('EnemyMovingLeft/L5E.png'), 
        pygame.image.load('EnemyMovingLeft/L6E.png'), 
        pygame.image.load('EnemyMovingLeft/L7E.png'), 
        pygame.image.load('EnemyMovingLeft/L8E.png'), 
        pygame.image.load('EnemyMovingLeft/L9E.png'), 
        pygame.image.load('EnemyMovingLeft/L10E.png'), 
        pygame.image.load('EnemyMovingLeft/L11E.png')]



    def drawing(self, win):
        self.move()
        #set walk count equal to zero if it reaches pass the given threshold 
        if self.walkCount + 1 >= 33: 
            self.walkCount = 0
            
        if self.vel > 0: # moving to the right we will display our walkRight images
            win.blit(self.walkRight[self.walkCount//3], self.rect)
            self.walkCount += 1
        else:  # if not we will display the walkLeft images
            win.blit(self.walkLeft[self.walkCount//3], self.rect)
            self.walkCount += 1

        # Draw blood level bar for common monster
        pygame.draw.rect(win, (210,0,0), (self.rect.x + 10, self.rect.y - 10, int(self.blood / 2), 10))

    def move(self):
        # If we are moving right
        if self.vel > 0:
            # If we have not reached the furthest right point on our path
            if self.rect.x < self.path[1] + self.vel:
                self.rect.x += self.vel
            else:  # Change direction and move back the other way
                self.vel = self.vel * -1
                self.rect.x += self.vel
                self.walkCount = 0
        else:  # If we are moving left
            # If we have not reached the furthest left point on our path
            if self.rect.x > self.path[0] - self.vel:
                self.rect.x += self.vel
            else:  # Change direction and move back the other way
                self.vel = self.vel * -1
                self.rect.x += self.vel
                self.walkCount = 0


    def attact(self, character):
        super().attack(character)

class BigEnemy(GameObject):
    def __init__(self, position_x_coor, attackPoint, experiencePoint):

        self.walkRight = [
            pygame.image.load('EnemyMovingRight/R1E.png').convert_alpha(),
            pygame.image.load('EnemyMovingRight/R2E.png').convert_alpha(), 
            pygame.image.load('EnemyMovingRight/R3E.png').convert_alpha(), 
            pygame.image.load('EnemyMovingRight/R4E.png').convert_alpha(), 
            pygame.image.load('EnemyMovingRight/R5E.png').convert_alpha(), 
            pygame.image.load('EnemyMovingRight/R6E.png').convert_alpha(), 
            pygame.image.load('EnemyMovingRight/R7E.png').convert_alpha(), 
            pygame.image.load('EnemyMovingRight/R8E.png').convert_alpha(), 
            pygame.image.load('EnemyMovingRight/R9E.png').convert_alpha(),
            pygame.image.load('EnemyMovingRight/R10E.png').convert_alpha(), 
            pygame.image.load('EnemyMovingRight/R11E.png').convert_alpha()]

        self.walkLeft = [
            pygame.image.load('EnemyMovingLeft/L1E.png').convert_alpha(), 
            pygame.image.load('EnemyMovingLeft/L2E.png').convert_alpha(), 
            pygame.image.load('EnemyMovingLeft/L3E.png').convert_alpha(), 
            pygame.image.load('EnemyMovingLeft/L4E.png').convert_alpha(), 
            pygame.image.load('EnemyMovingLeft/L5E.png').convert_alpha(), 
            pygame.image.load('EnemyMovingLeft/L6E.png').convert_alpha(), 
            pygame.image.load('EnemyMovingLeft/L7E.png').convert_alpha(), 
            pygame.image.load('EnemyMovingLeft/L8E.png').convert_alpha(), 
            pygame.image.load('EnemyMovingLeft/L9E.png').convert_alpha(), 
            pygame.image.load('EnemyMovingLeft/L10E.png').convert_alpha(), 
            pygame.image.load('EnemyMovingLeft/L11E.png').convert_alpha()]

        for i in range (len(self.walkRight)):
            self.walkRight[i]= pygame.transform.scale(self.walkRight[i], (self.walkRight[i].get_width()*3, self.walkRight[i].get_height()*3))
        for i in range (len(self.walkLeft)):
            self.walkLeft[i]= pygame.transform.scale(self.walkLeft[i], (self.walkLeft[i].get_width()*3, self.walkLeft[i].get_height()*3))

         # Call the superclass constructor
        super().__init__(self.walkLeft[0])
        self.blood = 200
        self.rect.x =position_x_coor
        self.rect.y = 485
        self.vel=2.5
        self.attackPoint =attackPoint
        self.experiencePoint= experiencePoint
        self.walkCount= 0
        self.left= False
        self.right= False
        

    def move(self,character):
        #If the big monster is at right of character(monster rect.x > character rect.x)
        # monster moves left
        if self.rect.x > character.rect.x:
            self.left = True
            self.right = False
            self.rect.x -= self.vel
            if self.rect.colliderect(character.rect):
                self.rect.x += 0.5

        #If the big monster is at left of character(monster rect.x <= character rect.x)
        # monster moves right
        elif self.rect.x < character.rect.x:
            self.right = True
            self.left = False
            self.rect.x += self.vel
            if self.rect.colliderect(character.rect):
                self.rect.x -= 0.5

    def drawing(self, win,character):
        self.move(character)
        if self.walkCount >= 33:
            self.walkCount = 0

        if self.left :
            win.blit(self.walkLeft[self.walkCount // 3], self.rect)
            self.walkCount += 1
        elif self.right :
            win.blit(self.walkRight[self.walkCount // 3], self.rect)
            self.walkCount += 1
        # Draw blood level bar for big monster
        pygame.draw.rect(win, (210,0,0), (self.rect.x + 60, self.rect.y - 10, int(self.blood / 2), 10))


class Weapon(GameObject):
    def __init__(self,x, y,facing,attackPoint, shootingRange):
        rocket_image = pygame.image.load("WeaponImages/rockImg.png").convert_alpha()
        rocket_image = pygame.transform.scale(rocket_image,(rocket_image.get_width() / 20, rocket_image.get_height() / 20))

        bullet_image_R = pygame.image.load("WeaponImages/flameR.png").convert_alpha()
        bullet_image_L = pygame.image.load("WeaponImages/flameL.png").convert_alpha()
        bullet_image_R = pygame.transform.scale(bullet_image_R, (bullet_image_R.get_width() / 30 , bullet_image_R.get_height() / 30))
        bullet_image_L = pygame.transform.scale(bullet_image_L, (bullet_image_L.get_width() / 30 , bullet_image_L.get_height() / 30))
        fire_bullet = [bullet_image_R,bullet_image_L]
        
        laser_image_R = pygame.image.load("WeaponImages/laserR.png").convert_alpha()
        laser_image_L = pygame.image.load("WeaponImages/laserL.png").convert_alpha()
        laser_image_R = pygame.transform.scale(laser_image_R,(laser_image_R.get_width() / 5, laser_image_R.get_height() / 5))
        laser_image_L = pygame.transform.scale(laser_image_L,(laser_image_L.get_width() / 5, laser_image_L.get_height() / 5))
        laser_bullet = [laser_image_R,laser_image_L]

        super().__init__(bullet_image_R)

        self.bullet = ""
        self.bullets = [rocket_image,fire_bullet,laser_bullet]

        self.attackPoint = attackPoint
        self.shootingRange = shootingRange
        self.rect.x = x
        self.rect.y = y

        self.vel = 8 * facing

    def draw(self,win):
        win.blit(self.bullet,self.rect)
        self.rect.x += self.vel
    
    #the bullet attacks monster and only deduct blood once
    def attack(self, monster):
        super().attack(monster)

   


    