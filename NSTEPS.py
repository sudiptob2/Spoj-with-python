t = int(input())

while t:
    x,y = input().split()
    x = int(x)
    y = int(y)
    
    if x == y and x%2 == 0:
        print(x+y)
    elif x == y:
        print(x+y-1)
    elif x - y == 2:
        if x%2!=0:
            print(x+y-1)
        else:
            print(x+y)
    else:
        print("No Number")
    t-=1