#fancy
#Python 6.7 demo

import sysfunc #as sx // would be more helpful but we'll be using the full module name.
#sysfunc is an essential module having all of Py6.7's functions.

class pystr: #classifies a string 
	def __init__(self, str):
		self.str = "Hello, world!" #message
		
	def echof(self): #signals Python to echo
		sysfunc.echo(self.str)

exec = True #signals mandatory loop to start
def main():
	global exec #lets loop flag in function
	while exec == True: 
	#mandatory loop running while it's True
		app = pystr(str) #defines a var for echof
		app.echof() #prints string
		exec = False #ends mandatory loop
main() #runs main code
	
	
	