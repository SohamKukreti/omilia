import pygame
import sys

def language_call():
    # Load the start page image
                pygame.init()
                screen_width = 1000
                screen_height = 1000

                screen = pygame.display.set_mode((screen_width, screen_height))
                pygame.display.set_caption('Language Selector')



                englishImg = pygame.image.load("menuAssets/English_Button.png")
                hindiImg = pygame.image.load("menuAssets/Hindi_Button.png")
                englishImgold = englishImg
                hindiImgold = hindiImg
                englishButton = pygame.Rect(370, 220, 240, 70)
                hindiButton = pygame.Rect(390,350,200,75)

                start_page_img = pygame.image.load('menuAssets/language_page.png')
                screen.blit(start_page_img, (0, 0))
                pygame.display.update()

                # Wait for the user to go back to the main menu
                back_flag = False
                while not back_flag:
                    # Draw the back button
                    click = False
                    back = pygame.image.load('menuAssets/back.png')
                    mx, my = pygame.mouse.get_pos()
                    back_button_rect = pygame.Rect(20, 20, back.get_width(), back.get_height())
                    screen.blit(back, back_button_rect)
                    screen.blit(englishImg,(340,200))
                    screen.blit(hindiImg,(340,320))
                    #pygame.draw.rect(screen, (255, 255, 255), englishButton)
                    #pygame.draw.rect(screen, (255, 255, 255), hindiButton)
                    # back_button_rect = pygame.Rect(20, 20, 100, 50)
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
                            click = True
                            if back_button_rect.collidepoint(event.pos):
                                back_flag = True  # Go back to the main menu
                                break

                    if hindiButton.collidepoint((mx,my)):
                                hindiImgNew = pygame.transform.scale(hindiImg, (300,180))
                                hindiImg = hindiImgNew
                                if click == True:
                                    print("running hindi")
                    if englishButton.collidepoint((mx,my)):
                                englishImgNew = pygame.transform.scale(englishImg, (215, 90))
                                englishImg = englishImgNew
                                if click == True:
                                    print("running english")
                    hindiImg = hindiImgold
                    englishImg = englishImgold
                    pygame.display.update()
                    
language_call()