#we can store items in tuples, like lists
#But we cannot modify them
#Tuples are immutable
number=(1,2,3)
#number[0]=10     this line is an error
print(number)
#Un-Packing feature of tuples
x=number[0]
print(x)
#This below line assigns every single value to every single variable
x, y, z = number
print(x,y,z)