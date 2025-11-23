import os, random, time, sys, threading, importlib
from colorama import Fore, Back, Style

#a collection of shorthands
#Update 1.1: shortened names for no reason

#terry davis
def affirmation(x=1, t=0.3):
	for i in range(x):
		print("I am the best programmer on Earth, that's why God chose me.")
		time.sleep(t)

#clear
##clears display
def c():
	os.system("clear")
clear = c
cls = c 

#delaclear
##pauses for x seconds, and clears display
##has additional parameter for input before delay
def dc(x=0, i = False, m = " "):
	if i == True:
		input(m)
		time.sleep(x)
		os.system("clear")
	else:
		time.sleep(x)
		os.system("clear")
delaclear = dc

#randint
def rint(x, y, p=False): 
	if p == True:
		print(random.randint(x,y))
	else:
		return random.randint(x,y)
r_int = rint
dice = rint

#random.sample
def rsample(x, l=1, p=False):
	if p == True:
		print(random.sample(x, k=l))
	else:
		return random.sample(x, k=l)
r_sample = rsample

#random.choice
def rchoice(x, p=False):
	if p == True:
		print(random.choice(x))
	else:
		return random.choice(x)
r_choice = rchoice

#random.choices		
def rchoices(x, y, p=False):
	if p == True:
		print(random.choices(x, k=y))
	else:
		return random.choices(x, k=y)
r_choices = rchoices

#delay
##has additional parameter to show a throbber/progressbar
def d(secs, type=None):
    if type is None:
        time.sleep(secs)
        return

    try:
        if type == "A": 
            anim = ["|", "/", "—", "\\", "-", "|", "/"]
            interval = 0.2

        elif type == "B":  
            anim = [
                "□□□□□□□□□□",
                "■□□□□□□□□□",
                "■■□□□□□□□□",
                "■■■□□□□□□□",
                "■■■■□□□□□□",
                "■■■■■□□□□□",
                "■■■■■■□□□□",
                "■■■■■■■□□□",
                "■■■■■■■■□□",
                "■■■■■■■■■□",
                "■■■■■■■■■■"
            ]
            interval = secs / len(anim)  # evenly spread
        elif type == "C": 
            anim = [
                "□□□□□□□□□□",
                "■□□□□□□□□□",
                "■■□□□□□□□□",
                "■■■□□□□□□□",
                "□■■■□□□□□□",
                "□□■■■□□□□□",
                "□□□■■■□□□□",
                "□□□□■■■□□□",
                "□□□□□■■■□□",
                "□□□□□□■■■□",
                "□□□□□□□■■■",
                "□□□□□□□□■■",
                "□□□□□□□□□■",
                "□□□□□□□□□□"]
            interval = secs / len(anim)
			
        else:
            time.sleep(secs)
            return

        for ch in anim:
            sys.stdout.write(f"\r{ch}")
            sys.stdout.flush()
            time.sleep(interval)
        print()

    except Exception as e:
        print(f"error: {e}")

throbber = d
tbr = d
delay = d

#timeout input
def timput(sprompt, eprompt=None, timeout=5):
    ans = [None]

    def ask():
        ans[0] = input(sprompt)

    t = threading.Thread(target=ask)
    t.start()
    t.join(timeout)

    if t.is_alive():  
        print(f"\n{eprompt}")
        return None
    else:
        return ans[0]

#print list
def lprint(x, e="\n"):
	for k in x:
		print(k, end=e)

#print nested list
def llprint(x, e="\n"):
	for row in x:
		for item in row:
			print(item, end=e)

#flatten nested list (doesn't work rn)			
def level(lst):
    flat = []
    for item in lst:
        if isinstance(item, list):
            flat.extend(level(item))
        else:
            flat.append(item)
    return flat
    
#print dict
def dprint(x, e="\n"):
	for key, value in x.items():
		print(f"{key} : {value}", end=e)

#print nested dict (soon) 
def ddprint(x, e="\n"):
	pass
	#soon

#new line	
def n(x=1):
	for i in range(x):
		print()
nl = n

#timer (does this even work?)
def t(secs, direction="fw", p=False):
    start = time.time()

    if direction == "fw":   # Count up
        while True:
            elapsed = int(time.time() - start)
            if p:
                print(f"\r{elapsed} (fw)", end="")
            time.sleep(1)
            if elapsed >= secs:
                return elapsed

    elif direction == "bw":   # Count down
        remaining = secs
        while remaining >= 0:
            if p:
                print(f"\r{remaining} (bw", end="")
            time.sleep(1)
            remaining -= 1
        return 0
		
#odd/even
#return even as True and odd as False
def oe(x):
	if x % 2 == 0:
		return True
	else:
		return False

#reload
def rl(x):
	try:
		importlib.reload(x)
	except Exception as e:
		print(f"error: {e}")

#typewriter effect
def typrint(text, delay=0.01): 
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()  
    
#fancy name for print
def echo(x, e="\n"):
	print(x, end=e)

