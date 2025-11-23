import random

print("""
CURSE CREATOR
CLICK BUTTON TO START
""")
input()

#curse-o-list

good = ["become a billionaire", "have superpowers", "gain 200 IQ"]
bad = ["never drink anything other than water again", "you need to stub your toe to use it", "there is a 10% chance you kill a random person on Earth"]

pickg = random.choice(good)
pickb = random.choice(bad)

#question

print("Would you", pickg, ", but you", pickb, "?")
yesno = input("Y/N")

if yesno == "Y" :
	print("What a masochist.")
elif yesno == "N" :
	print("It doesn't seem like you like taking risks")
else:
	print("I understand. Sometimes decisions are difficult to make")
