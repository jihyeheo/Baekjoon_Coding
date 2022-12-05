while True:
    a,b,c = map(int,input().split())
    list1 = [a,b,c]
    first = max(list1)
    third = min(list1)
    list1.remove(first)
    list1.remove(third)
    second = list1[0]
    if a ==0 and b ==0 and c == 0:
        break
    else:
        if (third**2)+(second**2) == (first**2):
            print("right")
        else:
            print("wrong")