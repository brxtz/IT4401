print("Enter the initial position in meters:")
initial_position = input()
#print(initial_position)
#print(type(initial_position))

print("Enter the initial velocity in meters/second:")
initial_velocity = input()
#print(initial_velocity)
#print(type(initial_velocity))

print("Enter the acceleration in meters/second^2:")
acceleration = input()
#print(type(acceleration))

print("Enter the time that has passed in seconds:")
time = input()
#print(type(time))

print("\nInitial position =" + " " + initial_position)
print("Initial velocity =" + " " + initial_velocity)
print("Acceleration =" + " " + acceleration)
print("Time =" + " " + time)

initial_position = float(initial_position)
initial_velocity = float(initial_velocity)
acceleration = float(acceleration)  
time = float(time)

final_position = initial_position + (initial_velocity * time) + (acceleration * time * time)/2
final_position = str(final_position)
print("Final position =" + " " + final_position)

