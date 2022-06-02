def getsum(n):
    sum=o
    for digit in str(n):
        sum+=int(digit)
    return sum
n=12345
print(getsum(n))        