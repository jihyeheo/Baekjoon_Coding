a,b,v =map(int, input().split())
num = 0 
def solve(a,b,v):
    last = (v - a + (a-b)) % (a-b)
    day = (v - a + (a-b)) / (a-b)
    if last == 0:
        return day
    else:
        return day+1
        
        
    return x
print(int(solve(a,b,v)))