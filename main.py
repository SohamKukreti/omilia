import pygame 

pygame.init()


screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')


bg_img = pygame.image.load('oi.png')
start_button = pygame.image.load('start1.png')
#start_button = pygame.Rect(50, 250, 200, 75)


run = True
while run:

	

	screen.blit(bg_img, (0, 0))
	screen.blit(start_button, (380, 400))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()