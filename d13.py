prc = int(input("yo whats ur grade"))

if prc >= 90:
	grd = ("A")
elif prc >= 80:
	grd = ("B")
elif prc >= 70:
	grd = ("C")
elif prc >= 60:
	grd = ("D")
else:
	grd = ("F")

if grd == "F":
	print("oh my god bro really")
else:
    print(f"bro got a {grd}")