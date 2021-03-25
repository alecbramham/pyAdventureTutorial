import sys
import items
import enemies
from player import Player
import world


def help_page():
	print('n or north move the player North')
	print('s or south will move the player South')
	print('e or east will move the player East')
	print('w or west will move the player West')
	print('i or inv will open the player inventory')
	print('q or quit will end the game')
	print('Capitalisation is ignored, have fun!')
	
	
def play():
	print('Escape from White Wolf Mountain')
	print('Type h or help for instructions')
	player = Player()
	while True:
		room = world.tile_at(player.x, player.y)
		print(room.intro_text())
		room.modify_player(player)
		action_input = get_player_command()
		if action_input in ['n', 'north', 'up', 'N', 'North', 'Up']:
			player.move_north()
		elif action_input in ['s', 'S', 'south', 'South', 'down', 'Down']:
			player.move_south()
		elif action_input in ['e', 'E', 'east', 'East', 'right', 'Right']:
			player.move_east()
		elif action_input in ['w', 'W', 'west', 'West', 'left', 'Left']:
			player.move_west()
		elif action_input in ['h', 'H', 'heal', 'Heal']:
			player.heal()
		elif action_input in ['?']:
			help_page()
		elif action_input in ['i', 'I', 'inv', 'Inv', 'inventory', 'Inventory']:
			player.print_inventory()
		elif action_input in ['a', 'A', 'attack', 'Attack']:
			player.attack()
		elif action_input in ['q', 'Q', 'exit', 'Exit', 'quit', 'Quit']:
			game_quit()
		else:
			print('Incorrect Syntax')
			print('Please try again')
			
			
def game_quit():
	print('Thanks for playing!')
	sys.exit()
	
	
def get_player_command():
	return input('Action: ')
	
	
play()
