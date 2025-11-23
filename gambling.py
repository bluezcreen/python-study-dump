import random
import time

print("""
SLOT MACHINE
PRESS ANY KEY TO START
""")
input()

#slot numbers
a = random.randint(5,7)
b = random.randint(5,7)
c = random.randint(5,7)

#first num
print("*roll*")
time.sleep(2)

print(a, "X, X")

#second num
print("*roll*")
time.sleep(2)

print(a, b, "X")

#third num
print("*roll*")
time.sleep(2)
print(a, b, c)

if a and b and c == 7:
	print ("u win nigga!!!!!!")
else:
	print("u lose nigger")


