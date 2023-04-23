import pygame
import sys
pygame.init()


def guide_english_call():
    screen_width = 1000
    screen_height = 1000
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('English Guide')
    help_page_img = pygame.image.load('menuAssets/Guide_English.png')
    screen.blit(help_page_img, (0, 0))
    pygame.display.update()
    # Wait for the user to go back to the main menu
    back_flag = False
    while not back_flag:
        # Draw the back button
        back = pygame.image.load('menuAssets/start1.png')
        back_button_rect = pygame.Rect(20, 20, back.get_width(), back.get_height())
        screen.blit(back, back_button_rect)
        # back_button_rect = pygame.Rect(20, 20, 100, 50)
        # pygame.draw.rect(screen, (255, 255, 255), back_button_rect)
        # back_button_font = pygame.font.Font(None, 30)
        # back_button_text = back_button_font.render('Back', True, (0, 0, 0))
        # screen.blit(back_button_text, (30, 30))
        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse clicked on the back button
                if back_button_rect.collidepoint(event.pos):
                    back_flag = True  # Go back to the main menu
                    break
        pygame.display.update()