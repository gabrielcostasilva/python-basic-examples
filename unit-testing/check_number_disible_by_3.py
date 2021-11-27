def check(number):
    if not number.isnumeric():
        raise Exception("Argument is not a number!")

    if number % 3 == 0:
        return True
    else:
        return False