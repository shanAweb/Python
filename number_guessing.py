import random

random_number = random.randint(1, 100)
while True:
    choice = int(input("Enter number: "))
    if choice >= 1 and choice <= 100:
        if choice < random_number:
            print("Your choice is low")
        elif choice > random_number:
            print("Your choice is high")
        else:
            print("Congratulations!!!, you have guessed the right number")
            break
    else:
        print("Enter valid choice")

