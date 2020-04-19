import random
a=[]

x=int(input("Enter no. of elements"))

for i in range(1, x+1):

    a.append(random.randint(1,20))

print(a)
