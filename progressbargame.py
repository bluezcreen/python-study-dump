import random
import s
from colorama import Fore, Back, Style

seg = [
    Fore.BLACK + Back.CYAN + "√" + Style.RESET_ALL,
    Fore.BLACK + Back.YELLOW + "X" + Style.RESET_ALL,
    Fore.BLACK + Back.MAGENTA + "-" + Style.RESET_ALL,
    Fore.WHITE + Back.RED + "@" + Style.RESET_ALL,
    Fore.BLACK + Back.GREEN + "%" + Style.RESET_ALL,
]
rarity = [0.3, 0.2, 0.1, 0.3, 0.1]

catch = []
progressbar = []

def randseg():
    choices = random.choices(seg, weights=rarity, k=3)
    catch[:] = choices
    for i, k in enumerate(choices, 1):
        print(i, k, end="   ")
    print("\n")

def printbar():
    print("\nProgress:")
    for k in progressbar:
        print(k, end="")
    print(f"\n{len(progressbar)*10}%\n")

def segsys(index):
    """Apply effect of chosen segment. Return 'ok'|'fail'|'win'."""
    sym = catch[index]
    # minus
    if sym == seg[2]:
        if progressbar:
            progressbar.pop()
        return "ok"
    # error -> immediate fail
    if sym == seg[3]:
        for i in range(len(progressbar)):
        	progressbar[i] = (Fore.WHITE + Back.RED + "Error!").center(10)
        return "fail"
    # instawin
    if sym == seg[4]:
        # fill to 10
        needed = 10 - len(progressbar)
        if needed > 0:
            progressbar.extend([seg[0]] * needed)
        return "win"
    # normal segments (√ or X) -> append
    progressbar.append(sym)
    if len(progressbar) >= 10:
        return "win"
    return "ok"

def main():
    while True:
        randtime = s.r_int(2, 4)
        randseg()
        # use s.timput(prompt, timeout) — not extra args
        dec = s.timput("catch one! ", randtime)
        if dec is None:
            print("You didn't pick in time...")
            s.delaclear(1)
            continue
        try:
            i = int(dec) - 1
        except ValueError:
            print("Not a number!")
            continue
        if i < 0 or i >= len(catch):
            print("Invalid choice!")
            continue

        status = segsys(i)
        printbar()
        s.delaclear(1)

        if status == "fail":
            ans = input(
                "An error occurred. Input 1 to retry the round, anything else to quit: "
            ).strip()
            if ans == "1":
                continue
            else:
                print("Game over.")
                break

        if status == "win":
            print("You win!")
            break

main()