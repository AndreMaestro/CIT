n = int(input())
f1 = 0
f2 = 1
print(f1)
print(f2)
for i in range (3, n+1):
	f3 = f2 + f1
	f1, f2 = f2, f3
	print(f3)
