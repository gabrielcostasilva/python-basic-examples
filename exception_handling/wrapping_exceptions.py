class MyOwnExceptionError(Exception):
    pass


def do_exception():
    try:
        1/0
    except ZeroDivisionError as error:
        raise MyOwnExceptionError from error
    
if __name__ == "__main__":
    try:
        do_exception()
    except MyOwnExceptionError:
        print("My exception was caught!")