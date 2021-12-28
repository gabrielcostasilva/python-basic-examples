from typing import Type

def check_number(number):
    if not number.isnumeric():
        raise TypeError("This is not a number!")

    int_number = int(number)

    if int_number <= 0:
        raise ValueError("Not a positive number!")

    return int_number

def main():
    number = input("Enter a positive integer: ").strip()
    a_number = 0

    try:
        a_number = check_number(number)

    except TypeError as e:
        print(e)
        main()

    except ValueError as e:
        print(e)
        main()

    except Exception:
        print("Unexpected error. Please, contact support.")

    else:
        print("Status code: 200")

    finally:
        print("Done!")

if __name__ == '__main__':
    main()
