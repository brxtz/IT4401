print("This program calculates the final position of an object\n")

do_calculation = True
while(do_calculation):
    #get necessary information
    while(True):
        try: 
            initial_position = float(input("Enter the initial position in meters: "))
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else: 
            break

    while(True):
        try:
            initial_velocity = float(input("Enter the initial velocity in meters/second: "))
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else: 
            break

    while(True):
        try:
            acceleration = float(input("Enter the acceleration in meters/second^2: "))
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else: 
            break

    while(True):
        try:
            time = float(input("Enter the time that has passed in seconds: "))
            if(time < 0):
                print("Negative elapsed times are not allowed.")
                continue
        except ValueError:
            print("The value you entered is invalid. Only numerical values are valid.")
        else: 
            break

    #check the values entered 
    print("\nInitial position =" + " " + str(initial_position))
    print("Initial velocity =" + " " + str(initial_velocity))
    print("Acceleration =" + " " + str(acceleration))
    print("Time =" + " " + str(time))
    print("\n")

    #calculate the final position
    final_position = initial_position + (initial_velocity * time) + (acceleration * time * time)/2

    #output final position
    print("Final position =" + " " + str(final_position))
    print("\n")

    another_calculation = input("Do you want to perform another calculation?(y/n): ")
    if(another_calculation != "y"):
        do_calculation = False
