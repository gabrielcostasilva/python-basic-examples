numberOne = int(input("Enter the first number: "))
numberTwo = int(input("Enter the second number: "))
numberThree = int(input("Enter the third number: "))

aux = 0

if numberOne > numberTwo:
    aux = numberOne
    numberOne = numberTwo
    numberTwo = aux

if numberOne > numberThree:
    aux = numberOne
    numberOne = numberThree
    numberThree = aux

if numberTwo > numberThree:
    aux = numberTwo
    numberTwo = numberThree 
    numberThree = aux

print(f"Ordered : {numberOne}, {numberTwo}, {numberThree}")