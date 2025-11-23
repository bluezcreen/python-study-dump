#convert bad units to good units and vice versa-er
import s

while True:
	ask = input("What unit?").strip().lower()
	if ask not in ("metric", "imperial"):
		print("no")
		s.delaclear(1)