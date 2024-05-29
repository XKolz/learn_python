weight = float(input("Weight: "))
unit = input("(K)kg or (L)lbs: ")

if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in (L)lbs" + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: "+ str(converted))

# Exercise
# The formula kg ÷ 0.4536 = lb
# Weight: 170
# K(kg) or (L)lbs
# Weight in kgs:76.5


# My modified version 
# weight = float(input("Weight: "))
# unit = input("K (kg) or L (lbs): ")

# if unit.upper() == 'K':
#     converted = weight / 0.45
#     print("Weight in L: " + str(converted))
# elif unit.upper() == 'L':
#     converted = weight * 0.45
#     print("Weight in K: " + str(converted))
# else:
#     print("Invalid unit. Please enter 'K' for kilograms or 'L' for pounds.")
