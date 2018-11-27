def sum(beg,en):
    sum = 0
    for i in range(beg,en+1):
        sum += i
    print ("The sum of the consecutive integers from " + str(beg) + " to " + str(en) + " is " + str(sum))
x = int(input("For integer from a to b, enter a:"))
y = int(input("Now enter b:"))
sum(x,y)