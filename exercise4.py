name=input("Enter your name ")
name_length=len(name)
if name_length<3:
    print("Name should be minimum 3 characters long")
elif name_length>50:
    print("Name should be maximum of 50 character long")
else:
    print("Name looks good!")