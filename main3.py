import pygame 
import sys

pygame.init()

# Set up the screen
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

# Load images
bg_img = pygame.image.load('oi.png')
start_button_img = pygame.image.load('start1.png')
help_button_img = pygame.image.load('help1.png')
# Create Rect objects for the buttons
start_button_rect = pygame.Rect(380, 430, start_button_img.get_width(), start_button_img.get_height())
help_button_rect = pygame.Rect(380, 550, help_button_img.get_width(), help_button_img.get_height())

# Main loop
while True:
    # Draw the background and buttons
    screen.blit(bg_img, (0, 0))
    screen.blit(start_button_img, start_button_rect)
    screen.blit(help_button_img, help_button_rect)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse clicked on a button
            if start_button_rect.collidepoint(event.pos):
                # Load the start page image
                start_page_img = pygame.image.load('start_page.png')
                screen.blit(start_page_img, (0, 0))
                pygame.display.update()
                # Wait for the user to go back to the main menu
                while True:
                    # Draw the back button
                    back_button_rect = pygame.Rect(20, 20, 100, 50)
                    pygame.draw.rect(screen, (255, 255, 255), back_button_rect)
                    back_button_font = pygame.font.Font(None, 30)
                    back_button_text = back_button_font.render('Back', True, (0, 0, 0))
                    screen.blit(back_button_text, (30, 30))
                    # Check for events
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            # Check if the mouse clicked on the back button
                            if back_button_rect.collidepoint(event.pos):
                                break  # Go back to the main menu
                    pygame.display.update()
            elif help_button_rect.collidepoint(event.pos):
                # Load the help page image
                help_page_img = pygame.image.load('help_page.png')
                screen.blit(help_page_img, (0, 0))
                pygame.display.update()
                # Wait for the user to go back to the main menu
                while True:
                    # Draw the back button
                    back_button_rect = pygame.Rect(20, 20, 100, 50)
                    pygame.draw.rect(screen, (255, 255, 255), back_button_rect)
                    back_button_font = pygame.font.Font(None, 30)
                    back_button_text = back_button_font.render('Back', True, (0, 0, 0))
                    screen.blit(back_button_text, (30, 30))
                    # Check for events
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            # Check if the mouse clicked on the back button
                            if back_button_rect.collidepoint(event.pos):
                                break  # Go back to the main menu
                    pygame.display.update()

    # Update the screen
    pygame.display.update()

pygame.quit()
