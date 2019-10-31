#1x1 - 1^2 = 1
#2x2 - 2^2 + 1^2 = 5.
#3x3 - 3^2 + 2^2 + 1^2 = 14.
#4x4 - 4^2 + 3^2 + 2^2 + 1^2 = 30.
#5x5 - 5^2 + 4^2 + 3^2 + 2^2 + 1^1 = 55.
# So this is nothing but sum of square untill N

# n(n+1)(2n+1)/6

while True:
    n = int(input())
    if n == 0:
        break
    r =  int(n*(n+1)*(2*n+1)/6)
    print(r)