import s

plane = {
	"Plane" : "F-22 'Raptor'",
	"Manufacturer" : "Lockheed Martin",
	"Description" : "A 5th gen fighter plane introduced in 2005.\n It is a jet-powered, all-weather fighter plane. \n",
	"my opinion" : None
}

def didnt_ask():
	x = ["Plane","Manufacturer","Description"]
	
	for key in x:
		if key in plane:
			print(f"{key}: {plane[key]}")
	
	plane["my opinion"] = input("what do you think of this plane: ")
	s.delaclear()
	
def did_ask():
	for name, desc in plane.items():
		print(f"{name}: {desc}")

didnt_ask()
did_ask()			