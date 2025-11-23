name = ("John Doe")
pw = ("password")
nvalid = False
pvalid = False
success = False

def AccCheck(x, y):
	global nvalid, pvalid
	if x == name:
		nvalid = True
	if y == pw:
		pvalid = True

def UserCheck():
	global success
	if AccCheck(False,:
		print("Username and password is wrong/doesn't exist")
		success = False
		nvalid = False
		pvalid = False
		
	elif nvalid == True and pvalid == False:
		print("Password is incorrect")
		success = False
		nvalid = False
		pvalid = False
		
	elif nvalid == False and pvalid == True:
		print("Username is incorrect or doesn't exist")
		success = False
		nvalid = False
		pvalid = False
		
	else:
		print("Welcome")
		success = True

while success == False:
	print("login")
	a = input("Username: ")
	b = input("Password: ")
	AccCheck(a, b)
	UserCheck()
