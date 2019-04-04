#!/usr/bin/python

import sys

print("Please select operations:")
print(" 1. Area     ")
print(" 2. Perimeter   ")
choice=input("enter choice(1/2):")
if choice == 1:
    print("select plane figures:")
    print("1.square")
    print("2.rectangle")
    print("3.circle")
    print("4.trapezium")
    print("5.parallelogram")
choice=input("enter choice(1/2/3/4/5):")
if choice == 1:
   l=float(input("enter the Side Lengt:"))
   area=l**2
   print("area of square:" ,area)
elif choice == 2:
    l=float(input("enter the length:"))
    b=int(input("enter the breadth:"))
    area=l*b
    print("area of rectangle:" ,area)
elif choice == 3:
   r=float(input("enter the radius:"))
   from math import pi
   area=pi*(r**2)
   print("area of circle:" , area)
elif choice == 4:
   a=float(input("enter the base1:"))
   b=float(input("enter the base2:"))
   h=float(input("enter the height:"))
   area=((a+b)/2)*h
   print("area of trapezium:" , area)
elif choice == 5:
   b=float(input("enter the base:"))
   h=float(input("enter the height:"))
   area=b*h
   print("area of paralleogram:" ,area)
else:
   print ("Wrong Choice")
   sys.exit()

if choice == 2:
       print("select plane figures:")
       print("1.square")
       print("2.rectangle")
       print("3.circle")
       print("4.trapezium")
       print("5.parallelogram")
choice=input("enter choice(1/2/3/4/5):")
if choice== 1:
      l=float(input("enter the length:"))
      perimeter=4*l
      print("perimeter of square:" ,perimeter)
elif choice == 2:
      l=float(input("enter the length:"))
      b=float(input("enter the breadth:"))
      perimeter=2*(l+b)
      print("perimeter of rectangle:" ,perimeter)
elif choice == 3:
      r=float(input("enter the radius:"))
      from math import pi
      circumference=2*pi*r
      print("circumference of circle:" ,circumference)
elif choice == 4:
      a=float(input("enter the base1:"))
      b=float(input("enter the base2:"))
      c=float(input("enter the side1:"))
      d=float(input("enter the side2:"))
      perimeter=a+b+c+d
      print("perimeter of trapezium:" ,perimeter)
elif choice == 5:
      a=float(input("enter the base:"))
      b=float(input("enter the side:"))
      perimeter=2*(a+b)
      print("perimeter of parallelogram:" ,perimeter)
   
else:
     print("invalid output")

