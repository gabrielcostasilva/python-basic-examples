even_number = lambda a : a % 2 == 0
odd_number = lambda a : not even_number(a)
divible_by3 = lambda a : a % 3 == 0

loop = "y"
while loop == "y":
    number = int(input("Enter a number: ").strip())
    print(f"The number '{number}' is even: '{even_number(number)}'")
    print(f"The number '{number}' is odd: '{odd_number(number)}'")
    print(f"The number '{number}' is divisible by 3: '{divible_by3(number)}'")

    loop = input("Try again? (y/n) ").strip().lower()
    