a=[]
b=[]

x=int(input("enter total no. of elements for list a"))

for i in range(1,x+1):
    k=int(input("Enter element"))
    a.append(k)

y=int(input("enter total no. of elements for list b"))
for j in range ( 1, y + 1 ):
    l = int ( input ( "Enter element" ) )
    b.append( l )

print(list(set(a)&set(b)))



