import os, time, random
from colorama import Fore, Back, Style

def clear():
	os.system("clear")
	
def delay():
	time.sleep(1)
	
print("xitter, where israeli propaganda spreads")
 
print("create account")
usr = input("username: ")
input("password: ")
clear()
print("user successfully made, logging in...")
time.sleep(2)
clear()

#im running out of creativity rn so im sorry if this is programmed like shit

def interact(x):
	if x == "L":
		print("tweet liked")
	elif x == "R":
		print("tweet reposted")
	elif x == "C":
		input("write a reply: ")
		print("reply sent")
		delay()
		clear()
	elif x == "N":
		clear()

twts = ("""
🔵 | Trump'sNo1Cocksucker!!!
@magaluvu

charlie kirk didnt deserve to die ok.... ok...
the l*berals bro...""", """
🔵 | bullshit gimmick account☑️
@kiraalwaysmisses

would you rather be a smart fella or a fart smella👀👀""", """
🔵|basic user
@basichandle

basic tweet""")
		
def printtwt():
		global twts
		x = random.choice(twts)
		print(x)

buttons = ("""
❤️(L) 67k | 🔄(R) 41k | 🗨️(C) 1.7k
(N) next tweet >
input exit to exit""")
		
while True:
	print(f"welcome, {usr}\n".center(80))
	print(Fore.BLACK + Back.WHITE + "xitter".center(80))
	print("for you | following".center(80))
	print(Style.RESET_ALL)
	printtwt()
	print(buttons)
	
	x = input(" ").strip().upper()
	interact(x)
	if x == "exit":
		break

print("pretend like the program is ended atp")