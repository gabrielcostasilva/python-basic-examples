aNumber = int(input("Enter an integer number: ").strip())
anotherNumber = int(input("Enter another integer number: ").strip())

if aNumber > anotherNumber:
    print("Sorted: {}, {}".format(anotherNumber, aNumber))
else:
    print("Sorted: {}, {}".format(aNumber, anotherNumber))