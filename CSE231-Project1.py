##############################
#    Computer Project #1
#    This assignment is for the conversion of a unit,
#    "rods" to basic units. This project is also to 
#    learn the basic python algorithms.
##############################

num_str = input("Input rods: ")
num_float = float(num_str)

meters = num_float*5.0292
feet = meters/0.3048
miles = meters/1609.34
furlongs = num_float*0.025
walking_time = (60*miles)/3.1


print("You input",num_float,"rods.")
print()
print("Conversions")
print("Meters:",round(meters, 3))
print("Feet:",round(feet, 3))
print("Miles:",round(miles, 3))
print("Furlongs:",round(furlongs, 3))
print("Minutes to walk", num_float, "rods:", round(walking_time, 3))
