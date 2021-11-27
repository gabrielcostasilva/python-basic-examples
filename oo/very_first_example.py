class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print(f"name = '{self.name}', age = {self.age}")

def main():
    p1 = Person("John Doe", 33)
    p2 = Person("Anna Doe", 35)

    p1.print()
    p2.print()

if __name__ == "__main__":
    main()