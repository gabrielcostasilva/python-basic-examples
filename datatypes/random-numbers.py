import random

n1 = int(input("Pick any integer number: "))
n2 = int(input("Pick any integer number GREATER than the first: "))

print("Here it goes your random number!")
print(random.randrange(n1, n2))