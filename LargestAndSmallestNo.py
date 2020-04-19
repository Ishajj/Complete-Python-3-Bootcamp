# Program to print the largest even and largest odd number in a list

a=[]
b=[]
c=[]

x=int(input("Enter no. of elements"))

for i in range(0, x):
    y=int(input("Enter element: "))
    a.append(y)

for j in a:
    if(j%2==0):
        b.append(j)
    else:
        c.append(j)

print(max(b))
print(max(c))
