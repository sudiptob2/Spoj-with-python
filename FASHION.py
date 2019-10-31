t = int(input())

while t:
    t -= 1
    n = int(input())
    m = [int(x) for x in input().split()]
    w = [int(x) for x in input().split()]
    m.sort()
    w.sort()
    sum = 0
    for i in range(n):
        sum += (m[i]*w[i])
    
    print(sum)
    
    
    
    