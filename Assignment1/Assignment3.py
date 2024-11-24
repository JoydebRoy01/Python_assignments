'''3. If the marks obtained by a student in five different subjects are input through the keyboard,
find out the aggregate marks and percentage marks obtained by the student. Assume that the
maximum marks that can be obtained by a student in each subject is 100.'''
mar1=int(input("Enter marks in bengli :"))
mar2=int(input("Enter marks in English :"))
mar3=int(input("Enter marks in math :"))
mar4=int(input("Enter marks in phic :"))
mar5=int(input("Enter marks in cam :"))
sum=mar1+mar2+mar3+mar4+mar5
ave=(sum/500)*100
print("Sum of all subject :",sum)
print("Sum of all subject everage :",ave)