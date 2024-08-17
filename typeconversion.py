#type conversion = changing the type of variable like from int to float and so on.
#let's understand type conversion by making and age calculator
#Background: input function in python always returns "str"
birth_year = input("Birth Year: ")
age = 2024 - int(birth_year)
print("Age is: " + str(age))
#type conversion of age from int to str is because + concatenate str only
#To check type of variable in python
print(type(birth_year))