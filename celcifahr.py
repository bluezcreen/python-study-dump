#fahrenheit to celcius, and vice versa
import s

def convert(x, y):
		#x = unit, y = value
		match x:
			case "celcius":
				#formula
				result = (y *9/5) + 32
				print(f"F = ({y}°C × 9/5) + 32 = {result}°C")
			
			case "fahrenheit":
				#formula
				result = (y - 32) *  5/9
				print(f"C = ({y}°F - 32) * 5/9 = {result}°F")
			
			case _:
				print("error?")
#ask
while True:
	unit_from = input("what unit to convert from?: ").strip().lower()
	
	if unit_from not in ("celcius", "fahrenheit"):
		print("invalid")
		continue
		
	value = float(input("what's the temp?: "))
	print("ok")
	s.throbber(2) 
	convert(unit_from, value)
	s.delaclear(0, True)
	
	
	

	