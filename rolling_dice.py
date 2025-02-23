import random 


while True:
    dicison = input("Want to role the dice? (y/n) ").lower()
    if dicison == 'y':
        dicison_x = random.randint(1, 6)
        dicison_y = random.randint(1, 6)
        print(f"({dicison_x}, {dicison_y})")
    elif dicison == "n":
        print("Thanks for playing")
        break
    else:
        print("Please input valid choice")
        break


    
