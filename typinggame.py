#typing game
import s, time

def accuracy():
	correct = 0
	for i in range(min(len(original), len(typed))):
	    if typed[i] == original[i]:
	        correct += 1
	
	accuracy = correct / len(original) * 100
	print(f"Accuracy: {accuracy:.2f}%")
	
def main():
	while True:
		text = ("The quick brown fox jumps over the lazy dog.")
		print("typing game!!!")
		print(f"sample text:{text}\n")
		input("Input to start...")
		s.t(999, "fw", True)
		typed = input("Type here\n")
		