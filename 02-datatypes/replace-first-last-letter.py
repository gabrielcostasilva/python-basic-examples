yourName = input("Enter your name: ").strip()
print("Inverting the first and last letter your name, we've got \'{}\' ".format(yourName.replace(yourName[0], yourName[-1]).capitalize()))
# The replace() method replaces all occurrences!