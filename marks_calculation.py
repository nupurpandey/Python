x=raw_input ("enter your name:" )
print("enter your marks:" )
first=int(input("enter marks scored in english:" ))
second=int(input("enter marks scored in Maths:" ))
third=int(input("enter marks scored in Biology:" ))
fourth=int(input("enter marks scored in Physics:" ))
fifth=int(input("enter marks scored in chemistry:" ))
sum=first+second+third+fourth+fifth
print("marks scored = ", sum )
average=sum/5
percentage=sum*100/500
print("average marks = ", average )
print("percentage scored = ", percentage )
if (percentage>=90) :
 print ("congratulations you hold first position:" )
elif (percentage>=33 and percentage<=90) :
  print ("you have passed the exam:" )
else:
 print ("sorry but failed the exam:" )
 print("enter x to exit")
