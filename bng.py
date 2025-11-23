#british town name generator 
from random import *

pref = ["Abbey", "Abber", "Bruns", "Bos", "Bick",
        "Bas", "Cas", "Clam", "Dam", "Doherty", "Dale", "Es", 
        "Fun", "Fee", "Far", "Golly", "Hamp", "Hick",
        "Holler", "In", "Jam", "Jolly", "Ken", "Key", "Lane",
        "Lot", "Lon", "Mc", "Mas", "Not", "Nor", "Pen",
        "Quins", "Queen", "Rains", "Rotter", "Sam", "Soot",
        "Tam", "Tack", "Tim", "Wen", "Well"]
        
suff = ["alley", "all", "and", "burg", "been", "dun",
        "ford", "gall", "hill", "hall", "in",
        "jot", "lamp", "mouth", "ober", "pass", "pink",
        "shire", "sall", "ton", "till", "worth", "wuns",
        "while", "wick", "won"]
        
for i in range(100):
	upon = choice([True, False])
	name = None
	
	presuf = choice(pref) + choice(suff)
	presuf2 = choice(pref) + choice(suff)
	if upon:
		name = presuf + " upon " + presuf2
	else:
		name = presuf
		
	print(name)