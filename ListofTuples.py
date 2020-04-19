l_range=int(input("Enter lower range"))
u_range=int(input("Enter upper range"))

a=[(x,x*x) for x in range(l_range,u_range+1)]
print(a)