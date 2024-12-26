base = int(input("Enter the Base Number :"))
pow = int(input("Enter the Power Number :"))
res = 1
while pow != 0:
    res *= base
    pow-=1
 
print("Answer :",res)