import pygame
import sys
def prompt():

	# initialize Pygame
	pygame.init()
	gamestate = "prof"
	# set the window size
	window_size = (1000, 1000)

	# create the window
	window = pygame.display.set_mode(window_size)

	# set the font
	textfont=pygame.font.Font("img/CompassPro.ttf",32)
	text = '''Marty, Try to guess what the word!'''

	#question_img = pygame.image.load("img/english/q1.png")


	bgimg = pygame.image.load("img/english/questionbg.png")
	appleimg = pygame.image.load("img/english/appleques.png")
	profimg = pygame.image.load("img/profslide.png")
	# main game loop
	running = True
	while running:
		# handle events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				# check if the user clicked on an option
				mouse_pos = pygame.mouse.get_pos()
				option_y = 100
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False
				if event.key == pygame.K_RETURN:
					if gamestate == "prof":
						gamestate = "play"
		# clear the screen
		window.fill((255, 255, 255))
		if gamestate == "prof":
			window.blit(profimg,(0,0))
			proftext=textfont.render(text,True,(255,255,255))
			window.blit(proftext, (550, 600))
		if gamestate == "play":
			window.blit(bgimg,(0,0))
			window.blit(appleimg,(150,35))

		# update the screen
		pygame.display.update()


