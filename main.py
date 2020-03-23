import pygame 
from control import Control
from snake import Snake
from gui import Gui
from food import Food

pygame.init()

window = pygame.display.set_mode((441, 441))
window1 = pygame.display.set_mode((441, 441))

control = Control()
snake = Snake()
gui = Gui()
food = Food()

var_speed = 0

gui.init_field()
food.get_food_position(gui)
# gui.create_image()

while control.flag_game:
	gui.chech_win_lose()
	control.control()
	window.fill(pygame.Color('Black'))
	if gui.game == 'GAME':
		snake.draw_snake(window)
		food.draw_food(window)
	elif gui.game == 'WIN':
		gui.draw_win(window)
	elif gui.game == 'LOSE':
		gui.draw_lose(window)
	gui.draw_indicator(window)
	gui.draw_level(window)
	# snake.update_body_window(window1) #UNCOMMENT FOR DEBUG
	if var_speed % 50 == 0 and control.flag_pause and gui.game == 'GAME':
		snake.move(control)
		snake.check_barrier(gui)
		snake.eat(food, gui)
		snake.check_end_window()
		snake.animation()
	var_speed += 1
	pygame.display.flip()