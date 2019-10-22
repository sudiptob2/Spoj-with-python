T = int(input())
while T:
    
    a , b = input().split()
    a = a[::-1]
    b = b[::-1]
    r = str(int(a)+int(b))
    r = r[::-1]
    print(int(r))
    T-=1