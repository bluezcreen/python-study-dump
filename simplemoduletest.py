import s
from colorama import Fore, Back, Style
print("SimpleModule 1.0 demo")
print(Fore.BLACK + Back.WHITE + """
to use: import s

current functions:
clear() - short for os.system("clear")

delay(x) - short for time.sleep

delaclear(x, i = False, m = none) - delays x seconds and clears terminal, has a flag to add input() or not
optional message for input() is also available 

r_int(x, y, p=False) - basically random.randint, has a flag to print() or not

r_sample(x, l=1, p= False) - basically random.sample\n has a print flag too \n

r_choice(x, p=False)
r_choices(x, y, p=False)
it's random.choice/s you get the point

throbber(secs)
cool loading thing, also works as a s.delay()""")
print(Style.RESET_ALL)

list = ["a", "b", "c", "d", "e"]
s.r_int(0,10, True)
s.r_sample(list, 1, True)
s.r_choice(list, True)
s.r_choices(list, 5, True)

s.throbber(3)

s.delaclear(1, True, "input to clear")

input("here's a more manual delay and input test to test both clear() and delay(x)")
s.delay(5)
s.clear()
