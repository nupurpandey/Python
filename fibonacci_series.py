a=0
b=1
upper=int(input("enter the upper limit:"))
for x in range(0,upper):
     if(x == a + b):
       a = b
       b = x
