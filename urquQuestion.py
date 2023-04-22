import pygame
import sys
def prompt1():

	# initialize Pygame
	pygame.init()

	# set the window size
	window_size = (1000, 1000)

	# create the window
	window = pygame.display.set_mode(window_size)

	# set the font
	font = pygame.font.SysFont(None, 30)

	#question_img = pygame.image.load("img/english/q1.png")


	bgimg = pygame.image.load("img/english/questionbg.png")
	appleimg = pygame.image.load("img/english/appleques.png")

	# main game loop
	running = True
	while running:
		# handle events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				# check if the user clicked on an option
				mouse_pos = pygame.mouse.get_pos()
				option_y = 100

		# clear the screen
		window.fill((255, 255, 255))
		window.blit(bgimg,(0,0))
		window.blit(appleimg,(100,0))
		#window.blit(question_img,(150,0))
		# update the screen
		pygame.display.update()


prompt1()