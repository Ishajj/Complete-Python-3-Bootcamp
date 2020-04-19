# Python Program to Read a List of Words and Return the Length of the Longest One

a=[]
b=[]

x=int(input("Enter no. of elements"))

for i in range(0, x):
    y=input("Enter element: ")
    a.append(y)

for j,k in enumerate(a):
    b.append(len(a[j]))

print(max(b))

# Python program to read a list of words and return the word with the length of the longest one
# a=[]
# n= int(input("Enter the number of elements in list:"))
# for x in range(0,n):
#     element=input("Enter element" + str(x+1) + ":")
#     a.append(element)
# max1=len(a[0])
# temp=a[0]
# for i in a:
#     if(len(i)>max1):
#        max1=len(i)
#        temp=i
# print("The word with the longest length is:")
# print(temp)