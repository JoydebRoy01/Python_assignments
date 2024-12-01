
age = int(input("Enter age: "))
health = input("Enter health condition (excellent/poor): ").lower()
location = input("Enter location (city/village): ").lower()
sex = input("Enter sex (male/female): ").lower()
if health == "excellent" and 25 <= age <= 35 and location == "city":
    if sex == "male":
        premium_rate = 4
        max_amount = 200000
        insured = True
    elif sex == "female":
        premium_rate = 3
        max_amount = 100000
        insured = True
    else:
        insured = False
elif health == "poor" and 25 <= age <= 35 and location == "village" and sex == "male":
    premium_rate = 6
    max_amount = 10000
    insured = True
else:
    insured = False

if insured:
    print("The person is insured.")
    print(f"Premium rate: Rs. {premium_rate} per thousand")
    print(f"Maximum policy amount: Rs. {max_amount}")
else:
    print("The person is not insured.")
