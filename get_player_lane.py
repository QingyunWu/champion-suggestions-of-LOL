# this script is to pick 5 top champions of the specific player from the master_clean dataset
from collections import OrderedDict
top_5_champs = []
TOP =[14, 17, 23, 27, 36, 39, 41, 48, 54, 57, 58, 62, 68, 75, 78, 80, 82, 83, 85, 86, 92, 98, 114, 122, 126, 133, 150, 240, 266, 420]
JUNGLE =[2, 5, 11, 19, 20, 24, 28, 32, 33, 35, 56, 59, 60, 64, 72, 76, 77, 79, 102, 104, 106, 107, 113, 120, 121, 154, 203, 254, 421, 427]
BOTTOM =[12, 15, 16, 18, 21, 22, 25, 29, 37, 40, 43, 44, 51, 53, 67, 81, 89, 111, 117, 119, 143, 201, 202, 222, 223, 236, 267, 412, 429, 432]
MIDDLE = [1, 3, 4, 6, 7, 8, 9, 10, 13, 26, 30, 31, 34, 38, 42, 45, 50, 55, 61, 63, 69, 74, 84, 90, 91, 96, 99, 101, 103, 105, 110, 112, 115, 127, 131, 134, 136, 157, 161, 163, 238, 245, 268]

def get_lane_of_the_player():
	top_points = 0
	jug_points = 0
	bot_points = 0
	mid_points = 0
	index = 10
	for x in top_5_champs:
		if x[0] in TOP:
			top_points += index
		elif x[0] in JUNGLE:
			jug_points += index
		elif x[0] in BOTTOM:
			bot_points += index
		else:
			mid_points += index
		index -= 1
	max_pints = 0
	max_points = max(top_points, jug_points, bot_points, mid_points)
	print "max_points" + str(max_points)
	if mid_points == max_points:
		print "mid player"
	elif top_points == max_points:
		print "top player"
	elif bot_points == max_points:
		print "bot player"
	elif jug_points == max_points:
		print "jug player"

def get_top_5_champs(playerID):
	file = open('mastery_clean.txt', 'r')
	champions_list_of_player = []
	while 1:
		line = file.readline()
		if not line:
			break
		if line.split("\t")[0] == playerID:
			champions_list_of_player.append(line.split("\t")[1])
	file.close()
	dic = {}
	for s in champions_list_of_player:
		dic[(int)(s.split(',')[0])] = (int)(s.split(',')[1])

	d_sorted_by_value = OrderedDict(reversed(sorted(dic.items(), key=lambda x: x[1])))
	index = 0
	for x in d_sorted_by_value.items():
		if index < 5:
			top_5_champs.append(x)
		index += 1
	print top_5_champs

get_top_5_champs('102657')
get_lane_of_the_player()