import math

# This function will calculate normal seive 
# Before staring any computation
# This will calculate all the primes under a maximum 
# range which the promblem allows
def sieve(MAX):
    isPrime = [1]*MAX
    
    isPrime[0] = 0
    isPrime[1] = 0
    
    result = list()
    for i in range(2,MAX):
        if isPrime[i] == 1:
            result.append(i)
            for j in range(i*i,MAX,i):
                isPrime[j] = 0
    return result

def segmented_sieve(l,r):
    primes = sieve(100001)
    isPrime = [1] * ((r-l)+1)
    if l == 1:
        isPrime[0] = 0
    for i in range(0,int(math.sqrt(r))+1):
        currentPrime = primes[i]
        base = int(math.floor(l/currentPrime)*currentPrime)
        if base < l:
            base += currentPrime
        
        for j in range(base,r+1,currentPrime):
            isPrime[j-l] = 0

            if base == currentPrime:
                isPrime[base - l] = 1
    
    result = list()
    for i in range(0,r-l+1):
        if isPrime[i] == 1:
            result.append(i+l)
    return result

# MAin program
T = int(input())

while T:
    l,r = input().split()
    l = int(l)
    r = int(r)
    result = segmented_sieve(l,r)
    for i in result:
        print(i)
    T-=1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
    
            
            
            
            
            
            
            
            
            
            
            
            