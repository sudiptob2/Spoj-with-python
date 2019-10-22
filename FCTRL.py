T = int(input())
while T:
    n = int(input())
    z = 0
    while n >= 5:
        r = int(n/5)
        z += r
        n = r
    print(z)
    T-=1
