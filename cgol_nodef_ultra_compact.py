import libtcodpy as l
(H,W) = (48,80)
l.console_init_root(W,H,'CGOL',0)
def cb(b):return [[0 if x==0 or x==W-1 or y==0 or y==H-1 else 1<sum(b[x-1][y-1:y+2]+b[x+1][y-1:y+2])+b[x][y-1]+b[x][y+1]<4 if b[x][y] else 3==sum(b[x-1][y-1:y+2]+b[x+1][y-1:y+2])+b[x][y-1]+b[x][y+1] for y in range(H)] for x in range(W)]
(m,k,i,b)=(l.Mouse(),l.Key(),0,[[0 for y in range(H)] for x in range(W)])
while 1:
	l.sys_check_for_event(l.EVENT_KEY_PRESS|l.EVENT_MOUSE,k,m)
	if k.vk==l.KEY_ESCAPE:break
	elif k.vk==l.KEY_ENTER:i=not i
	elif k.vk==l.KEY_SPACE:b=cb(b)
	b[m.cx][m.cy]=(1 if m.lbutton else 0 if m.rbutton else b[m.cx][m.cy])
	if i:b=cb(b)
	[[l.console_put_char(0,x,y,chr(176*b[x][y]),l.BKGND_NONE) for y in range(H)] for x in range(W)]
	l.console_flush()