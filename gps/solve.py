import math
flag = ''
for i in range(1,13):
	x ,y =0,0
	path = open("input/"+str(i)+".txt").read().split('\n')[1:-1]
	for p in path:
		if p[:5] == "north":
			y += 1
		if p[:5] == "south":
			y -= 1
		if p[-4:] == "east":
			x += 1
		if p[-4:] == "west":
			x -= 1
	distance = math.sqrt((x*2)**2 + (y*2)**2)
	flag += chr(int((round(distance)%26)+97))
print flag