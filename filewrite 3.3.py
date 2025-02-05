lname = input("Enter last name: ")
fname = input("Enter first name: ")
age = input("Enter age: ")
cont = input("Enter contact Number: ")
cour = input("Enter course: ")

data = "Last Name: {}\n" + "First Name: {}\n" + "Age: {}\n" + "Contact Number: {}\n" + "Course: {}\n"
filedata = data.format(lname, fname, age, cont, cour)

filename = "students.txt"

file = open(filename, 'a')
file.write(filedata)
file.close()

print("Student information has been saved to 'students.txt'. ")