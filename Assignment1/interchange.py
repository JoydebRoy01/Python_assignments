'''Two numbers are input through the keyboard into two locations C and D. Write a program to
interchange the contents of C and D.'''
c=int(input("Enter the number c:"))
d=int(input("Enter the Number d:"))
e=c
c=d
d=e
print("The value of c is : ",c)
print("The value of d is : ",d)