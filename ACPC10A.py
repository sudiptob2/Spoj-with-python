while True:
    a1,a2,a3 = map(int, input().split())
    if a1==0 and a2==0 and a3==0:
        break;
    n = 4
    
    if a2-a1 == a3-a2:
        d = a2 - a1
        a4 = a1 + (n-1) * d
        print("AP {}".format(a4))
    else:
        r = a2/a1
        a4 = a1 * r**(n-1)
        print("GP {}".format(int(a4)))
        
    