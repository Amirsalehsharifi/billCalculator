print("Welcome to tip calculator.")
total_bill=float(input("What was the total bill? $"))
tip_percentage=float(input("What percentage tip would yo like to give?"))/100
num_people_split=int(input("How many people to split the bill?"))
total_pay= total_bill + (total_bill*tip_percentage)
each_person_pay=total_pay/num_people_split
round_to_show ="{:.2f}".format(each_person_pay)
print(f"Each person should pay: {round_to_show}$")
