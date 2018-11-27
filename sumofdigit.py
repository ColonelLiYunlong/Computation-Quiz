def fac(n):
    if n == 1:
        return 1
    pro = 1
    for i in range(2,n+1):
        pro *= i
    return pro
x = int(input("enter a integer:"))
def digitsum(n):
    sum = 0
    for i in (str(n)):
        sum += int(i)
    return sum
num = fac(x)
print (digitsum(num))