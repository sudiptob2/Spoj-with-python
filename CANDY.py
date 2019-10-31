while True:
    
    n = int(input())
    if n == -1:
        break;
    sum = 0
    c = list()
    for i in range(n):
        c.append(int(input()))
        sum += c[i]
        
    
    if sum % n == 0:
        avg = int(sum/n)
        move = 0
        for i in c:
            if i > avg:
                move += (i-avg)              
        print(move)
    else:
        print(-1)
                
        