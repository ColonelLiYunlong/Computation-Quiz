def isitprime(n):
    res = True
    if n == 2:
        return True
    for i in range(2,n):
        if n % i == 0:
            res = False
    return res
def nthprime(n):
    if n == 1:
        return 2
    i = 1
    prime = 3
    while (i <= n):
        if isitprime(prime):
            i += 1
            if i == n:
                return prime
        prime += 2
        
x = int(input("input nth prime:"))
print (nthprime(x))