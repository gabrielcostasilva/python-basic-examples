month = int(input("Enter a number from 1 to 12 representing a month: ").strip())
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

if month in range(1, 13):
    print(f"\'{months[month - 1]}\' is the month chosen!")

else:
    print("Sorry, month does not exist!")