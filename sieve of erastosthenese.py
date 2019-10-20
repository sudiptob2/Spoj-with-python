n = int(input("Entr upper bound: "))
primes = [1]*(n+1)

primes[0] = 0
primes[1] = 0

for i in range(2,n):
    if primes[i] == 1:
        print(i)
        for j in range(i*i,n,i):
            primes[j] = 0
