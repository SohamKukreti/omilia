import pygame
import sys
import random
import consts as c
def prompt(level):

	# initialize Pygame
	pygame.init()
	if level == 0:
		gamestate = "prof"
	else:
		gamestate = "play"
	# set the window size

	# create the window
	window = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))

	# set the font

	textfont=pygame.font.Font("English/img/CompassPro.ttf",32)
	text = '''Marty, Try to guess what the word!'''
	images = ["English/img/english/q1.png","English/img/english/q2.png","English/img/english/q3.png","English/img/english/q4.png","English/img/english/q5.png","English/img/english/q6.png","English/img/english/q7.png","English/img/english/q8.png","English/img/english/q9.png","English/img/english/q10.png","English/img/english/q11.png","English/img/english/q12.png","English/img/english/q13.png","English/img/english/q14.png","English/img/english/q15.png","English/img/english/q16.png","English/img/english/q17.png","English/img/english/q18.png","English/img/english/q19.png","English/img/english/q20.png"]
	ansKey = [1,4,4,2,3,2,1,4,1,3,1,2,1,3,2,3,3,1,3,1]
	n = random.randint(0,19)
	ques_img = pygame.image.load(images[n])
	selectedAns = -1
	print(ansKey[n])
	optionSound = pygame.mixer.Sound("English/img/optionsound.mp3")
	correctSound = pygame.mixer.Sound("English/img/rightans.mp3")
	wrongSound = pygame.mixer.Sound("English/img/wrongans.wav")
	pygame.mixer.music.load("English/img/questionbg.wav")
	pygame.mixer.music.play(-1)


	#creating the buttons

	button1 = pygame.Rect(100, 255, 290, 300)
	button2 = pygame.Rect(610, 255, 290, 300)
	button3 = pygame.Rect(100, 625, 290, 300)
	button4 = pygame.Rect(610, 635, 290, 300)

	bgimg = pygame.image.load("English/img/english/questionbg.png")
	appleimg = pygame.image.load("English/img/english/appleques.png")
	profimg = pygame.image.load("English/img/profslide.png")




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


