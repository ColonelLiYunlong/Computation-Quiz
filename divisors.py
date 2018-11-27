def triangular(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
def finddivisors(n):
    cont = 0
    for i in range(1,n+1):
        if n % i == 0:
            cont += 1
    return cont
x = int(input("Enter divisors:"))
n = 1
while (finddivisors(triangular(n)) <= x):
    n += 1
print (triangular(n))