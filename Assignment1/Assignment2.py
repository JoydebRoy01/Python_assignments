'''2. The distance between two cities (in km.) is input through the keyboard. Write a program to
convert and print this distance in meters, feet, inches and centimeters.'''

d=int(input("Enter the distance: "))
m=d*1000
ft=m*3.28
inches=ft*12
cm=inches*2.54
print("Distance in meters:",m)
print("Distance in meters:",ft)
print("Distance in meters:",inches)
print("Distance in meters:",cm)