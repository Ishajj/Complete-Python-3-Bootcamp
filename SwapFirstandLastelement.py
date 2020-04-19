# Python Program to Swap the First and Last Value of a List

a=[]

x=int(input("Enter no. of elements"))

for i in range(0, x):
    y=int(input("Enter element: "))
    a.append(y)

temp=a[0]
a[0]=a[x-1]
a[x-1]=temp

print(a)