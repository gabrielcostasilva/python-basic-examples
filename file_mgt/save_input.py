keep_going = "y"

while keep_going.startswith("y"):
    a_name = input("Enter a name: ").strip()
    
    with open("users.txt", "a") as file:
        file.write(a_name + "; ")
        
    keep_going = input("Insert another name? (y/n) ").strip()