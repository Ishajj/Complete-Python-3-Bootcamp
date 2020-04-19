x=int(input("Enter no. of elements"))

a=[]
b=[]
c=[]

for i in range(1,x+1):
    y=int(input("Enter number"))
    a.append(y)
for j in a:
    if(j%2==0):
        b.append(j)
    else:
        c.append(j)
print("Even list",b)
print("Odd list",c)

