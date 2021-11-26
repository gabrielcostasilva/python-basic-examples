firstNumber = int(input("Enter the first number: ").strip())
secondNumber = int(input("Enter the second number: ").strip())
thirdNumber = int(input("Enter the third number: ").strip())

if firstNumber > secondNumber and firstNumber > thirdNumber:
    print("The first number ({}) is the greatest!".format(firstNumber))

elif secondNumber > firstNumber and secondNumber > thirdNumber:
    print("The second number ({}) is the greatest!".format(secondNumber))

else:
    print("The third number ({}) is the greatest!".format(thirdNumber))