import pygame,random
import level2BackgroundElements
import GameObject
from endGame import win
from endGame import lose



pygame.init()

character_name = ""

def level2(): 
    clock = pygame.time.Clock()
    FPS = 60

    #background music
    pygame.mixer.music.load('sounds/level1_music.mp3')
    pygame.mixer.music.play(-1,0.0,5000)
    
    rock_sound = pygame.mixer.Sound('sounds/rock-shooting3.mp3')
    fire_sound = pygame.mixer.Sound('sounds/fire_shooting.mp3')
    laser_sound = pygame.mixer.Sound('sounds/laser_shooting.mp3')
    keyboard_sound = pygame.mixer.Sound('sounds/keyboard.mp3')
    win_sound = pygame.mixer.Sound('sounds/win_sound.mp3')
    endGame_sound = pygame.mixer.Sound('sounds/endGame_sound.mp3')




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
    furthest_group_x = SCREEN_WIDTH + 1200
    ground_count = furthest_group_x // ground_width

    #append ground_count number of ground image into group
    for i in range(ground_count):
        ground_xcoor = ground_width * i
        ground_ycoor = SCREEN_HEIGHT - ground_height
        ground_group.add(level2BackgroundElements.ground(ground_xcoor,ground_ycoor,ground_image))


    #character
    character = GameObject.Character(screen_rect,furthest_group_x,10,ground_ycoor - 100,character_name,50)

    #stage in the air
    stage_image = pygame.Surface((ground_image.get_width()*6 , ground_image.get_height()),pygame.SRCALPHA)
    for i in range(6):
        stage_image.blit(ground_image, (i * ground_image.get_width(),0))
        
    stage_group = pygame.sprite.Group()
    x_coor_stage1 = 500
    x_coor_stage2 = 1200
    x_coor_stage3 = 1600
    stage_group.add(level2BackgroundElements.ground(x_coor_stage1,350,stage_image))
    stage_group.add(level2BackgroundElements.ground(x_coor_stage2,350,stage_image))
    stage_group.add(level2BackgroundElements.ground(x_coor_stage3,160,stage_image))

        
    #background images
    bg_images = []
    for i in range(1, 6):
        bg_image = pygame.image.load(f"backgroundImage/background{i}.png").convert_alpha()
        bg_images.append(bg_image)

    # adjust background height to fit remaining screen space
    bg_height = SCREEN_HEIGHT - ground_height

    # adjust background width to fit entire screen
    for i in range(len(bg_images)):
        bg_images[i] = pygame.transform.scale(bg_images[i], (SCREEN_WIDTH, SCREEN_HEIGHT))

    bg_width = bg_images[0].get_width()

    #door img 
    door_image = pygame.image.load("backgroundImage/door2.png")
    door_width = door_image.get_width()
    door_height = door_image.get_height() 

    #door group
    door_group = pygame.sprite.Group()
    door_group.add(level2BackgroundElements.door(2020,598 - door_height,door_image))

    #bush images
    bush_image_0 = pygame.image.load("backgroundImage/Props_Bush_0.png").convert_alpha()
    bush_image_1 = pygame.image.load("backgroundImage/Props_Bush_1.png").convert_alpha()
    bush_image_2 = pygame.image.load("backgroundImage/Props_Bush_2.png").convert_alpha()

    bush_image = pygame.Surface((bush_image_0.get_width() + bush_image_1.get_width() + bush_image_2.get_width(),
                                    max(bush_image_0.get_height(), bush_image_1.get_height(), bush_image_2.get_height())),
                                    pygame.SRCALPHA)

    bush_image.blit(bush_image_0, (0, 0))
    bush_image.blit(bush_image_1, (bush_image_0.get_width(), 0))
    bush_image.blit(bush_image_2, (bush_image_0.get_width() + bush_image_1.get_width(), 0))

    ##scale bush
    bush_image = pygame.transform.scale(bush_image,(bush_image.get_width() * 2 ,bush_image.get_height() * 2 ))
    bush_image_width = bush_image.get_width()
    bush_image_height = bush_image.get_height()

    #bush group
    bush_group = pygame.sprite.Group()

    for i in range(random.randint(3,10)):
        bush_xcoor = random.uniform(bush_image_width, SCREEN_WIDTH * 2)
        bush_group.add(level2BackgroundElements.bush(bush_xcoor,SCREEN_HEIGHT - 2 * ground_height,bush_image))

    #Mushroom images
    original_mushroom_image = pygame.image.load("backgroundImage/mushroom.png")
    original_group_of_mushroom_image = pygame.image.load("backgroundImage/Props_Mushroom_1.png")

    new_mushroom_size1 = (original_mushroom_image.get_width() / 2, original_mushroom_image.get_height() // 2)
    mushroom_image = pygame.transform.scale(original_mushroom_image, (new_mushroom_size1))

    mushroom_image = pygame.image.load("backgroundImage/mushroom.png")
    mushroom_width = mushroom_image.get_width()
    mushroom_height = mushroom_image.get_height() 


    #mushroom group
    mushroom_group = pygame.sprite.Group()
    mushroom_group.add(level2BackgroundElements.mushroom(830,350 - mushroom_height,mushroom_image))
    mushroom_group.add(level2BackgroundElements.mushroom(840,350 - original_mushroom_image.get_height() ,original_mushroom_image))

    mushroom_group.add(level2BackgroundElements.mushroom(1050,593 - original_mushroom_image.get_height() ,original_mushroom_image))
    mushroom_group.add(level2BackgroundElements.mushroom(1075,593 - mushroom_height,mushroom_image))

    mushroom_group.add(level2BackgroundElements.mushroom(1225,350 - mushroom_height,mushroom_image))
    mushroom_group.add(level2BackgroundElements.mushroom(1200,350 - original_mushroom_image.get_height() ,original_mushroom_image))

    #group of mushrooms
    mushroom_group.add(level2BackgroundElements.mushroom(1540,350 - original_group_of_mushroom_image.get_height() ,original_group_of_mushroom_image))
    mushroom_group.add(level2BackgroundElements.mushroom(900,660 - original_group_of_mushroom_image.get_height() ,original_group_of_mushroom_image))

    #Tiles images
    tile_image_0 = pygame.image.load("backgroundImage/Tiles_0.png").convert_alpha()
    tile_image_1 = pygame.image.load("backgroundImage/Tiles_1.png").convert_alpha()
    tile_image_2 = pygame.image.load("backgroundImage/Tiles_2.png").convert_alpha()
    tile_image_3 = pygame.image.load("backgroundImage/Tiles_3.png").convert_alpha()
    tile_image_4 = pygame.image.load("backgroundImage/Tiles_4.png").convert_alpha()
    tile_image_5 = pygame.image.load("backgroundImage/Tiles_5.png").convert_alpha()
    tile_image_6 = pygame.image.load("backgroundImage/Tiles_6.png").convert_alpha()
    tile_image_width = tile_image_0.get_width()
    tile_image_height = tile_image_0.get_height()


    #glue them into a new object
    combined_image = pygame.Surface((tile_image_width * 30,tile_image_height * 2),pygame.SRCALPHA)

    # tile_xcoor = random.randint(0,SCREEN_WIDTH * 1.5)
    combined_image.blit(tile_image_0, (0, 0))
    combined_image.blit(tile_image_1, (0, tile_image_height))

    for i in range (29):
        combined_image.blit(tile_image_6, (tile_image_width * (i+1), 0))
        combined_image.blit(tile_image_2, (tile_image_width * (i+1), tile_image_height))

    combined_image.blit(tile_image_4, (tile_image_width * 30 , 0))
    combined_image.blit(tile_image_3, (tile_image_width * 30, tile_image_height))

    #scale the new object
    combined_image = pygame.transform.scale(combined_image,(combined_image.get_width() * 2, combined_image.get_height() * 2))
    combined_image_width = combined_image.get_width()
    combined_image_height = combined_image.get_height()

    #tile group
    tile_group = pygame.sprite.Group()
    tile_group.add(level2BackgroundElements.tile(960,SCREEN_HEIGHT - combined_image_height ,combined_image))

    #Monster
    monster_group = pygame.sprite.Group()
    enemy1 = GameObject.Monster(400,800,5,10)
    enemy2 = GameObject.Monster(350,500,5,10)
    enemy3 = GameObject.Monster(300,600,5,10)
    enemy4 = GameObject.Monster(350,700,5,10)
    enemy5 = GameObject.Monster(500,800,5,10)
    enemy6 = GameObject.Monster(550,900,5,10)
    monster_group.add(enemy1,enemy2,enemy2,enemy3,enemy4,enemy5,enemy6)

    #moving big monster
    big_monster_group = pygame.sprite.Group()
    big_monster = GameObject.BigEnemy(1200,20,30)
    big_monster.blood = 600
    big_monster_group.add(big_monster)

    #bullet
    bullet_group = pygame.sprite.Group()

    def render_level_2():
        for x in range(5):
            speed = 1
            for i in bg_images:
                screen.blit(i, ((x * bg_width) - scroll * speed, 0))
                speed += 0.2

        ground_group.update()
        ground_group.draw(screen)

        stage_group.update()
        stage_group.draw(screen)

        bush_group.update()
        bush_group.draw(screen)

        tile_group.update()
        tile_group.draw(screen)

        mushroom_group.update()
        mushroom_group.draw(screen)
        
        door_group.update()
        door_group.draw(screen)

        character.redrawGameWindow(screen)
        character.drawInfo_level2(screen,character.ID,character.blood,character.weaponPoint)

        for monster in monster_group:
            monster.drawing(screen)

        for big_monster in big_monster_group:
            big_monster.drawing(screen,character)

        for bullet in bullet_group:
            bullet.draw(screen)

        pygame.display.flip()


    # game loop
    run = True
    #flag to determine if it's the only bullet
    firing = False
    #flag to determine if it's the only jump
    jumping = False
    #flag to determine if it's the only weapon switch 
    switching = False
    bullet_index = 0
    #flag to mark the position when character shoots bullet
    characterShootingPos = 0
    

    while run:
        # event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #game logic
        clock.tick(FPS)
        character.rect.y += character.jumpCount * 2
        for monster in monster_group:
            monster.rect.y += 5
        for monster in big_monster_group:
            monster.rect.y += 5
        # get keypresses
        key = pygame.key.get_pressed()
        ##left for moving left
        if key[pygame.K_LEFT]:
            if scroll > 0:
                scroll -= 5
                for ground in ground_group:
                    ground.rect.x += 4 
                for bush in bush_group:
                    bush.rect.x += 4
                for tile in tile_group:
                    tile.rect.x += 4
                for stage in stage_group:
                    stage.rect.x += 4
                for mushroom in mushroom_group:
                    mushroom.rect.x += 4
                for door in door_group:
                    door.rect.x += 4


            if character.rect.x > character.speed:
                character.rect.x -= character.speed
                character.left = True
                character.right = False
                character.standing = False
        ##right for moving right
        elif key[pygame.K_RIGHT] :
            if scroll < 1200:
                scroll += 5
                for ground in ground_group:
                    ground.rect.x -= 4
                for bush in bush_group:
                    bush.rect.x -= 4
                for tile in tile_group:
                    tile.rect.x -= 4
                for stage in stage_group:
                    stage.rect.x -= 4
                for mushroom in mushroom_group:
                    mushroom.rect.x -=4
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
        if not(character.isJump):
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
                character.rect.y -= (int)((character.jumpCount ** 2)* 0.9 * neg)

                #character's head goes over the top of screen
                if character.rect.top <= 0:
                    character.rect.top = 5
                character.jumpCount -= 1
                
            else:
                character.isJump = False
                character.jumpCount = 10
        
        ##space for bullet
        ##only one bullet a time
        if  not firing and key[pygame.K_SPACE] :
            firing = True
            characterShootingPos = character.rect.x
            if character.left:
                facing = -1
                #fire bullet left, with 20 attack point
                if bullet_index == 1:
                    fire_sound.play()
                    bullet = GameObject.Weapon(round(character.rect.x - character.rect.width //2) + 8, round(character.rect.y + character.rect.height//2) - 30, facing ,20,400)                    
                    bullet.bullet = bullet.bullets[1][1]
                #rocket bullet, with 10 attack point
                elif bullet_index == 0:
                    rock_sound.play()
                    bullet = GameObject.Weapon(round(character.rect.x - character.rect.width //2), round(character.rect.y + character.rect.height//2) - 30, facing ,10,300)
                    bullet.bullet = bullet.bullets[0]
                #laser bullet with 30 attack point
                elif bullet_index == 2:
                    laser_sound.play()
                    bullet = GameObject.Weapon(round(character.rect.x - character.rect.width //2), round(character.rect.y + character.rect.height//2) - 40, facing ,30,500)
                    bullet.bullet = bullet.bullets[2][1]
            else:
                facing = 1
                #fire bullet right
                if bullet_index == 1:
                    fire_sound.play()
                    
                    bullet = GameObject.Weapon(round(character.rect.x + character.rect.width //2), round(character.rect.y + character.rect.height//2) - 30, facing ,20,400)
                    bullet.bullet = bullet.bullets[1][0]
                #rocket bullet
                elif bullet_index == 0:
                    rock_sound.play()
                    bullet = GameObject.Weapon(round(character.rect.x + character.rect.width //2), round(character.rect.y + character.rect.height//2) - 30, facing ,10,300)
                    bullet.bullet = bullet.bullets[0] 
                #laser bullet 
                elif bullet_index == 2:
                    laser_sound.play()
                    bullet = GameObject.Weapon(round(character.rect.x + character.rect.width //2), round(character.rect.y + character.rect.height//2) - 43, facing ,30,500)
                    bullet.bullet = bullet.bullets[2][0]
            bullet_group.add(bullet)

        elif not key[pygame.K_SPACE]:
            firing = False

        #if bullet in bullet_group flys out of range
        for bullet in bullet_group:
            if bullet.rect.x >= characterShootingPos + bullet.shootingRange or bullet.rect.x <= characterShootingPos - bullet.shootingRange:
                    bullet_group.remove(bullet)

        # R for switching bullet
        if not switching and key[pygame.K_r]:
            keyboard_sound.play()
            max_index = 1
            switching = True
            keyboard_sound.play()
            bullet_index += 1
            if character.weaponPoint > 50:
                max_index = 2
            if bullet_index > max_index:
                bullet_index = 0
        elif not key[pygame.K_r]:
            switching = False

        # collisions between bushes
        for bush_sprite in bush_group:
            bush_collisions = pygame.sprite.spritecollide(bush_sprite, bush_group, False)
            for other_bush_sprite in bush_collisions:
                if bush_sprite != other_bush_sprite and bush_sprite.rect.colliderect(other_bush_sprite.rect):
                    bush_sprite.rect.right = other_bush_sprite.rect.left

        # collisions between tiles
        for tile_sprite in tile_group:
            tile_collisions = pygame.sprite.spritecollide(tile_sprite, tile_group, False)
            for other_tile_sprite in tile_collisions:
                if tile_sprite != other_tile_sprite and tile_sprite.rect.colliderect(other_tile_sprite.rect):
                    tile_sprite.rect.left = other_tile_sprite.rect.right

        # collisions between bush and tile
        pygame.sprite.groupcollide(bush_group, tile_group, False, False)

        #collisions between tile and ground
        pygame.sprite.groupcollide(tile_group, ground_group,False, True)

        #collisions between character and ground
        collisions_character_and_ground = pygame.sprite.spritecollide(character,ground_group,False)
        for ground in collisions_character_and_ground:
            character.rect.bottom = ground.rect.top

        #collision between monster and ground
        collisions_monster_and_ground = pygame.sprite.groupcollide(monster_group,ground_group,False,False)
        for monster in collisions_monster_and_ground:
            for ground in collisions_monster_and_ground[monster]:
                monster.rect.bottom = ground.rect.top+10

        #collision between big monster and ground
        collisions_big_monster_and_ground = pygame.sprite.groupcollide(big_monster_group,ground_group,False,False)
        for monster in collisions_big_monster_and_ground:
            for ground in collisions_big_monster_and_ground[monster]:
                monster.rect.bottom = ground.rect.top+20

        #collisions between character and tiles
        collisions_character_and_tile = pygame.sprite.spritecollide(character,tile_group,False)
        if collisions_character_and_tile:
            for tile in collisions_character_and_tile:
                character.rect.bottom = tile.rect.top

        #collision between monsters and tiles
        collisions_monster_and_tile = pygame.sprite.groupcollide(monster_group,tile_group,False,False)
        for monster in collisions_monster_and_tile:
            for tile in collisions_monster_and_tile[monster]:
                monster.rect.bottom = tile.rect.top+10
                
        #collision between big monsters and tiles
        collisions_big_monster_and_tile = pygame.sprite.groupcollide(big_monster_group,tile_group,False,False)
        for monster in collisions_big_monster_and_tile:
            for tile in collisions_big_monster_and_tile[monster]:
                monster.rect.bottom = tile.rect.top+20

        #collision between character and stages
        collisions_character_and_stages = pygame.sprite.spritecollide(character,stage_group,False)
        if collisions_character_and_stages:
            for stage in collisions_character_and_stages:
                #collission only happen when center of the character over the stage
                if character.rect.y <= stage.rect.top :
                    character.rect.bottom = stage.rect.top

        #collision between monster and stages
        collisions_monster_and_stages = pygame.sprite.groupcollide(monster_group,stage_group,False,False)
        for monster in collisions_monster_and_stages:
            for stage in collisions_monster_and_stages[monster]:
                monster.rect.bottom = stage.rect.top + 5

        #collision between bullets and monsters
        collisions_monsters_and_bullets = pygame.sprite.groupcollide(monster_group,bullet_group,False,True)
        for monster in collisions_monsters_and_bullets:   
            for bullet in collisions_monsters_and_bullets[monster]:
                bullet.attack(monster)
                if monster.blood <= 0:   
                    character.addWeaponPoint(monster)
                    monster_group.remove(monster)
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

        # collision between monster and character(monster attacks chatacter)
        collisions_monsters_and_character = pygame.sprite.spritecollide(character,monster_group,False)
        if collisions_monsters_and_character:
            for monster in collisions_monsters_and_character:
                monster.attack(character)
                if character.blood <= 0: 
                 pygame.mixer.music.stop()
                 endGame_sound.play()
                 lose()
        else:
            for monster in monster_group:
                monster.ifAttacked = False

        #collision between big monster and character
        for big_monster in big_monster_group:
            big_monster.attack(character) 
            if character.blood <= 0: 
                pygame.mixer.music.stop()
                endGame_sound.play()
                lose()
        
        #collisions between character and gate
        collisions_character_and_gate = pygame.sprite.spritecollide(character, door_group, False)
        for door in collisions_character_and_gate: 
            if character.rect.center >= door.rect.center:
                if not monster_group:
                    pygame.mixer.music.stop() 
                    win_sound.play()
                    win()
    
        # draw world
        render_level_2()
        # background.render()

        pygame.display.update()
    pygame.quit()
