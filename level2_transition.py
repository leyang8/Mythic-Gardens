import pygame, sys
import time
import level2
pygame.init()

character_name = ""

def transitionToLevel2(): 
    SCREEN = pygame.display.set_mode((1280, 705))
    pygame.display.set_caption("Menu")

    BG = pygame.image.load("WindowsPage/level2Transition.png")
    BG = pygame.transform.scale(BG, (1280, 705))


    def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("font.ttf", size)
    def main_menu():
        start_time = time.time()
        while time.time() - start_time < 3:  # exit after 3 seconds
            SCREEN.blit(BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            TEXT = get_font(18).render("NEW WEAPONS UNLOCKED", True, "#DA531F")
            TEXT_RECT = TEXT.get_rect(center=(640, 370))

            SCREEN.blit(TEXT, TEXT_RECT)

            TEXT = get_font(15).render("PRESS 'R' TO CHANGE WEAPONS", True, "#2E1B58")
            TEXT_RECT = TEXT.get_rect(center=(640, 395))

            SCREEN.blit(TEXT, TEXT_RECT)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()

        level2.character_name = character_name
        level2.level2()
        pygame.quit()
        sys.exit()

    main_menu()


    # def main_menu():
    #     while True:
    #         SCREEN.blit(BG, (0, 0))

    #         MENU_MOUSE_POS = pygame.mouse.get_pos()

    #         TEXT = get_font(18).render("NEW WEAPONS UNLOCKED", True, "#DA531F")
    #         TEXT_RECT = TEXT.get_rect(center=(640, 370))

    #         SCREEN.blit(TEXT, TEXT_RECT)

    #         TEXT = get_font(15).render("PRESS 'R' TO CHANGE WEAPONS", True, "#2E1B58")
    #         TEXT_RECT = TEXT.get_rect(center=(640, 395))

    #         SCREEN.blit(TEXT, TEXT_RECT)
            
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 pygame.quit()
    #                 sys.exit()
    #         time.sleep(2000)
    #         level2()    
    #         pygame.display.update()
            

    # main_menu() 
    
        
