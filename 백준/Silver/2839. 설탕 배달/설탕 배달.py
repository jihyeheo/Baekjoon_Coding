n = int(input())

res = 0
while n >= 0:
    if n % 5 == 0:
        res += n//5
        break
    n -= 3
    res += 1
else:
    res = -1
print(res)