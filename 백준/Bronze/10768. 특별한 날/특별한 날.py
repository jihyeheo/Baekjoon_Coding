months = int(input())
days = int(input())




if months < 2:
    print("Before")
elif months == 2:
    if days < 18:
        print("Before")
    elif days == 18 :
        print("Special")
    else :
        print("After")
else:
    print("After")