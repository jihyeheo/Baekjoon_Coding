n = int(input())

list1 = []
for _ in range(n):
    a,b = map(int, input().split())
    list1.append([a,b])
    
for i in sorted(list1):
    print(i[0], i[1])