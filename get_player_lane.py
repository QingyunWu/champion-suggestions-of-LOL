# this script is to pick 5 top champions of the specific player from the master_clean dataset
# compare the 5 champs with the 4 lists, derive the main lane of the player
from collections import OrderedDict
import json
import argparse
import random

top_5_champs = []
top_5_champ_names = []
# hadoop to get average win_rate and champ_points for every champ ID
win_rates = {}
champ_points = {}


champion_names = {}

top_win_rates = {}
mid_win_rates = {}
bot_win_rates = {}
jug_win_rates = {}

top_10_win_rate_champs = {}
champ_selct_suggestions = {}


TOP =[14, 17, 23, 27, 36, 39, 41, 48, 54, 57, 58, 62, 68, 75, 78, 80, 82, 83, 85, 86, 92, 98, 114, 122, 126, 133, 150, 240, 266, 420]
JUNGLE =[2, 5, 11, 19, 20, 24, 28, 32, 33, 35, 56, 59, 60, 64, 72, 76, 77, 79, 102, 104, 106, 107, 113, 120, 121, 154, 203, 254, 421, 427]
BOTTOM =[12, 15, 16, 18, 21, 22, 25, 29, 37, 40, 43, 44, 51, 53, 67, 81, 89, 111, 117, 119, 143, 201, 202, 222, 223, 236, 267, 412, 429, 432]
MIDDLE = [1, 3, 4, 6, 7, 8, 9, 10, 13, 26, 30, 31, 34, 38, 42, 45, 50, 55, 61, 63, 69, 74, 84, 90, 91, 96, 99, 101, 103, 105, 110, 112, 115, 127, 131, 134, 136, 157, 161, 163, 238, 245, 268]



def generate_win_rates():
	with open('champions.json','r') as file:
		champions_data = json.load(file)
		for key in champions_data.keys():
			# create a float between 0.4 - 0.6
			win_rates[(int)(key)] = random.uniform(0.4, 0.6)
			champ_points[(int)(key)] = (int)(random.uniform(4000, 8000))

def get_lane_of_the_player():
	top_points = 0
	jug_points = 0
	bot_points = 0
	mid_points = 0
	for x in top_5_champs:
		if x[0] in TOP:
			top_points += x[1]
		elif x[0] in JUNGLE:
			jug_points += x[1]
		elif x[0] in BOTTOM:
			bot_points += x[1]
		else:
			mid_points += x[1]
	max_pints = 0
	max_points = max(top_points, jug_points, bot_points, mid_points)
	string = 'From our analysis, you are a '
	if mid_points == max_points:
		print string + "MIDDLE player!"
		return "mid"
	elif top_points == max_points:
		print string + "TOP player!"
		return "top"
	elif bot_points == max_points:
		print string + "BOTTOM player!"
		return "bot"
	elif jug_points == max_points:
		print string + "JUNGLE player!"
		return "jug"

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

def get_champion_names():
	name = open('champions.json', 'r')
	title = open('champions_title.json', 'r')
	title_data = json.load(title)
	name_data = json.load(name)
	# fill the champ_names list
	for champ in name_data.keys():
		champion_names[(int)(champ)] = name_data.get(champ)
	for champ in top_5_champs:
		top_5_champ_names.append(name_data.get(str(champ[0])))
	string = 'You are most familiar with these five champions: \n'
	for champ_name in top_5_champ_names:
		string += champ_name + ': ' + title_data.get(champ_name).get('title') + ',\n'
	string = string[:-2]
	name.close()
	title.close()
	print string +'\n'

def get_data_for_every_lane():
	for champ in win_rates.keys():
		if champ in TOP:
			top_win_rates[champ] = win_rates[champ]
		elif champ in JUNGLE:
			jug_win_rates[champ] = win_rates[champ]
		elif champ in MIDDLE:
			mid_win_rates[champ] = win_rates[champ]
		elif champ in BOTTOM:
			bot_win_rates[champ] = win_rates[champ]

def make_suggestions(lane):
	sorted_by_value = {}
	if lane == 'mid':
		sorted_by_value = OrderedDict(reversed(sorted(mid_win_rates.items(), key=lambda x: x[1])))
	elif lane == 'bot':
		sorted_by_value = OrderedDict(reversed(sorted(bot_win_rates.items(), key=lambda x: x[1])))
	elif lane == 'top':
		sorted_by_value = OrderedDict(reversed(sorted(top_win_rates.items(), key=lambda x: x[1])))
	elif lane == 'jug':
		sorted_by_value = OrderedDict(reversed(sorted(jug_win_rates.items(), key=lambda x: x[1])))

	index  = 0
	for x in sorted_by_value.keys():
		if index < 10:
			top_10_win_rate_champs[x] = sorted_by_value[x]
			index += 1
	# we have top 10 win rate champ for that lane, get three lowest champion points
	# hadoop to get the average champion points for every champ
	champ_points_of_10 = {}
	for x in top_10_win_rate_champs.keys():
		champ_points_of_10[x] = champ_points[x]
	ordered_champ_points_of_10 = OrderedDict(sorted(champ_points_of_10.items(), key=lambda x: x[1]))
	index2 = 0
	for key,value in ordered_champ_points_of_10.items():
		if index2 < 3:
			champ_selct_suggestions[key] = value
			index2 += 1
	# now we have three recommended champs
	string = 'The recommended champions for you are: \n'
	for champ in champ_selct_suggestions.keys():
		string += (str)(champion_names[champ]) + ", winrate: " + (str)((int)(win_rates[champ] * 100)) + '%\n'
	print string



if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('playerID', help='the ID of the player for suggestions')
	args = parser.parse_args()
	playerID = args.playerID
	generate_win_rates()
	get_data_for_every_lane()

	get_top_5_champs(playerID)
	get_champion_names()
	generate_win_rates
	lane = get_lane_of_the_player()
	make_suggestions(lane)