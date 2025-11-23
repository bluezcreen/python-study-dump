import os
	
Mainl = [ ]
	
class Str:
	def __init__(self, str):
		self.str = str
		
	def __str__(self):
		return self.str
			
x = Str("こんにちは、世界！")
Mainl.append(x)
	
Tempbool = True
def main():
	global Tempbool
	while Tempbool != False:
		for Print in Mainl:
			print(Print)
		return 0
		break
	return 0
	
main()
