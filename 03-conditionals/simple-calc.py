aNumber = int(input("Enter an integer: ").strip())
anotherNumber = int(input("Enter another integer: ").strip())
op = input("Pick an operation (+, -, *, /): ").strip()

if op not in ["+", "-", "*", "/"]:
    print("I'm afraid, the operation you chose is invalid!")
else:
    if op in "+":
        print("{} + {} = {}".format(aNumber, anotherNumber, aNumber + anotherNumber))
    elif op in "-":
        print("{} - {} = {}".format(aNumber, anotherNumber, aNumber - anotherNumber))
    elif op in "*":
        print("{} * {} = {}".format(aNumber, anotherNumber, aNumber * anotherNumber))
    else:
        print("{} / {} = {}".format(aNumber, anotherNumber, aNumber / anotherNumber))
    