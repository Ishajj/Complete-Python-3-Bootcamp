#Inverted rows of star pattern
#https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/
n=int(input("Enter number of rows: "))
# for i in range (n,0,-1):
#     print((n-i) * ' ' + i * '*')

for i in range(1,n+1):
    print(i *'*')

for i in range(1,n+1):
    print(i *'*')
