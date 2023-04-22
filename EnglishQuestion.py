import pygame
import sys
import random
def prompt(level):

	# initialize Pygame
	pygame.init()
	if level == 0:
		gamestate = "prof"
	else:
		gamestate = "play"
	# set the window size
	window_size = (1000, 1000)

	# create the window
	window = pygame.display.set_mode(window_size)

	# set the font

	textfont=pygame.font.Font("img/CompassPro.ttf",32)
	text = '''Marty, Try to guess what the word!'''
	images = ["img/english/cat.jpg","img/english/dog.jpg","img/english/pencil.jpg"]
	ansKey = [1,4,4]
	n = random.randint(0,2)
	ques_img = pygame.image.load(images[n])
	selectedAns = -1
	print(ansKey[n])
	optionSound = pygame.mixer.Sound("img/optionsound.mp3")
	correctSound = pygame.mixer.Sound("img/rightans.mp3")
	wrongSound = pygame.mixer.Sound("img/wrongans.wav")
	pygame.mixer.music.load("img/questionbg.wav")
	pygame.mixer.music.play(-1)


	#creating the buttons

	button1 = pygame.Rect(100, 255, 290, 300)
	button2 = pygame.Rect(610, 255, 290, 300)
	button3 = pygame.Rect(100, 625, 290, 300)
	button4 = pygame.Rect(610, 635, 290, 300)

	bgimg = pygame.image.load("img/english/questionbg.png")
	appleimg = pygame.image.load("img/english/appleques.png")
	profimg = pygame.image.load("img/profslide.png")




	# main game loop
	running = True
	while running:
		mx, my = pygame.mouse.get_pos()
		click = False
		# handle events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False
				if event.key == pygame.K_RETURN:
					if gamestate == "prof":
						gamestate = "play"
		# clear the screen
		window.fill((255, 255, 255))
		if gamestate == "prof" and level == 0:
			window.blit(profimg,(0,0))
			proftext=textfont.render(text,True,(255,255,255))
			window.blit(proftext, (550, 600))
		if gamestate == "play":
			window.blit(ques_img,(0,0))
			#window.blit(appleimg,(150,35))
			#pygame.draw.rect(window, (255, 255, 255), button1)
			#pygame.draw.rect(window, (255, 255, 255), button2)
			#pygame.draw.rect(window, (255, 255, 255), button3)
			#pygame.draw.rect(window, (255, 255, 255), button4)
			if button1.collidepoint((mx, my)):
				if click:
					optionSound.play()
					print("button1")
					selectedAns = 1
					if selectedAns == ansKey[n]:
						correctSound.play()
						print("successful")
						return 1
					else:
						wrongSound.play()
						return -1

			if button2.collidepoint((mx, my)):
				if click:
					optionSound.play()
					print("button2")
					selectedAns = 2
					if selectedAns == ansKey[n]:
						correctSound.play()
						print("successful")
						return 1
					else:
						wrongSound.play()
						return -1
			if button3.collidepoint((mx, my)):
				if click:
					optionSound.play()
					print("button3")
					selectedAns = 3
					if selectedAns == ansKey[n]:
						correctSound.play()
						print("successful")
						return 1
					else:
						wrongSound.play()
						return -1
			if button4.collidepoint((mx, my)):
				if click:
					optionSound.play()
					print("button4")
					selectedAns = 4
					if selectedAns == ansKey[n]:
						correctSound.play()
						print("successful")
						return 1
					else:
						wrongSound.play()
						return -1
		# update the screen
		pygame.display.update()


