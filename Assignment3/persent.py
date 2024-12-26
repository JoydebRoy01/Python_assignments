#A machine is purchased which will produce earning of Rs. 1000 per year while it lasts. The
#machine costs Rs. 6000 and will have a salvage of Rs. 2000 when it is condemned. If 12 percent
#per annum can be earned on alternate investments what would be the minimum life of the
#machine to make it a more attractive investment compared to alternative investment?
n= int(input("Enter number of years"))
machine=6000
salvage=2000
bank=6000
machine_carring=0
bank_carring=0
machine_total=0
for year in range(1,n+1):
    machine_carring+=1000
    bank_carring+=720
    machine_total=machine_carring+salvage
    if(machine_total>bank_carring+bank):
        print(f"The machine become more profitable after {year}year")
        print('machine value:f{bank+bank_carring}')
        break

    else:
        print("The machine become does not more profitable with in the given time:")