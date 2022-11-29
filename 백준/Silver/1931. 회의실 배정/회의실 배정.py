n = int(input())

room = []
for i in range(n):
    start, end = map(int, input().split())
    room.append([start, end])
room.sort(key = lambda x:x[0])
room.sort(key = lambda x:x[1])

cnt = 1
end = room[0][1]

for i in range(1,n):
    if room[i][0]>=end:
        cnt +=1
        end = room[i][1]
print(cnt)