f = open("file.txt", "a")

print("highscore saver")
name = input("input 3 letter name")
hscore = input("your high score")
f.write(f"{name[0:3]} - {hscore}\n")
print("saved")
f.close()