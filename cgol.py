import libtcodpy as libtcod

SCREEN_HEIGHT = 48
SCREEN_WIDTH = 80
libtcod.console_set_custom_font('arial12x12.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'CGOL', False)
libtcod.sys_set_fps(24)

def check_life(board, x, y):
	if x == 0 or x == SCREEN_WIDTH or y == 0 or y == SCREEN_HEIGHT:
		return 0
	if board[x][y] == 1:
		return 1 < sum_neighbors(board, x, y) < 4
	return 3 == sum_neighbors(board, x, y)

def sum_neighbors(board, x, y):
	return (sum(board[x-1][y-1:y+2] + board[x+1][y-1:y+2]) + board[x][y-1] + board[x][y+1])

def cycle_board(board):
	new_board = [[0 for y in range(SCREEN_HEIGHT)] for x in range(SCREEN_WIDTH)]
	for x in range(1, SCREEN_WIDTH - 1):
		for y in range(1, SCREEN_HEIGHT - 1):
			new_board[x][y] = check_life(board, x, y)
	return new_board

def main():
	mouse = libtcod.Mouse()
	key = libtcod.Key()

	old_m_pos = (0, 0)
	living = 0

	board = [[0 for y in range(SCREEN_HEIGHT)] for x in range(SCREEN_WIDTH)]

	libtcod.console_set_default_foreground(0, libtcod.white)

	while True:
		libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
		if key.vk == libtcod.KEY_ESCAPE:
			break  #exit game
		elif key.vk == libtcod.KEY_ENTER:
			living = not living
		elif key.vk == libtcod.KEY_SPACE:
			board = cycle_board(board)

		if mouse.lbutton:
			board[mouse.cx][mouse.cy] = 1
		elif mouse.rbutton:
			board[mouse.cx][mouse.cy] = 0

		if living:
			board = cycle_board(board)

		for x in range(0, len(board)):
			for y in range(0, len(board[x])):
				try:
					libtcod.console_put_char(0, x, y, chr(176 * board[x][y]), libtcod.BKGND_NONE)
				except:
					print board[x][y]

		libtcod.console_flush()

if __name__ == "__main__":
	main()