n=int(input("Enter number "))

fact=1
for i in range(1,n):
    fact=fact*n
    n=n-1
print(fact)