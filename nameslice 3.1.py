fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = input("Enter your age: ")

print()
fullname = fname + " " + lname
print("Full name: ", fullname)

slicname = fullname[0:3]
print("Sliced Name: ", slicname)

greet = "Hello, {}! Welcome. You are {} years old."
print("Greeting Message: ", greet.format(slicname, age))