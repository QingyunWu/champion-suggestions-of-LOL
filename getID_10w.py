import json
f = open('player_id.json', 'r')
newFile = open('player_ID_10w.txt', 'w')

for x in range(100000):
	line = json.loads(f.readline()).get('summonerID')
	newFile.write(str(line) + '\n')
f.close()
newFile.close()



