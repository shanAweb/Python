weight=input("Enter your weight: ")
weight_type=input("(L)bs or (K)g: ")
if weight_type.upper()=="L":
    converted_weight=float(weight) * 0.45
    print(f"Weight is: {converted_weight}KG")
elif weight_type.upper()=="K":
    converted_weight=float(weight) / 0.45
    print(f"Weight is: {converted_weight}lbs")
else:
    print("Please enter valid weight type")
