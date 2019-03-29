board = {
	'tl': ' ', 'tm': ' ', 'tr': ' ',
	'ml': ' ', 'mm': ' ', 'mr': ' ',
	'bl': ' ', 'bm': ' ', 'br': ' '
}

def print_board():
	to_print = '{}|{}|{}\n'.format(board['tl'], board['tm'], board['tr'])
	to_print += '------\n'
	to_print += '{}|{}|{}\n'.format(board['ml'], board['mm'], board['mr'])
	to_print += '------\n'
	to_print += '{}|{}|{}\n'.format(board['bl'], board['bm'], board['br'])
	print(to_print)

def alternate(current):
	if current == 'X':
		return 'O'
	else:
		return 'X'

def updated_square(square, current):
	try:
		if board[square] == ' ':
			board[square] = current
			return True
		else:
			print("Square already occupied.  Please pick another square.")
			return False
	except KeyError:
		print("Invalid square.  Please try again.")
		return False

def all_squares_occupied():
	for key, value in board.items():
		if value == ' ':
			return False
	return True

def is_winner(current):
	if (board['tl'] == current) and (board['tm'] == current) and (board['tr'] == current):
		return True
	elif (board['tl'] == current) and (board['ml'] == current) and (board['bl'] == current):
		return True
	elif (board['tl'] == current) and (board['mm'] == current) and (board['br'] == current):
		return True
	elif (board['tm'] == current) and (board['mm'] == current) and (board['bm'] == current):
		return True
	elif (board['tr'] == current) and (board['mm'] == current) and (board['bl'] == current):
		return True
	elif (board['tr'] == current) and (board['mr'] == current) and (board['br'] == current):
		return True
	elif (board['ml'] == current) and (board['mm'] == current) and (board['mr'] == current):
		return True
	elif (board['bl'] == current) and (board['bm'] == current) and (board['br'] == current):
		return True
	else:
		return False

def is_game_done(current):
	if is_winner(current):
		print("Congrats player {}!  You won!".format(current))
		return True
	elif all_squares_occupied():
		print("No winner :(")
		return True
	return False

if __name__ == "__main__":
	print("Welcome to a game of tic tac toe!")
	done = False
	current = 'X'
	while not done:
		print("Please enter a square to mark")
		print_board()
		square = input()
		updated_square(square, current)
		if not updated_square:
			continue
		else:
			done = is_game_done(current)
			current = alternate(current)
