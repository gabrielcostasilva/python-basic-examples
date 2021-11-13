yourFullName = input("Enter your name followed by your surname (full name): ").strip()
name, surname = yourFullName.split(" ")
print("Your name is \'{}\', and your surname is \'{}\'".format(name, surname))