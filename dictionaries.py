#Dictionaries in python are used for key value pairs
#Dictionaries are represented by {}
from datetime import datetime

customer = {
    "name": "Joseph Smith",
    "age" : 30,
    "is_verified" : True
}
print(customer)
#To get specific values
print(customer["name"])
print(customer["age"])
#we can get specific value using get method as well
print(customer.get("name"))
#To add key values in dictionary
customer["date_of_birth"] = "12 DEC 1980"
print(customer["date_of_birth"])