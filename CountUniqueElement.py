arr=[1,3,3,2,4,5,6,5,6,1,2]

for i,el in enumerate(arr):
    s=arr.count(el)
    if s==1:
     print(el,"is unique element")
