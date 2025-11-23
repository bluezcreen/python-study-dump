import s

print("dingo card")

d = [
[None, None, None],
[None, None, None],
[None, None, None]]

#insert random thing
for r in range(0, 3):
	for c in range(0,3):
		d[r][c] = s.r_int(1,50)
	
#certified [DINGO] stamp
d[1][1] = ("DINGO")

print(f"""
{d[0][0]} | {d[0][1]:^5} | {d[0][2]}
================
{d[1][0]} | {d[1][1]} | {d[1][2]}
================
{d[2][0]} | {d[2][1]:^5} | {d[2][2]}
""")
	


				