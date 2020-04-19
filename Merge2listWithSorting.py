a=[]
b=[]

n1=int(input("Enter number of elements:"))
for i in range(1,n1+1):
    l=int(input("Enter elements for list a"))
    a.append(l)

n2=int(input("Enter number of elements:"))
for j in range (1,n2 + 1):
    m = int ( input ( "Enter elements for list b" ) )
    b.append(m)
new=a+b
print(sorted(new))
