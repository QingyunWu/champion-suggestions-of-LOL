import json
import sys
from collections import OrderedDict
dic_list = []
with open('newPlayerId.json') as data_file:
	for line in data_file:
		player_id = json.loads(line)
		dic_list.append(player_id)
seen = OrderedDict()
for d in dic_list:
	oid = d['summonerID']
	if oid not in seen:
		seen[oid] = d
with open('player_id.json', 'w') as f:
	for x in seen.values():
		line = json.dumps(x)
		f.write("{}\n".format(line))



