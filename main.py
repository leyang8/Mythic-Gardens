import pygame, sys 
from button import Button
from characterID import characterId
pygame.init()


SCREEN = pygame.display.set_mode((1280, 705))
pygame.display.set_caption("Menu")

#background music
pygame.mixer.music.load('sounds/mainMenu_music.mp3')
pygame.mixer.music.play(-1,0.0,5000)

click_sound = pygame.mixer.Sound('sounds/buttonClick.mp3')

BG = pygame.image.load("WindowsPage/forest_menu.png")
BG = pygame.transform.scale(BG, (1280, 705))

def get_font(size): # Returns Press-Start-2P in the desired size
     return pygame.font.Font("font.ttf", size) 

def play():
    characterId()

def rules():
    # Load and resize the background image
    bg_image = pygame.image.load("WindowsPage/rules.png")
    bg_image = pygame.transform.scale(bg_image, (1280, 705))

    while True:
        RULES_MOUSE_POS = pygame.mouse.get_pos()

        # Blit the background image onto the screen
        SCREEN.blit(bg_image, (0, 0))

        RULES_BACK = Button(image=None, pos=(1130, 600), 
                            text_input="BACK", font=get_font(35), base_color="Black", hovering_color="White")

        RULES_BACK.changeColor(RULES_MOUSE_POS)
        RULES_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                click_sound.play()                
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



