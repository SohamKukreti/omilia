import pygame
import sys
from EnglishPlatformer import engplatform
from HindiPlatformer import hindplatform
from BanglaPlatformer import banglaplatform
from guide_English import guide_english_call
from guide_Hindi import guide_hindi_call
from guide_Bangla import guide_bangla_call
import consts as c

pygame.init()
def language_call():
    # Load the start page image
                

                screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT), pygame.RESIZABLE)
                pygame.display.set_caption('Omilia')



                englishImg = pygame.image.load("menuAssets/English_Button.png")
                hindiImg = pygame.image.load("menuAssets/Hindi_Button.png")
                banglaImg = pygame.image.load("menuAssets/Bengali_Button.png")
                englishImgold = englishImg
                hindiImgold = hindiImg
                banglaImgold = banglaImg
                englishButton = pygame.Rect(370, 220, 240, 70)
                hindiButton = pygame.Rect(390,350,200,75)
                banglaButton = pygame.Rect(370, 460, 230, 75)

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
                    screen.blit(banglaImg,(350,440))
                    #pygame.draw.rect(screen, (255, 255, 255), englishButton)
                    #pygame.draw.rect(screen, (255, 255, 255), banglaButton)
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
                                    guide_hindi_call()
                                    hindplatform()
                                    print("running hindi")
                    if englishButton.collidepoint((mx,my)):
                                englishImgNew = pygame.transform.scale(englishImg, (215, 90))
                                englishImg = englishImgNew
                                if click == True:
                                    guide_english_call()
                                    engplatform()
                                    print("running english")
                    if banglaButton.collidepoint((mx,my)):
                                banglaImgNew = pygame.transform.scale(banglaImg, (215, 90))
                                banglaImg = banglaImgNew
                                if click == True:
                                    guide_bangla_call()
                                    banglaplatform()
                                    print("running Bengali")
                    hindiImg = hindiImgold
                    englishImg = englishImgold
                    banglaImg = banglaImgold
                    pygame.display.update()
                    
