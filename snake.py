import pygame

class Snake:
	def __init__(self):
		self.head = [45, 45]
		self.body = [[45, 45], [34, 45], [23, 45]]

	def move(self, control):
		"""Движение змеи в зависимости от направления"""
		if control.flag_direction == 'RIGHT':
			self.head[0] += 11
		elif control.flag_direction == 'LEFT':
			self.head[0] -= 11
		elif control.flag_direction == 'UP':
			self.head[1] -= 11
		elif control.flag_direction == 'DOWN':
			self.head[1] += 11

	def animation(self):
		"""Прибавдяем в список тела голову, а хвост удаляем"""
		self.body.insert(0, list(self.head))
		self.body.pop()

	def draw_snake(self, window):
		"""Отрисовка змеи на экране"""
		for segment in self.body:
			pygame.draw.rect(window, pygame.Color('Green'), pygame.Rect(segment[0], segment[1], 10, 10))

	def check_end_window(self):
		"""Отслеживает достидение змеёй края экрана"""
		if self.head[0] == 419:
			self.head[0] = 23
		elif self.head[0] == 12:
			self.head[0] = 419
		elif self.head[1] == 23:
			self.head[1] = 419
		elif self.head[1] == 419:
			self.head[1] = 34

	def eat(self, food, gui):
		"""Змея ест еду"""
		if self.head == food.food_position:
			self.body.append(food.food_position)
			food.get_food_position(gui)
			gui.get_new_indicator()

	def check_barrier(self, gui):
		"""Проверяет не верзалась ли змея куда то"""
		if self.head in gui.barrier:
			self.body.pop()
			gui.indicator.pop()
		elif self.head in self.body[1:]:
			self.body.pop()
			gui.indicator.pop()

	#UNCOMMENT FOR DECLARE DEBUG METHOD
	# def update_body_window(self, window):
	# 	count = 1
	# 	x = 23
	# 	y = 34
	# 	for segment in self.body:
	# 		text = '{}:{}'.format(str(count), str(segment))
	# 		font = pygame.font.Font('/home/arthur/Programs/Snake_game_train/Baloo2-Regular.ttf', 12)
	# 		text = font.render(text, True, pygame.Color('Red'))
	# 		window.blit(text, (x, y))
	# 		count += 1
	# 		y += 20
	# 		if x == 223:
	# 			x = 100
	# 			y = 34



