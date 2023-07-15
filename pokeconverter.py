import json
import requests
import pprint
import random


response = requests.get("https://play.pkmn.cc/data/random/gen9randombattle.json")
mons = json.loads(response.text) #dict

#json.dumps(mons, indent=4)

#mons = response.json()

# print(type(mons))
#print(mons)

# pprint.pprint(mons)
#print(len(mons))


with open('names.txt') as namefile:
    names = [line.rstrip() for line in namefile] #list
namefile.close()

#print(names)

#print(len(names))

rannums = random.sample(range(1, len(mons)), len(names)*6) #list

#print(rannums)

teamfile = open('teams.txt', 'w')
for x in range(len(names)):
	teamfile.write(names[x]+"\n")
	

with open('data.json', 'w') as f:
    json.dump(mons, f, indent=4)
f.close();