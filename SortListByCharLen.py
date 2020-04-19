x=int(input("Enter total no. of elements"))

a=[]
temp = None

for i in range(1,x+1):
    y=input("Enter string")
    a.append(y)
for m,j in enumerate(a):
    for k in range(0,x-m-1):
        if len(a[k])>len(a[k+1]):
            temp=a[k]
            a[k]=a[k+1]
            a[k+1]=temp
print(a)

# a=[]
# n=int(input("Enter number of elements:"))
# for i in range(1,n+1):
#     b=input("Enter element:")
#     a.append(b)
# a.sort(key=len)
# print(a)


