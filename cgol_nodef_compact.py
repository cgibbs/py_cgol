import libtcodpy as libtcod
(SCREEN_HEIGHT, SCREEN_WIDTH) = (48, 80)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'CGOL', False)
(mouse, key, living, board) = (libtcod.Mouse(), libtcod.Key(), 0, [[0 for y in range(SCREEN_HEIGHT)] for x in range(SCREEN_WIDTH)])
while True:
	libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
	if key.vk == libtcod.KEY_ESCAPE: break
	elif key.vk == libtcod.KEY_ENTER: living = not living
	elif key.vk == libtcod.KEY_SPACE: board = cycle_board(board)
	board[mouse.cx][mouse.cy] = (1 if mouse.lbutton else 0 if mouse.rbutton else board[mouse.cx][mouse.cy])
	if living: board = [[(0 if x == 0 or x == SCREEN_WIDTH - 1 or y == 0 or y == SCREEN_HEIGHT - 1 else 1 < sum(board[x-1][y-1:y+2] + board[x+1][y-1:y+2]) + board[x][y-1] + board[x][y+1] < 4 if board[x][y] else 3 == sum(board[x-1][y-1:y+2] + board[x+1][y-1:y+2]) + board[x][y-1] + board[x][y+1]) for y in range(SCREEN_HEIGHT)] for x in range(SCREEN_WIDTH)]
	[[libtcod.console_put_char(0, x, y, chr(176 * board[x][y]), libtcod.BKGND_NONE) for y in range(SCREEN_HEIGHT)] for x in range(SCREEN_WIDTH)]
	libtcod.console_flush()