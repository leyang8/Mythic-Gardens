import pygame, sys
from button import Button
import level1
# from main import play

pygame.init()

def main_page():
    SCREEN = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Menu")
    
    pygame.mixer.music.load('sounds/mainMenu_music.mp3')
    pygame.mixer.music.play(-1,0.0,5000)
    
    click_sound = pygame.mixer.Sound('sounds/buttonClick.mp3')



    BG = pygame.image.load("WindowsPage/forest_menu.png")
    BG = pygame.transform.scale(BG, (1280, 720))

    def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("font.ttf", size)

    def play():
        level1.level1()
        
    def rules():
        while True:
            RULES_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.fill("#859970")


            RULES_TEXT = get_font(45).render("1. Follow all posted rules.", True, "Black")
            RULES_RECT = RULES_TEXT.get_rect(center=(640, 260))
            SCREEN.blit(RULES_TEXT, RULES_RECT)

            RULES_BACK = Button(image=None, pos=(1040, 640), 
                                text_input="BACK", font=get_font(60), base_color="Black", hovering_color="White")

            RULES_BACK.changeColor(RULES_MOUSE_POS)
            RULES_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if RULES_BACK.checkForInput(RULES_MOUSE_POS):
                        click_sound.play()     
                                   
                        main_menu()

            pygame.display.update()

    def main_menu():
        while True:
            SCREEN.blit(BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()
    # #8B3909
            MENU_TEXT = get_font(100).render("MAIN MENU", True, "#7D3A12")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 110))

            PLAY_BUTTON = Button(image=pygame.image.load("WindowsPage/Play Rect.png"), pos=(640, 250), 
                                text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            RULES_BUTTON = Button(image=pygame.image.load("WindowsPage/Options Rect.png"), pos=(640, 400), 
                                text_input="RULES", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("WindowsPage/Quit Rect.png"), pos=(640, 550), 
                                text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

            SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, RULES_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(SCREEN)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    click_sound.play() 
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        click_sound.play()                
                        
                        play()
                    if RULES_BUTTON.checkForInput(MENU_MOUSE_POS):
                        click_sound.play()
                        rules()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        click_sound.play()
                        pygame.quit()
                        sys.exit()

            pygame.display.update()
    main_menu()


def lose():
    SCREEN = pygame.display.set_mode((1280, 705))
    pygame.display.set_caption("Game Over")

    BG = pygame.image.load("WindowsPage/TryAgain.png")
    BG = pygame.transform.scale(BG, (1280, 705))

    click_sound = pygame.mixer.Sound('sounds/buttonClick.mp3')

    def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("font.ttf", size)

    def try_again():
        main_page()

    def main_menu():
        while True:
            SCREEN.blit(BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(60).render("GAME OVER!", True, "White")
            MENU_RECT = MENU_TEXT.get_rect(center=(620, 250))

            TRY_AGAIN_BUTTON = Button(image=None, pos=(600, 420), 
                                text_input="TRY AGAIN", font=get_font(40), base_color="Black", hovering_color="White")

            TRY_AGAIN_BUTTON.changeColor(MENU_MOUSE_POS)
            TRY_AGAIN_BUTTON.update(SCREEN)

            SCREEN.blit(MENU_TEXT, MENU_RECT)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    click_sound.play() 
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if TRY_AGAIN_BUTTON.checkForInput(MENU_MOUSE_POS):
                        click_sound.play()                         
                        try_again()

            pygame.display.update()

    main_menu() 



def win():
    SCREEN = pygame.display.set_mode((1280, 705))
    pygame.display.set_caption("Game Over")

    BG = pygame.image.load("WindowsPage/end.png")
    BG = pygame.transform.scale(BG, (1280, 705))

    click_sound = pygame.mixer.Sound('sounds/buttonClick.mp3')


    def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("font.ttf", size)

    def try_again():
        main_page()
        
    def quit():
        pygame.quit()
        sys.exit()

    
    def main_menu():
        while True:
            SCREEN.blit(BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(70).render("THE END!", True, "White")
            MENU_RECT = MENU_TEXT.get_rect(center=(620, 270))

            TRY_AGAIN_BUTTON = Button(image=None, pos=(640, 410), 
                                text_input="Restart", font=get_font(40), base_color="Black", hovering_color="White")

            TRY_AGAIN_BUTTON.changeColor(MENU_MOUSE_POS)
            TRY_AGAIN_BUTTON.update(SCREEN)
            
            QUIT_BUTTON = Button(image=None, pos=(640, 460), 
                                text_input="QUIT", font=get_font(40), base_color="Black", hovering_color="White")

            QUIT_BUTTON.changeColor(MENU_MOUSE_POS)
            QUIT_BUTTON.update(SCREEN)


            SCREEN.blit(MENU_TEXT, MENU_RECT)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    click_sound.play() 
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if TRY_AGAIN_BUTTON.checkForInput(MENU_MOUSE_POS):
                        click_sound.play() 
                        try_again()
                    elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        quit()


            pygame.display.update()

    main_menu() 
