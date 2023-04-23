import pygame 
import sys
from language_menu import language_call
from help_menu import help_call

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
                language_call()
            elif help_button_rect.collidepoint(event.pos):
                help_call()

    # Update the screen
    pygame.display.update()

pygame
