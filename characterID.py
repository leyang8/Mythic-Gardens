import pygame, sys
from button import Button
import level1

pygame.init()



def characterId():

    SCREEN = pygame.display.set_mode((1280, 705))
    pygame.display.set_caption("Character Name")

    BG = pygame.image.load("WindowsPage/ID.png")
    BG = pygame.transform.scale(BG, (1280, 705))

    click_sound = pygame.mixer.Sound('sounds/buttonClick.mp3')
    keyboard_sound = pygame.mixer.Sound('sounds/keyboard.mp3')

    character = pygame.image.load("CharacterStanding/standing.png")
    character = pygame.transform.scale(character, (character.get_width() * 7, character.get_height() * 7))

    def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("font.ttf", size)

    def try_again():
        print("TRY AGAIN")

    def main_menu():
        # Set up the font
        font = get_font(32)

        # Display the text prompt
        text = font.render("Enter your character name:", True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2 - 100))
        SCREEN.blit(text, text_rect)

        # Create the text input box
        input_box = pygame.Rect(460, 535, 350, 50)
        color_inactive = pygame.Color('black')
        color_active = pygame.Color('grey')
        color = color_inactive
        active = False
        text = ''

        # Create the "Submit" button
        button = Button(image=None, pos=(910, 550),
                        text_input="Save", font=get_font(18), base_color="Black", hovering_color="White")

        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    click_sound.play()
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click_sound.play()
                    # Check if the "Submit" button was clicked
                    if button.checkForInput(pygame.mouse.get_pos()) and text != '':
                        level1.character_name = text
                        level1.level1()
                        running = False
                    # Toggle the active variable for the input box
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    # Change the color of the input box
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    keyboard_sound.play()
                    # Handle key presses
                    if active:
                        if event.key == pygame.K_RETURN:
                            if text != '':
                                running = False
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            # Limit the number of characters in the text box to 10
                            if len(text) < 10:
                                text += event.unicode
            
                          
            # Draw the background
            SCREEN.blit(BG, (0, 0))

            # Draw the input box and text
            pygame.draw.rect(SCREEN, color, input_box, 2)
            text_surface = font.render(text, True, (255, 255, 255))
            SCREEN.blit(text_surface, (input_box.x + 5, input_box.y + 5))

            # Draw the "Submit" button
            button.changeColor(pygame.mouse.get_pos())
            button.update(SCREEN)

            #draw the character
            SCREEN.blit(character,(430,80))


            # Update the display
            pygame.display.flip()

        # Print the player's name
        print("Player name:", text)

        # Quit Pygame
        pygame.quit()
        sys.exit()
        


    main_menu()
    

 
