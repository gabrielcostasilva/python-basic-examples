fullDate = input("Enter a full date following this format: ddmmyy: ").strip()
intFullDate = int(fullDate)
day = int(intFullDate / 10000)
month = int(intFullDate % 10000 / 100)
year = int(intFullDate % 100)
# print("The formatted full date is ", day, " / ", month, " / ", year)
print("The formatted full date is {}/{}/{}".format(day, month, year))