#demo
import s
from colorama import Fore, Back, Style

def stupiddemo():
	thing = ("welcome 2 simplemodule 1.1 demo")
	print(Fore.BLACK + Back.WHITE)
	print(f"{thing}".center(59))
	
	list = ["a", "b", "c", "d", "e"]
	nlist = [["a", "b", "c", "d", "e"], ["f", "g", "h", "i", "j"]]
	dictionary = {"k" : "1", "l" : "2", "m" : "3", "n" : "4", "o" : "5"}
	

	print(Style.RESET_ALL)
	
	while True:
		test = int(input("""
			features to test:
			1. random.x() shorthands
			2. throbber
			3. print shortcuts
			4. misc\n"""))
		
		if test == 1:
			print("rint(x, y, p=False)")
			print("also callable by dice()")
			s.rint(1,10, True)
			s.n()
			print("rsample(x, y=1, p=False")
			s.rsample(list, 5, True)
			s.n()
			print("rchoice(x, p=False)")
			s.rchoice(list, True)
			s.n()
			print("rchoices(x, y, p=False)")
			s.rchoices(list, 5, True)
			s.dc(3)
			continue
		
		elif test == 2:
			print("d(sec, type=None)")
			
			s.d(3, "A")
			s.n(3)
			s.d(3, "B")
			s.n(3)
			s.d(3, "C")
			
			s.dc(3)
			continue
		
		elif test == 3:
			print("lprint(x,e)")
			s.lprint(list, "\nsimple!\n")
			n()
			s.print("llprint(x, e)")
			llprint(nlist, "\nsimple!\n")
			s.n()
			print("dprint(x, e)")
			s.dprint(dictionary, "\nsimple!\n")
			print("level(lst)")
			bonk = s.level(nlist)
			print(bonk)
			s.dc(0, True)
			continue
			
		elif test == 4:
			print("t(secs, direction='fw', p=False)")
			s.t(5, "fw", True)
			s.t(5, "bw", True)
			n()
			print("timput(sprompt, eprompt, timeout=5")
			s.timput("3s for timeout input", "Too late!", 3)
			s.delaclear(5)
			s.n()
			continue
			
		else:
			print("what?")
			continue
			
stupiddemo()