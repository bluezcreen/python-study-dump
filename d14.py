import time

counter = 0
exit = " "
print("this counter will count from 1 to 10 and back")
while counter < 10 and exit != "Yes" :
	time.sleep(1)
	counter += 1
	print(counter)
	if counter == 10:
		exit = input("do u want to count back or not? ion fucking know how to connect 2 loops so youll have to type Yes in yourself")
print("yeah fuck no code this yourself dumbass")
	