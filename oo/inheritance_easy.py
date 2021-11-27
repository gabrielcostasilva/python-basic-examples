from very_first_example import Person

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def print(self):
        super().print()
        print(f"Major in {self.major}")

s1 = Student("Catherine Zeta Jones", 54, "Arts")
s1.print()