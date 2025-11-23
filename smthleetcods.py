string = ("abcabcbb")

import Counter

for pointer in string[len(string)]:
	print(Counter(pointer))