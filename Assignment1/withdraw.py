amount=int(input("Enter the Amount:"))
hundred=amount//100
fifties=(amount%100)//50
tens=(amount%100)//10
print("No of 100s:",hundred)
print("No of 50s:",fifties)
print("No of 10s:",tens)