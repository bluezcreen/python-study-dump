'''
py-dos / fake tui thing

directories

root

>programs
>>calculator
>>dice
>>clock

>docs
>>helloworld.txt (not a real .txt)

>games
>>roulette (import from gambling.py)
'''
import s
import os, textwrap
from colorama import Fore, Back, Style

	
dir = {
"root" : {
"programs	<DIR>" :
	{"calculator	<EXE>",
	"dice	<EXE"},

"docs	<DIR>" : 
	{"helloworld	<TXT>" : "hi!"},

"games	<DIR>" :
	"roulette	<EXE>",

#layered folder test
"folder	<DIR>" :
	{"folder1	<DIR>":
		{"folder2	<DIR>" : "thing	<???>"}}
}}

current_dir = dir["root"]

#name of current dir
name_dir = ("SOMETHING IDK")

def loading():
	s.d(4, "A")
	s.dc()
	
def setup():
	title = (textwrap.dedent("""PY-DOS 6.7 SETUP
================="""))
	finish = False	
	while finish == False:
		loading()
		print(title)
		print(textwrap.dedent("""
Welcome to the setup for PY-DOS 6.7.
Please select a directory to install PY-DOS in:
╔═══════════╗
║▸ C drive    ║
╚═══════════╝

You may need to read the manual that comes with the packaging for PY-DOS 6.7.
It describes the complete guide to installing and using PY-DOS efficiently.

To continue Setup, press any key.


==================
ANY KEY = Continue
"""))
		skip = input()
		if skip == "skip":
			print("Setup skipped for technical reasons (debugging)")
			s.dc(1)
			break
			
		loading()
		
		#insert disks (virtually unnecesary)
		for i in range(1, 6):
			print(title)
			print(textwrap.dedent(f"""
			Please insert Disk {i} in the disk drive.
			╔════╗
			║▋▐██║╔═══════════╗
			║██▣█║║ Discs {i}/6  ║
			║████║╚═══════════╝
			╚════╝"""))
			input()
			print(f"Moving items from Disk {i} to C partition...")
			s.d(8, "B")
			loading()
			s.dc()
		
		print(textwrap.dedent("""
		PY-DOS 6.7 SETUP
		================
		Setup for PY-DOS 6.7 is finished and is ready to be ran. Enjoy the luxurious experience of Divine Intellects Corp.'s technology.
		
		
		================
		ANY KEY = Continue"""))
		input()
		s.dc()
		break
		
def cmd(x):
	global dir
	#cmdprompt commands 
	#cd [dir]
	#dir
	#clear
	#rmdir
	#shutdown
	#to run a program match w program name
	#god this code will be awful so brace yourself
	for p in current_dir:
				print(p)
				
	match x:
		case "cd":
			input("")
		case "dir":
			print(f"Directories of {name_dir}: ")
		
		case _:
				print(f"No command named {x}")
				
def main():
	s.typrint("PY-DOS 6.7 © Divine Intellects Corp, 2018")
	s.d(0.5)
	s.typrint("cLang is testing code...")
	s.d(1)
	s.typrint("Done.\n")
	while True:
		inp = input(f"C:\\>{name_dir}")
		cmd(inp)

main()
