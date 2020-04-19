l_range=int(input("Enter lower range"))
u_range=int(input("Enter upper range"))
a=[]
a=[x for x in range(l_range,u_range+1) if (int(x**0.5))**2==x and sum(list(map(int,str(x))))<10]
print(a)
#https://www.sanfoundry.com/python-problems-solutions/