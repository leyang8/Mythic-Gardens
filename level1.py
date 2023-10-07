import pygame,random
import level2BackgroundElements
import GameObject
from endGame import lose
import level2_transition

pygame.init()

character_name = ""
    

def level1 (): 
    clock = pygame.time.Clock()
    FPS = 60

    #background music
    pygame.mixer.music.load('sounds/level1_music.mp3')
    pygame.mixer.music.play(-1,0.0,5000)

    rock_sound = pygame.mixer.Sound('sounds/rock-shooting3.mp3')
    endGame_sound = pygame.mixer.Sound('sounds/endGame_sound.mp3')
    gate_sound = pygame.mixer.Sound('sounds/gate-sound5.mp3')

    # create game window
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen_rect = screen.get_rect()


    # define game variables
    scroll = 0


    #ground image
    ground_image = pygame.image.load("backgroundImage/groundBlock.png").convert_alpha()
    # adjust to appropriate ground size 
    ground_image = pygame.transform.scale(ground_image, (ground_image.get_width() * 2, ground_image.get_height() * 2))
    ground_width = ground_image.get_width()
    ground_height = ground_image.get_height() 

    #group group
    ground_group = pygame.sprite.Group()
    furthest_group_x = SCREEN_WIDTH + 200
    ground_count = furthest_group_x // ground_width

    #append ground_count number of ground image into group
    for i in range(ground_count):
        ground_xcoor = ground_width * i
        ground_ycoor = SCREEN_HEIGHT - ground_height
        ground_group.add(level2BackgroundElements.ground(ground_xcoor,ground_ycoor,ground_image))


    #mushroom image 
    mushroom_image = pygame.image.load("backgroundImage/mushroom.png")
    mushroom_width = mushroom_image.get_width()
    mushroom_height = mushroom_image.get_height() 
    small_mushroom = pygame.transform.scale(mushroom_image, (mushroom_image.get_width() /2, mushroom_image.get_height() /2))

    #mushroom group
    mushroom_group = pygame.sprite.Group()
    mushroom_group.add(level2BackgroundElements.mushroom(500,SCREEN_HEIGHT-ground_height-mushroom_height ,mushroom_image))
    mushroom_group.add(level2BackgroundElements.mushroom(1200,SCREEN_HEIGHT-ground_height-mushroom_height ,mushroom_image))
    mushroom_group.add(level2BackgroundElements.mushroom(1185,640 ,small_mushroom))

    #grass1 image
    grass1_image = pygame.image.load("backgroundImage/grass1.png").convert_alpha()
    grass1_image = pygame.transform.scale(grass1_image, (grass1_image.get_width() * 4, grass1_image.get_height() * 4))
    grass1_width = grass1_image.get_width() 
    grass1_height = grass1_image.get_height() 

    #grass1 group
    grass1_group = pygame.sprite.Group()
    grass1_group.add(level2BackgroundElements.grass1(200,SCREEN_HEIGHT-ground_height-grass1_height ,grass1_image))
    grass1_group.add(level2BackgroundElements.grass1(1000,SCREEN_HEIGHT-ground_height-grass1_height ,grass1_image))

    #grass2 image
    grass2_image = pygame.image.load("backgroundImage/grass2.png").convert_alpha()
    grass2_image = pygame.transform.scale(grass2_image, (grass2_image.get_width() * 4, grass2_image.get_height() * 4))
    grass2_width = grass2_image.get_width() * 4
    grass2_height = grass2_image.get_height() * 4

    #grass2 group
    grass2_group = pygame.sprite.Group()
    grass2_group.add(level2BackgroundElements.grass2(155,528,grass2_image))
    grass2_group.add(level2BackgroundElements.grass2(1300,528 ,grass2_image))

    #character
    character = GameObject.Character(screen_rect,furthest_group_x,10,ground_ycoor, character_name ,0)
    level2_transition.character_name = character_name

    #Monster
    enemy_group = pygame.sprite.Group()
    enemy1 = GameObject.Monster(800,1000,5,10)
    enemy2 = GameObject.Monster(600,950,5,10)
    enemy3 = GameObject.Monster(400,600,5,10)
    enemy4 = GameObject.Monster(350,700,5,10)
    enemy5 = GameObject.Monster(500,800,5,10)
    enemy6 = GameObject.Monster(550,900,5,10)
    enemy_group.add(enemy1,enemy2,enemy2,enemy3,enemy4,enemy5,enemy6)
    
    #moving big monster
    big_monster_group = pygame.sprite.Group()
    big_monster = GameObject.BigEnemy(700,20,20)
    big_monster_group.add(big_monster)


    #door img 
    door_image = pygame.image.load("backgroundImage/door3.png")
    door_width = door_image.get_width()
    door_height = door_image.get_height() 
    #door group
    door_group = pygame.sprite.Group()
    door_group.add(level2BackgroundElements.door(1250,690 - door_height,door_image))
    
    #bullet
    bullet_group = pygame.sprite.Group()

    #background images
    bg_images = []
    for i in range(1, 6):
        bg_image = pygame.image.load(f"backgroundImage/background{i}.png").convert_alpha()
        bg_images.append(bg_image)

    # adjust background height to fit remaining screen space
    bg_height = SCREEN_HEIGHT - ground_height

    # adjust background width to fit entire screen
    for i in range(len(bg_images)):
        bg_images[i] = pygame.transform.scale(bg_images[i], (SCREEN_WIDTH, bg_height))

    bg_width = bg_images[0].get_width()

    def render():
        for x in range(5):
            speed = 1
            for i in bg_images:
                screen.blit(i, ((x * bg_width) - scroll * speed, 0))
                speed += 0.2

        ground_group.update()
        ground_group.draw(screen)

        character.redrawGameWindow(screen)
        character.drawInfo_level1(screen,character.ID,character.blood)

        mushroom_group.update()
        mushroom_group.draw(screen)

        grass1_group.update()
        grass1_group.draw(screen)

        grass2_group.update()
        grass2_group.draw(screen)
        
        door_group.update()
        door_group.draw(screen)


        for enemy in enemy_group:
            enemy.drawing(screen)

        for bullet in bullet_group:
            bullet.draw(screen)

        for big_monster in big_monster_group:
            big_monster.drawing(screen,character)

        pygame.display.update()


    # game loop
    run = True
    #flag to determine if it's the only bullet
    firing = False
    #flag to determine if it's the only jump
    jumping = False
    #flag to mark the position when character shoots bullet
    characterShootingPos = 0

    while run:
        clock.tick(FPS)

        for monster in enemy_group:
            monster.rect.y += 0
        # draw world
        render()

        # get keypresses
        key = pygame.key.get_pressed()

        # event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        ##left for moving left
        if key[pygame.K_LEFT]:
            if scroll > 0:
                scroll -= 5
                for ground in ground_group:
                    ground.rect.x += 4 
                for mushroom in mushroom_group:
                    mushroom.rect.x += 4
                for grass1 in grass1_group:
                    grass1.rect.x += 4
                for grass2 in grass2_group:
                    grass2.rect.x += 4
                for door in door_group:
                    door.rect.x += 4

            if character.rect.x > character.speed:
                character.rect.x -= character.speed
                character.left = True
                character.right = False
                character.standing = False
        ##right for moving right
        elif key[pygame.K_RIGHT] :
            if scroll < 200:
                scroll += 5
                for ground in ground_group:
                    ground.rect.x -= 4
                for mushroom in mushroom_group:
                    mushroom.rect.x -=4
                for grass1 in grass1_group:
                    grass1.rect.x -=4
                for grass2 in grass2_group:
                    grass2.rect.x -=4
                for door in door_group:
                    door.rect.x -=4

            if character.rect.x < character.range_right:
                character.rect.x += character.speed
                character.left = False
                character.right = True
                character.standing = False
        else:
            character.standing = True
            character.walkCount = 0
        ## up for jump
        if not(character.isJump) :
            if key[pygame.K_UP] and not jumping:
                jumping = True
                character.isJump = True
                character.right = False
                character.left = False
                character.walkCount = 0
            elif not key[pygame.K_UP]:
                jumping = False 
        else:
            if character.jumpCount >= -10:
                neg = 1
                if character.jumpCount < 0:
                    neg = -1
                character.rect.y -= (int)((character.jumpCount ** 2) * 0.5 * neg)
                character.jumpCount -= 1
            else:
                character.isJump = False
                character.jumpCount = 10

        ##space for bullet
        ##only one bullet a time
        if  not firing and key[pygame.K_SPACE] :
            rock_sound.play()
            
            firing = True
            characterShootingPos = character.rect.x
            if character.left:
                facing = -1
                #rocket bullet, with 10 attack point
                bullet = GameObject.Weapon(round(character.rect.x - character.rect.width //2), round(character.rect.y + character.rect.height//2) - 10, facing ,10,300)
                bullet.bullet = bullet.bullets[0]
            else:
                facing = 1
                #rocket bullet
                bullet = GameObject.Weapon(round(character.rect.x + character.rect.width //2), round(character.rect.y + character.rect.height//2) - 10, facing ,10,300)
                bullet.bullet = bullet.bullets[0] 
            bullet_group.add(bullet)

        elif not key[pygame.K_SPACE]:
            firing = False

        #if bullet in bullet_group flys out of range
        for bullet in bullet_group:
            if bullet.rect.x >= characterShootingPos + bullet.shootingRange or bullet.rect.x <= characterShootingPos - bullet.shootingRange:
                    bullet_group.remove(bullet)

        #collisions between character and ground
        collisions_character_and_ground = pygame.sprite.spritecollide(character,ground_group,False)
        for ground in collisions_character_and_ground:
            character.rect.bottom = ground.rect.top
       
        #collisions between character and gate
        collisions_character_and_gate = pygame.sprite.spritecollide(character, door_group, False)
        for door in collisions_character_and_gate: 
            if character.rect.center >= door.rect.center:
                if not enemy_group:
                    pygame.mixer.music.stop() 
                    gate_sound.play()
                    level2_transition.transitionToLevel2()
                
        #collision between bullets and monsters
        collisions_monsters_and_bullets = pygame.sprite.groupcollide(enemy_group,bullet_group,False,False)
        for monster in collisions_monsters_and_bullets:   
            for bullet in collisions_monsters_and_bullets[monster]:
                if bullet.rect.top >= monster.rect.top and bullet.rect.bottom <= monster.rect.bottom:
                    bullet.attack(monster)
                    bullet_group.remove(bullet)
                    if monster.blood <= 0:   
                        enemy_group.remove(monster)
                        bullet_group.remove(bullet)

        #collision between bullets and big monster
        collisions_big_monsters_and_bullets = pygame.sprite.groupcollide(big_monster_group,bullet_group,False,False)
        for monster in collisions_big_monsters_and_bullets:   
            for bullet in collisions_big_monsters_and_bullets[monster]:
                if bullet.rect.top >= monster.rect.top and bullet.rect.bottom <= monster.rect.bottom:
                    bullet.attack(monster)
                    bullet_group.remove(bullet)
                    if monster.blood <= 0:   
                        big_monster_group.remove(monster)
                        bullet_group.remove(bullet)

        #collision between monster and character(monster attacks chatacter)
        collisions_monsters_and_character = pygame.sprite.spritecollide(character,enemy_group,False)
        if collisions_monsters_and_character:
            for monster in collisions_monsters_and_character:
                monster.attack(character)    
                if character.blood <= 0:
                    pygame.mixer.music.stop() 
                    endGame_sound.play()
                    lose()  
        else:
            for monster in enemy_group:
                monster.ifAttacked = False
        
        #collision between big monster and character
        if big_monster_group:
            big_monster.attack(character) 
            if character.blood <= 0: 
                pygame.mixer.music.stop()
                endGame_sound.play()
                lose()  

        pygame.display.flip()
    pygame.quit()

