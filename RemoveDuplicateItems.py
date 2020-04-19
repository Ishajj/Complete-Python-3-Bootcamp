a=[]

x=int(input("Enter no. of elements"))

for i in range(1, x+1):
    y=int(input("Enter element"))
    a.append(y)

print(set(a))