#Conditional statement
temperature = 15
if temperature >30:
    print ("It's warm")
    print ("Drink water")
elif temperature >20:
    print ("It's nice")
else:
    print ("It's cold")

#Logical operator
high_income = True
good_credit = False
if high_income or good_credit: 
    print("Eligible")
else:
    print("Not eligible")

#for loop
for number in range(3):
    print("Attempt", number)

#nested loop
for x in range(3):
    for y in range(2):
        print(f"({x}, {y})")