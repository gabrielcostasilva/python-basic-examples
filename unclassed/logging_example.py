import logging

logging.basicConfig(level=logging.DEBUG,
                    format="%(levelname)s %(asctime)s - %(message)s")

logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())

inputOne = input("Enter an integer number: ").strip()
numberOne = 0

if not inputOne.isnumeric():
    logger.error("Ooops, it seems the input is not a number!")
    raise Exception("Your input is not a number")
else:
    logger.info("Ok, number registered!")
    numberOne = int(inputOne)

inputTwo = input("Enter another integer number: ").strip()
numberTwo = 0

if not inputTwo.isnumeric():
    logger.error("Ooops, it seems the input is not a number!")
    raise Exception("Your input is not a number")
else:
    numberTwo = int(inputTwo)
    logger.info("Ok, number registered!")

logger.info("Input phase status: passed!")

sum = numberOne + numberTwo
logger.info("Calculation phase: passed!")

logger.info("Proceeding to last phase ...")

print(f"The result is '{sum}'")

logger.info("Result phase: passed!")
