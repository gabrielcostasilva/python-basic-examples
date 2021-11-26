age = int(input("Inform your age: "))
salary = float(input("Inform your salary: "))

ageType = str(type(age))
salaryType = str(type(salary))

strAge = str(age) 
strSalary = str(salary)

print("Your age ({}) is of type {}".format(strAge, ageType))
print("Your salary ({}) is of type {}".format(strSalary, salaryType))
