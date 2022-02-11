import math

print("Welcome to the Paint Job Estimator!\n")
print("-----------------------------------")

do_estimate = True
while(do_estimate):
    while(True):
        try:
            square_ft = int(input("\nHow many square feet of wall would you like to be painted?\n"))
            if(square_ft <= 0):
                print("Only positive values allowed. Please enter a valid value.\n")
                continue
        except:
            print("The value you entered is invalid. Only numerical values are valid.\n")
        else:
            break

    while(True):
        try:
            cost = float(input("What is the price of the paint per gallon?\n"))
            if(cost <= 0):
                print("You entered a invalid cost for the paint. Please enter a valid value.\n")
                continue
        except:
            print("The value you entered is invalid.\n")
        else:
            break


    gallons = math.ceil(square_ft / 350)
    #if it takes 6h to finish painting 350 quare feet of wall space, then it takes 1h to paint 58.33 square feet of wall space 
    time = square_ft / 58.33
    paint_cost = cost * gallons
    labor = 69.25 * time
    total = labor + cost

    print("\nThe number of gallons of paint required is %d" % gallons)
    print("The hours of labor needed to finish the job will be %.1f hours" % time)
    print("The cost of the paint will be $%.2f" % paint_cost)
    print("The labor charges will be $%.2f" % labor)
    print("The cost of the job will be $%.2f\n" % total)

    another_estimate = str(input("Would you like to get another estimate? (y/n): "))
    if(another_estimate != "y"):
        do_estimate = False
