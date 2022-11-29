n = int(input())

list1 = []
for _ in range(n):
	list1.append(int(input()))
list1 = sorted(list1)

for i in list1:
	print(i)