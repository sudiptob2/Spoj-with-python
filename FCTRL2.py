t = int(input())

while t:
    
    n = int(input())
    fact = 1
    for i in range(1,(n+1)):
        fact*= i
    print(fact)
    
    t-=1