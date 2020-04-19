n=int(input("Enter a number:")) #231
tot=0
while(n>0): #231>0
    dig=n%10 #dig=231%10 4321%10=321
    tot=tot+dig #tot=0+31
    n=n//10 #231/10=2.31
print("The total sum of digits is:",tot)