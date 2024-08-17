#formatted strings are used to dynamically add our variable values. f. strings makes our work and addition of dynamic variable values easier.
first_name=input("First Name: ")
middle_initial=input("Middle Name Initial: ")
last_name=input("Last Name: ")
semester_number=input("Semester: ")
info=f'{first_name} [{middle_initial}] {last_name} is a student of {semester_number} semester in university'
print(info)
