x=float(input('Enter side 1:'))
y=float(input('Enter side 2:'))
z=float(input('Enter side 3:'))
if x==y==z:
    print('Equilateral Triangle')
elif x==y or y==z or z==x:
    print('isoscales triangle:')
elif x**2+y**2==z**2 or y**2+z**2==x**2 or z**2+x**2==y**2:
    print('Righr_angel_triangle:')
else:
    print('scalene triangle')



