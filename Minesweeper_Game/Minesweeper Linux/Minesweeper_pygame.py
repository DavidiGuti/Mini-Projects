# Example file showing a circle moving on screen
import pygame
import random

def ClickFace(space, action, img_face, check):
	pos = pygame.mouse.get_pos()
	Action = action
	runGame = True
	Face = Button(screen_width/2-32, space-100, img_face, Face_hover, False, 2)
	if pygame.mouse.get_pressed()[0]: 
		if check:
			Face = Button(screen_width/2-32, space-100, Scared, Face_hover, False, 2)
			Face.draw(screen)
		if Face.rect.collidepoint(pos):
			Face = Button(screen_width/2-32, space-100, img_face, Face_hover, False, 2)
			Face.draw(screen)
			Action = True
			runGame = True
		elif Action:
			Face = Button(screen_width/2-32, space-100, img_face, Face_hover, False, 2)
			Face.draw(screen)
			Action = False
			runGame = True
	elif Action:
		Face = Button(screen_width/2-32, space-100, img_face, Face_hover, False, 2)
		Action = True
		runGame = False
	else: 
		Face = Button(screen_width/2-32, space-100, img_face, Face_hover, False, 2)
		Face.draw(screen)
		Action = False
		runGame = True
  
	return Action, runGame
	
  
#Class Button
class Button():
	def __init__(self, x, y, image, image_hover, clicked, scale):
		height = image.get_height()
		width = image.get_width()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.image_hover = pygame.transform.scale(image_hover, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = clicked

	def draw(self, surFace):
		action = self.clicked
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if pygame.key.get_pressed()[pygame.K_LCTRL]:
			surFace.blit(self.image, (self.rect.x, self.rect.y))
			if pygame.mouse.get_pressed()[0]:
				surFace.blit(self.image, (self.rect.x, self.rect.y))
				if self.rect.collidepoint(pos):
					action = "rightClick"
					surFace.blit(self.image_hover, (self.rect.x, self.rect.y))
				elif action:
					action = "Out"
					surFace.blit(self.image, (self.rect.x, self.rect.y))
		elif pygame.mouse.get_pressed()[0]:
			surFace.blit(self.image, (self.rect.x, self.rect.y))
			if self.rect.collidepoint(pos):
				action = True
				surFace.blit(self.image_hover, (self.rect.x, self.rect.y))
			elif action:
				action = "Out"
				surFace.blit(self.image, (self.rect.x, self.rect.y))
    
		elif pygame.mouse.get_pressed()[2]:
			surFace.blit(self.image, (self.rect.x, self.rect.y))
			if self.rect.collidepoint(pos):
				action = "rightClick"
				surFace.blit(self.image_hover, (self.rect.x, self.rect.y))
			elif action:
				action = "Out"
				surFace.blit(self.image, (self.rect.x, self.rect.y))
    
		elif self.rect.collidepoint(pos) and action:
			action = False
			surFace.blit(self.image_hover, (self.rect.x, self.rect.y))
		else:
			surFace.blit(self.image, (self.rect.x, self.rect.y))
			action = False

		#draw button on screen
		
		return action

def except_hashtag(mine_coordinate0, mine_coordinate1):
	mine_coordinate_board = minesweeper[int(random_coordinate[0])+(mine_coordinate0)][int(random_coordinate[1])+(mine_coordinate1)]
	if mine_coordinate_board != "Bomb":				
		mine_coordinate_board += 1
	return mine_coordinate_board

def Game(minesweeper_game, hover, check):
	line_index = 0
	for line in minesweeper_game:
		square_index = 0
		for square in line:
			button_square_pressed = False
			button_image = pygame.image.load(f"Data/{square}.png").convert_alpha()
			button_image_hover = pygame.image.load("Data/Hover.png").convert_alpha()
			button_y = (32*line_index)+space
			button_x = (32*square_index)+space
			if hover and minesweeper_game[line_index][square_index] == "Empty square":
				button_square = Button(button_x, button_y, button_image, button_image_hover, button_square_pressed, 2)
			else:
				button_square = Button(button_x, button_y, button_image, button_image, button_square_pressed, 2)
    
			if check:
				button_square_pressed = button_square.draw(screen)
			else:
				button_square.draw(screen)
   
			if button_square_pressed and check and minesweeper_game[line_index][square_index] == "Empty square":
				return line_index, square_index, button_x, button_y, button_image, button_image_hover, button_square_pressed
			if button_square_pressed == "rightClick" and (minesweeper_game[line_index][square_index] == "Empty square" or minesweeper_game[line_index][square_index] == "Bomb defused"):
				return line_index, square_index, button_x, button_y, button_image, button_image_hover, button_square_pressed

			square_index += 1
		line_index += 1
	if check:
		return line_index, square_index, button_x, button_y, button_image, button_image_hover, False

def checkAround(line_index, square_index, board_range):

	if square_index == 0: 
		if line_index == 0: #Top Left Corner
			list = [(line_index+1, square_index+1)]
			list.append((line_index+1, square_index+2))

			list.append((line_index+2, square_index+1))
			list.append((line_index+2, square_index+2))

		elif line_index == board_range-1: #Bottom Left Corner
			list = [(line_index+1, square_index+1)]
			list.append((line_index+1, square_index+2))

			list.append((line_index, square_index+1))
			list.append((line_index, square_index+2))
   
		else: #Left Col
			list = [(line_index+1, square_index+1)]
			list.append((line_index+2, square_index+1))
			list.append((line_index, square_index+1))

			list.append((line_index+2, square_index+2))
			list.append((line_index+1, square_index+2))
			list.append((line_index, square_index+2))

	elif square_index == board_range-1: #Top Right Corner
	
		if line_index == 0: #Top Right Corner
			list = [(line_index+1, square_index+1)]
			list.append((line_index+1, square_index))

			list.append((line_index+2, square_index+1))
			list.append((line_index+2, square_index))

		elif line_index == board_range-1: #Bottom Right Corner
			list = [(line_index+1, square_index+1)]
			list.append((line_index+1, square_index))

			list.append((line_index, square_index+1))
			list.append((line_index, square_index))
		
		else: #Right Col
			list = [(line_index+1, square_index+1)]
			list.append((line_index+2, square_index+1))
			list.append((line_index, square_index+1))

			list.append((line_index+2, square_index))
			list.append((line_index+1, square_index))
			list.append((line_index, square_index))

	elif line_index == 0: #Top Row
		list = [(line_index+1, square_index+1)]
		list.append((line_index+1, square_index+2))
		list.append((line_index+1, square_index))

		list.append((line_index+2, square_index+2))
		list.append((line_index+2, square_index+1))
		list.append((line_index+2, square_index))

	elif line_index == board_range-1: #Bottom Row
		list = [(line_index+1, square_index+1)]
		list.append((line_index+1, square_index+2))
		list.append((line_index+1, square_index))

		list.append((line_index, square_index+2))
		list.append((line_index, square_index+1))
		list.append((line_index, square_index))

	else: #Middle
		list = [(line_index+1, square_index+1)]
		list.append((line_index+2, square_index+1))
		list.append((line_index, square_index+1))

		list.append((line_index+2, square_index))
		list.append((line_index+1, square_index))
		list.append((line_index, square_index))

		list.append((line_index+2, square_index+2))
		list.append((line_index+1, square_index+2))
		list.append((line_index, square_index+2))
	
	return list

# pygame setup
screen_height = 720
screen_width = 720
screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("Minesweeper")
Icon = pygame.image.load("Data/Icon.ico").convert_alpha()
pygame.display.set_icon(Icon)
clock = pygame.time.Clock()

# Menu Buttons Height 16px Width 49px
Hard_img = pygame.image.load("Data/Hard.png").convert_alpha()
Medium_img = pygame.image.load("Data/Medium.png").convert_alpha()
Easy_img = pygame.image.load("Data/Easy.png").convert_alpha()
Hard_img_hover = pygame.image.load("Data/Hard_hover.png").convert_alpha()
Medium_img_hover = pygame.image.load("Data/Medium_hover.png").convert_alpha()
Easy_img_hover = pygame.image.load("Data/Easy_hover.png").convert_alpha()

#Face Height 21px Width 21px
Happy = pygame.image.load("Data/Happy.png").convert_alpha()
Scared = pygame.image.load("Data/Scared.png").convert_alpha()
Dead = pygame.image.load("Data/Dead.png").convert_alpha()
Sunglasses = pygame.image.load("Data/Sunglasses.png").convert_alpha()
Face_hover = pygame.image.load("Data/Face hover.png").convert_alpha()

Face_clicked = True
while Face_clicked:
	runMenu = True
	runGame = True
	button_pressed_hard = False
	button_pressed_medium = False
	button_pressed_easy = False

	while runMenu and button_pressed_hard == False and button_pressed_medium == False and button_pressed_easy == False:

		hard_button = Button(175, 150, Hard_img, Hard_img_hover, button_pressed_hard, 7.75)
		medium_button = Button(175, 300, Medium_img, Medium_img_hover, button_pressed_medium, 7.75)
		easy_button = Button(175, 450, Easy_img, Easy_img_hover, button_pressed_easy, 7.75)
		screen_start = screen.fill((155, 155, 155))
		button_pressed_hard = hard_button.draw(screen)
		button_pressed_medium = medium_button.draw(screen)
		button_pressed_easy = easy_button.draw(screen)


		while button_pressed_hard:
			hard_button = Button(175, 150, Hard_img, Hard_img_hover, button_pressed_hard, 7.75)
			button_pressed_hard = hard_button.draw(screen)
			medium_button.draw(screen)
			easy_button.draw(screen)
			
			if button_pressed_hard == False:
				button_pressed_hard = True
				button_pressed_medium = False
				button_pressed_easy = False
				break
			
			if button_pressed_hard == "Out":
				button_pressed_hard = False
				button_pressed_medium = False
				button_pressed_easy = False
				break
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					runMenu = False
					runGame = False
		
			pygame.display.update()
			clock.tick(30)

		while  button_pressed_medium:
			medium_button = Button(175, 300, Medium_img, Medium_img_hover, button_pressed_medium, 7.75)
			hard_button.draw(screen)
			button_pressed_medium = medium_button.draw(screen)
			easy_button.draw(screen)
			
			if button_pressed_medium == False:
				button_pressed_hard = False
				button_pressed_medium = True
				button_pressed_easy = False
				break
			
			if button_pressed_medium == "Out":
				button_pressed_hard = False
				button_pressed_medium = False
				button_pressed_easy = False
				break
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					runMenu = False
					runGame = False
		
			pygame.display.update()
			clock.tick(30)
		
		while button_pressed_easy:
			easy_button = Button(175, 450, Easy_img, Easy_img_hover, button_pressed_easy, 7.75)
			hard_button.draw(screen)
			medium_button.draw(screen)
			button_pressed_easy = easy_button.draw(screen)
			
			if button_pressed_easy == False:
				button_pressed_hard = False
				button_pressed_medium = False
				button_pressed_easy = True
				break
			
			if button_pressed_easy == "Out":
				button_pressed_hard = False
				button_pressed_medium = False
				button_pressed_easy = False
				break
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					runMenu = False
					runGame = False
		
			pygame.display.update()
			clock.tick(30)
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				runMenu = False
				runGame = False
		
		pygame.display.update()
		clock.tick(30)


	#Creation of the Minesweeper Blank Board Size with the difficulty chosed

	if button_pressed_easy:
		mines = 10
		board_range = 8
		minesweeper = [[0] * board_range for _ in range(board_range)]
		minesweeper_game = [["Empty square"] * board_range for _ in range(board_range)]
		space = (screen_height/2)-(board_range*32/2)

		total_squares = board_range*board_range-mines

				
	elif button_pressed_medium:

		mines = 25
		board_range = 12
		minesweeper = [[0] * board_range for _ in range(board_range)]
		minesweeper_game = [["Empty square"] * board_range for _ in range(board_range)]
		space = (screen_height/2)-(board_range*32/2)
	
		total_squares = board_range*board_range-mines
			
	elif button_pressed_hard:
		
		mines = 40
		board_range = 16
		minesweeper = [[0] * board_range for _ in range(board_range)]
		minesweeper_game = [["Empty square"] * board_range for _ in range(board_range)]
		space = (screen_height/2)-(board_range*32/2)
	
		total_squares = board_range*board_range-mines

	Face_clicked = False 
	#Creation of the mines in the Minesweeper Board
	while runGame:
		screen_start = screen.fill((155, 155, 155))
		ClickFace(space, Face_clicked, Happy, False)
		Game(minesweeper_game, False, False)
		pygame.display.update()
		pygame.time.delay(200)
		
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				runGame = False
	
		pygame.display.update()
		clock.tick(30)
		break


	button_square_pressed = False
	while runGame and button_square_pressed == False:
		screen_start = screen.fill((155, 155, 155))

		Face_clicked, runGame = ClickFace(space, Face_clicked, Happy, True)
		line_index, square_index, button_x, button_y, button_image, button_image_hover, button_square_pressed = Game(minesweeper_game, True, True)

		while button_square_pressed:
			Face_clicked, runGame = ClickFace(space, Face_clicked, Happy, True)
			Game(minesweeper_game, False, False)
			button_square = Button(button_x, button_y, button_image, button_image_hover, button_square_pressed, 2)
			button_square_pressed = button_square.draw(screen)
			

			if button_square_pressed == False:
				Face_clicked, runGame = ClickFace(space, Face_clicked, Happy, True)
				mines_coordinates = checkAround(line_index, square_index, board_range)
				minesweeper_game[line_index][square_index] = 0	
				button_square_pressed = True
				break

			if button_square_pressed == "Out":
				button_square_pressed = False
				break
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					runGame = False
			
			pygame.display.update()
			clock.tick(30)
	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				runGame = False
	
		pygame.display.update()
		clock.tick(30)


	if runGame:
		add_mine = False
		for x in range(0, mines):
			add_mine = True
			random_coordinate = random.randint(1, len(minesweeper)), random.randint(1, len(minesweeper))
			for mine in mines_coordinates:
				if mine == random_coordinate:
					add_mine = False
					break

			while add_mine == False:
				add_mine = True
				random_coordinate = random.randint(1, len(minesweeper)), random.randint(1, len(minesweeper))
				for mine in mines_coordinates:
					if mine == random_coordinate:
						add_mine = False
						break

	#Creation of the square mines in the minesweeper

			mines_coordinates.append(random_coordinate)
			minesweeper[int(random_coordinate[0])-1][int(random_coordinate[1])-1] = "Bomb"

	#Creation of the squares 1, 2, 3, 4, 5, 6, 7, 8 (+1 all directions)

			if random_coordinate[0] < len(minesweeper):
				minesweeper[int(random_coordinate[0])][int(random_coordinate[1])-1] = except_hashtag(0, -1)
				
				if random_coordinate[1] < len(minesweeper):
					minesweeper[int(random_coordinate[0])][int(random_coordinate[1])] = except_hashtag(0, 0)

				if random_coordinate[1]-2 >= 0:
					minesweeper[int(random_coordinate[0])][int(random_coordinate[1])-2] = except_hashtag(0, -2)
			

			if random_coordinate[1] < len(minesweeper):
				minesweeper[int(random_coordinate[0])-1][int(random_coordinate[1])] = except_hashtag(-1, 0)
				
				if random_coordinate[0]-2 >= 0:
					minesweeper[int(random_coordinate[0])-2][int(random_coordinate[1])] = except_hashtag(-2, 0)


			if random_coordinate[0]-2 >= 0:
				minesweeper[int(random_coordinate[0])-2][int(random_coordinate[1])-1] = except_hashtag(-2, -1)

				if random_coordinate[1]-2 >= 0:
					minesweeper[int(random_coordinate[0])-2][int(random_coordinate[1])-2] = except_hashtag(-2, -2)
			
			
			if random_coordinate[1]-2 >= 0:
				minesweeper[int(random_coordinate[0])-1][int(random_coordinate[1])-2] = except_hashtag(-1, -2)
			
	#Print of the Minesweeper Board in the console

	def checkAroundZero(minesweeper_game):
		for x in range(16):
			line_index = 0
			for line in minesweeper_game:
				square_index = 0
				for square in line:
					if minesweeper_game[line_index][square_index] == 0:
						AroundCoordinates = checkAround(line_index, square_index, board_range)
						for coordinate in AroundCoordinates:
							minesweeper_game[coordinate[0]-1][coordinate[1]-1] = minesweeper[coordinate[0]-1][coordinate[1]-1]
					square_index += 1
				line_index += 1
	
	checkAroundZero(minesweeper_game)

	lose = False
	while runGame and lose == False:

		screen_start = screen.fill((155, 155, 155))
	
		Face_clicked, runGame = ClickFace(space, Face_clicked, Happy, True)
		line_index, square_index, button_x, button_y, button_image, button_image_hover, button_square_pressed = Game(minesweeper_game, True, True)
		
		while button_square_pressed == "rightClick" and (minesweeper_game[line_index][square_index] == "Empty square" or minesweeper_game[line_index][square_index] == "Bomb defused"):
			
			Game(minesweeper_game, False, False)
			button_image = pygame.image.load("Data/Bomb defused.png").convert_alpha()
			button_square = Button(button_x, button_y, button_image, button_image, False, 2)
			button_square_pressed = button_square.draw(screen)

			if button_square_pressed == False:
				if minesweeper_game[line_index][square_index] == "Empty square": 
					minesweeper_game[line_index][square_index] = "Bomb defused"
					button_image = pygame.image.load("Data/Bomb defused.png").convert_alpha()
				else:
					minesweeper_game[line_index][square_index] = "Empty square"
					button_image = pygame.image.load("Data/Empty square.png").convert_alpha()
			
				button_square = Button(button_x, button_y, button_image, button_image, False, 2)
				button_square.draw(screen)
				pygame.display.update()
	
			if button_square_pressed == "Out":
				button_square_pressed = "rightClick"
	
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					runGame = False
			pygame.display.update()
			clock.tick(30)
	
	
		while button_square_pressed and minesweeper_game[line_index][square_index] == "Empty square" and button_square_pressed != "rightClick":
			Face_clicked, runGame = ClickFace(space, Face_clicked, Happy, True)
			Game(minesweeper_game, True, False)
			button_square = Button(button_x, button_y, button_image, button_image_hover, button_square_pressed, 2)
			button_square_pressed = button_square.draw(screen)
			
			if button_square_pressed == False:
				minesweeper_game[line_index][square_index] = minesweeper[line_index][square_index]
				button_image = pygame.image.load(f"Data/{minesweeper[line_index][square_index]}.png").convert_alpha()
				button_square = Button(button_x, button_y, button_image, button_image, button_square_pressed, 2)
				button_square.draw(screen)
				checkAroundZero(minesweeper_game)
				pygame.display.update()
				if minesweeper[line_index][square_index] == "Bomb":
					lose = True
					minesweeper[line_index][square_index] = "Bomb exploded"
					break

			if button_square_pressed == "Out":
				break
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					runGame = False
			pygame.display.update()
			clock.tick(30)

		counted_squares = 0
		line_index = 0
		for line in minesweeper_game:
			square_index = 0
			for square in line:
				if minesweeper_game[line_index][square_index] == minesweeper[line_index][square_index] and minesweeper_game[line_index][square_index] != "Bomb":
					counted_squares += 1
				square_index += 1
			line_index += 1
		
		if counted_squares == total_squares:
			line_index = 0
			for line in minesweeper_game:
				square_index = 0
				for square in line:
					if square == "Empty square":
						minesweeper_game[line_index][square_index] = "Bomb defused"
					square_index += 1
				line_index += 1

			Game(minesweeper_game, True, False)
			while runGame:
				Face_clicked, runGame = ClickFace(space, Face_clicked, Sunglasses, False)
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						runGame = False
				pygame.display.update()
				clock.tick(30)
			
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				runGame = False
		pygame.display.update()
		clock.tick(30)

	if lose:
		line_index = 0
		for line in minesweeper:
			square_index = 0
			for square in line:
				if square != "Bomb" and minesweeper_game[line_index][square_index] == "Bomb defused":
					minesweeper[line_index][square_index] = "Defused failed"
				elif square == "Bomb" and minesweeper_game[line_index][square_index] == "Bomb defused":
					minesweeper[line_index][square_index] = "Bomb defused"
				if square != "Bomb" and square != "Bomb exploded" and minesweeper_game[line_index][square_index] != "Bomb defused":
					minesweeper[line_index][square_index] = minesweeper_game[line_index][square_index]
				
				square_index += 1
			line_index += 1
		

		while runGame:
			line_index = 0
			for line in minesweeper:
				square_index = 0
				if runGame == False:
						break
				for square in line:   
					button_image = pygame.image.load(f"Data/{square}.png").convert_alpha()
					button_y = (32*line_index)+space
					button_x = (32*square_index)+space
					Face = Button(screen_width/2-21, space-50, Dead, Dead, False, 2)
					Face_clicked, runGame = ClickFace(space, Face_clicked, Dead, False)
					if runGame == False:
						break
					button_square = Button(button_x, button_y, button_image, button_image, button_square_pressed, 2)
					button_square.draw(screen)
		
					square_index += 1
				line_index += 1		
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					runGame = False
			
			pygame.display.update()
			clock.tick(30)

pygame.quit()