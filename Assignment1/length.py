'''5. The length & breadth of a rectangle and radius of a circle are input through the keyboard.
Write a program to calculate the area & perimeter of the rectangle, and the area &
circumference of the circle.'''

len=int(input("Enter Length of Rectangle :"))
bre=int(input("Enter Breath of Rectangle :"))
re=len*bre
print("Area of Rectangle is : ",re)
per=2*(len+bre)
print("Perimeter of Rectangle is : ",per)
r=int(input("Enter  Radius of Circle :"))
cir=2*3.14*r
cirl=3.14*r**2
print("Area is :",cirl)


